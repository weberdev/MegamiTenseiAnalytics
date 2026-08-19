from bs4 import BeautifulSoup
from pathlib import Path
Path("raw_pages").mkdir(exist_ok=True)
import re

class Demon_Instance:
    def __init__(self, givenName, race, level, game, canonicalName):
        self.givenName = givenName
        self.race = race
        self.level = level
        self.game = game
        self.canonicalName = canonicalName

    def __str__(self):
        return self.givenName + " | " + self.race + " | " + str(self.level) + " | " + self.game + " | " + self.canonicalName
Compendium = []
html = ""

def normalizeRace(race):
    if " (" in race:
        #print("removing clarification")
        race = race.split(" (", 1)[0]
    if " / " in race:
        #print("removing extraneous alignment data")
        race = race.split(" / ", 1)[0]
    if " Arcana" in race:
        race = race.split(" Arcana", 1)[0]
    if ".0" in race:
        race = race.split(".0", 1)[1]
    if ".0" in race:
        race = race.split(".0", 1)[1]
    if "Suit of " in race:
        race = race.split("Suit of ", 1)[1]
    if race== "Coins":
        race = "Coin"
    if race == "Swords":
        race = "Sword"
    if race == "Cups":
        race = "Cup"
    if race == "Wands":
        race = "Wand"
    if race == "Seraph/Herald":
        race = "Herald"
    if race == "02Priestess":
        race = "Priestess"

    return race.strip()

# a note on rereleases:
# some games have separate wiki entries for each version. That's awesome and makes my life easier.
# Some do not.
# Shin Megami Tensei: rerelease demons for Sega CD: †
# Likewise for Shin Megami Tensei II on the GBA: † or †#
# Nocturne and Soul Hackers: italics
# Devil Survivor 2: *

def parseCompendium():
    import re
    def parseModernPersonaTable():
        import re

        headings = soup.find_all("h2")

        for category in headings:
            raceSpan = category.find("span", class_="mw-headline")

            if raceSpan is None:
                continue

            arcana = raceSpan.get_text(" ", strip=True)

            # Find the table immediately following this Arcana heading
            table = category.find_next_sibling("table")

            if table is None:
                continue

            # Make sure this is actually one of the Persona roster tables
            headers = [
                th.get_text(" ", strip=True)
                for th in table.find_all("th")
            ]

            if "Level" not in headers or "Persona" not in headers:
                continue

            for row in table.find_all("tr"):
                cells = row.find_all(["th", "td"])

                if not cells:
                    continue

                # These tables are:
                # Level | Persona | Level | Persona | ...
                #
                # So walk them two cells at a time.
                for i in range(0, len(cells) - 1, 2):

                    levelCell = cells[i]
                    personaCell = cells[i + 1]

                    # Make sure the second cell really contains a Persona link.
                    nameLink = personaCell.find("a")

                    if nameLink is None:
                        continue

                    givenName = nameLink.get_text(" ", strip=True)

                    if not givenName:
                        continue

                    canonicalName = (
                            nameLink.get("title")
                            or givenName
                    )

                    levelText = levelCell.get_text(" ", strip=True)

                    # Pull a numeric level out of things like:
                    #
                    # 01*
                    # 64★
                    # 23↓
                    #
                    # "Inherit" has no numeric level.
                    match = re.search(r"\d+", levelText)

                    if match:
                        level = match.group()
                    else:
                        # Your current convention for unlevelled
                        # character Personas.
                        level = "1"

                    demon = Demon_Instance(
                        givenName,
                        arcana,
                        level,
                        gameName,
                        canonicalName
                    )

                    Compendium.append(demon)
    def parsePQInitialPersonas():
        heading = soup.find("span", id="Innate_Personas")

        if heading is None:
            return

        table = heading.parent.find_next_sibling("table")

        if table is None:
            return

        currentArcana = None

        for row in table.find_all("tr"):
            cells = row.find_all("td")

            if not cells:
                continue

            # In this table, the first td of a real Persona row is the Persona.
            personaCell = cells[0]
            nameLink = personaCell.find("a")

            if nameLink is None:
                continue

            givenName = nameLink.get_text(" ", strip=True)
            canonicalName = nameLink.get("title") or givenName

            # Some rows explicitly contain Arcana;
            # subsequent rowspan rows inherit the previous one.
            for cell in cells:
                arcanaLink = cell.find(
                    "a",
                    href=re.compile(r"Arcana")
                )

                if arcanaLink is not None:
                    currentArcana = arcanaLink.get_text(
                        " ",
                        strip=True
                    )
                    break

            if currentArcana is None:
                continue

            demon = Demon_Instance(
                givenName,
                currentArcana,
                1,
                gameName,
                canonicalName
            )

            Compendium.append(demon)
    def parseSoulHackersBosses():
        bossesHeading = soup.find(
            "span",
            class_="mw-headline",
            id="Bosses"
        )

        if bossesHeading is None:
            return

        element = bossesHeading.parent.find_next_sibling()

        while element is not None:
            # Stop when we hit the next h2-level section
            if element.name == "h2":
                break

            if element.name == "table":
                headers = [
                    th.get_text(strip=True)
                    for th in element.find_all("th")
                ]

                if "Demon" not in headers:
                    element = element.find_next_sibling()
                    continue

                nameIndex = headers.index("Demon")

                raceIndex = (
                    headers.index("Race")
                    if "Race" in headers
                    else None
                )

                levelIndex = (
                    headers.index("Lvl.")
                    if "Lvl." in headers
                    else None
                )

                for row in element.find_all("tr"):
                    cells = row.find_all(["td", "th"])

                    if len(cells) <= nameIndex:
                        continue

                    givenName = cells[nameIndex].get_text(strip=True)
                    if givenName == "Headless Rider *3":
                        givenName = "Headless Rider"

                    if givenName in ["", "Demon"]:
                        continue

                    nameLink = None

                    for link in cells[nameIndex].find_all("a"):
                        if link.get_text(strip=True) == givenName:
                            nameLink = link
                            break

                    if nameLink is not None:
                        canonicalName = nameLink.get("title") or givenName
                    else:
                        canonicalName = givenName
                    race = (
                        cells[raceIndex].get_text(strip=True)
                        if raceIndex is not None
                           and len(cells) > raceIndex
                        else "Boss"
                    )

                    level = (
                        cells[levelIndex].get_text(strip=True)
                        if levelIndex is not None
                           and len(cells) > levelIndex
                        else None
                    )
                    #print(givenName, race, level)
                    if givenName == "Headless Rider*3":
                        givenName = "Headless Rider"
                        canonicalName = "Headless Rider"
                    Compendium.append(
                        Demon_Instance(
                            givenName,
                            race,
                            level,
                            gameName,
                            canonicalName
                        )

                    )

            element = element.find_next_sibling()
    def parsePersona1Table():
        if "Demons" in file.stem:
            headings = soup.find_all("h3")
        else:
            headings = soup.find_all(["h2", "h3"])

        for category in headings:
            # IMPORTANT: only accept a table that is the next structural sibling.
            nextElement = category.find_next_sibling(["h2", "h3", "table"])

            if nextElement is None or nextElement.name != "table":
                continue

            table = nextElement

            raceSpan = category.find("span", class_="mw-headline")

            if raceSpan is None:
                continue

            race = normalizeRace(
                raceSpan.get_text(" ", strip=True)
            )

            for row in table.find_all("tr"):
                cells = row.find_all("td")

                if not cells:
                    continue

                nameLink = row.find("a")

                if nameLink is None:
                    continue

                nameLink = row.find("a")
                givenName = nameLink.get_text(" ", strip=True)
                canonicalName = nameLink.get("title")

                if not givenName:
                    continue


                level = None

                for cell in cells:
                    text = cell.get_text(" ", strip=True)

                    match = re.fullmatch(
                        r"\s*(\d+(?:\s*/\s*\d+)*)\s*[°*]?\s*",
                        text
                    )

                    if match:
                        level = match.group(1).replace(" ", "")
                        break

                if level is None:
                    continue

                demon = Demon_Instance(
                    givenName,
                    race,
                    level,
                    gameName,
                    canonicalName
                )

                Compendium.append(demon)

    for file in Path("raw_pages").glob("*.html"):
        html = file.read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")
        parsedTables = set()

        gameName = file.stem
        gameName = gameName.replace("_", " ")
        gameName = gameName.removeprefix("List of ")
        gameName = gameName.removesuffix(" Demons")
        gameName = gameName.removesuffix(" Personas")
        if gameName == "Devil Summoner  Soul Hackers":
            parseSoulHackersBosses()
        if gameName == "Persona Q" or gameName == "Persona Q2":
            parsePQInitialPersonas()
        if gameName == "Megami Ibunroku Persona":
            parsePersona1Table()
            continue
        modernPersonaGames = {
            "Persona 3",
            "Persona 3 FES",
            "Persona 3 Portable",
            "Persona 3 Reload",
            "Persona 4",
            "Persona 5",
            "Persona 5 Royal",
        }

        if gameName in modernPersonaGames:
            parseModernPersonaTable()
            continue
        # your existing generic parser continues here
        headings = soup.find_all(["h2", "h3", "h4"])


        for category in headings:

            # Look at the next meaningful structural element.
            nextElement = category.find_next_sibling(["h3", "table", "h2"])

            if nextElement is None:
                continue

            if nextElement.name == "table":

                race = category.find("span", class_="mw-headline")


                if race is None:
                    continue

                race = race.get_text(strip=True)
                table = nextElement
                tableID = id(table)

                if tableID in parsedTables:
                    continue

                parsedTables.add(tableID)
                headers = [th.get_text(strip=True) for th in table.find_all("th")]

                if "Level" not in headers and not (
                        gameName == "Persona Q"
                        and "Lv" in headers
                ):
                    continue

                if "Demon" in headers:
                    nameIndex = headers.index("Demon")
                elif "Persona" in headers:
                    nameIndex = headers.index("Persona")
                elif "Name" in headers:
                    nameIndex = headers.index("Name")
                elif "Boss" in headers:
                    nameIndex = headers.index("Boss")
                else:
                    continue

                if gameName == "Persona Q" and "Lv" in headers:
                    levelIndex = headers.index("Lv")
                else:
                    levelIndex = headers.index("Level")

                for row in table.find_all("tr"):
                    cells = row.find_all(["td", "th"])

                    # Avoid header rows and malformed rows
                    if len(cells) <= max(nameIndex, levelIndex):
                        continue

                    givenName = cells[nameIndex].get_text(strip=True)
                    level = cells[levelIndex].get_text(strip=True)
                    nameLink = cells[nameIndex].find("a")

                    if nameLink is not None:
                        wikiTitle = nameLink.get("title")
                    else:
                        wikiTitle = givenName
                    canonicalName = wikiTitle

                    if givenName == "":
                        continue


                    if level.isnumeric()== False:
                        level = level[:-1]

                    # Skip header-like rows accidentally picked up by find_all(["td","th"])
                    if givenName in ["Demon", "Persona", "Name", "Boss"]:
                        continue

                    race = normalizeRace(race)
                    if gameName == "Shin Megami Tensei  Devil Summoner" and "Race" in headers:
                        race = cells[1].get_text(strip=True)
                    if not race.isascii() and race != "Onryō" and race != "Zōma":
                        continue
                    if gameName == "Devil Summoner  Soul Hackers" or gameName == "Shin Megami Tensei  Devil Summoner" or gameName == "Shin Megami Tensei III  Nocturne":
                        if cells[nameIndex].find(["i", "em"]) is not None:
                            givenName = givenName + " †"

                    def isReduxExclusive(nameCell):
                        style = nameCell.get("style", "").replace(" ", "").lower()
                        return "background:#000088" in style
                    if gameName == "Shin Megami Tensei  Strange Journey":
                        nameCell = cells[nameIndex]
                        if isReduxExclusive(nameCell):
                            givenName = givenName + " †"
                    if gameName == "Devil Survivor 2" and givenName[-1] == "*":
                        givenName = givenName[:-1]+" †"
                    if gameName == "Persona Q":
                        race = cells[1].get_text(strip=True)
                    if gameName == "Persona Q":
                        race = re.sub(r'^\d+\.0', '', race)
                    if race == "02Priestess":
                        race = "Priestess"

                    demon = Demon_Instance(
                        givenName,
                        race,
                        level,
                        gameName,
                        canonicalName
                    )

                    Compendium.append(demon)

            elif nextElement.name == "h3":

                element = category.find_next_sibling()

                while element is not None and element.name != "h2":

                    if element.name == "h3":
                        raceSpan = element.find("span", class_="mw-headline")

                        if raceSpan is None:
                            element = element.find_next_sibling()
                            continue

                        raceLink = raceSpan.find("a")

                        if raceLink is not None:
                            race = raceLink.get("title")
                        else:
                            race = raceSpan.get_text(strip=True)

                        if race == "Element (race)":
                            race = "Element"


                        table = element.find_next_sibling("table")

                        if table is None:
                            element = element.find_next_sibling()
                            continue
                        tableID = id(table)

                        if tableID in parsedTables:
                            continue

                        parsedTables.add(tableID)
                        headers = [
                            th.get_text(strip=True)
                            for th in table.find_all("th")
                        ]

                        if "Level" not in headers and not (gameName == "Persona Q" and "Lv" in headers):
                            element = element.find_next_sibling()
                            continue

                        if "Demon" in headers:
                            nameIndex = headers.index("Demon")
                        elif "Persona" in headers:
                            nameIndex = headers.index("Persona")
                        elif "Name" in headers:
                            nameIndex = headers.index("Name")
                        elif "Boss" in headers:
                            nameIndex = headers.index("Boss")
                        else:
                            element = element.find_next_sibling()
                            continue

                        if gameName == "Persona Q" and "Lv" in headers:
                            levelIndex = headers.index("Lv")
                        else:
                            levelIndex = headers.index("Level")

                        for row in table.find_all("tr"):
                            cells = row.find_all(["td", "th"])

                            if len(cells) <= max(nameIndex, levelIndex):
                                continue

                            givenName = cells[nameIndex].get_text(strip=True)
                            level = cells[levelIndex].get_text(strip=True)
                            nameLink = cells[nameIndex].find("a")

                            if nameLink is not None:
                                wikiTitle = nameLink.get("title")
                            else:
                                wikiTitle = givenName
                            canonicalName = wikiTitle


                            if givenName == "":
                                continue



                            if givenName in ["Demon", "Persona", "Name", "Boss"]:
                                continue
                            while race[-1].isalnum() == False:
                                race = race[:-1]

                            if level.isnumeric() == False:
                                level = level[:-1]
                            if gameName == "Persona Q":
                                race = cells[1].get_text(strip=True)
                            race = normalizeRace(race)
                            if not race.isascii() or race == "Onryō" or race == "Zōma":
                                continue
                            if gameName == "Devil Summoner  Soul Hackers":
                                if cells[nameIndex].find(["i", "em"]) is not None:
                                    givenName = givenName + " †"

                            def isReduxExclusive(nameCell):
                                style = nameCell.get("style", "").replace(" ", "").lower()
                                return "background:#000088" in style

                            if gameName == "Shin Megami Tensei  Strange Journey":
                                nameCell = cells[nameIndex]
                                if isReduxExclusive(nameCell):
                                    givenName = givenName + " †"
                            if gameName == "Devil Survivor 2" and givenName[-1] == "*":
                                givenName = givenName[:-1] + " †"
                            if gameName == "Persona Q":
                                race = cells[1].get_text(strip=True)
                            if gameName == "Persona Q":
                                race = re.sub(r'^\d+\.0', '', race)
                            if race == "02Priestess":
                                race = "Priestess"

                            demon = Demon_Instance(
                                givenName,
                                race,
                                level,
                                gameName,
                                canonicalName
                            )

                            Compendium.append(demon)

                    element = element.find_next_sibling()
parseCompendium()
import copy

gamesWithRereleases = {
    "Persona 4": "Persona 4 Golden",
    "Devil Survivor 2": "Devil Survivor 2 Record Breaker",
    "Shin Megami Tensei": "Shin Megami Tensei (Sega CD)",
    "Shin Megami Tensei II": "Shin Megami Tensei II (GBA)",
    "Shin Megami Tensei  Strange Journey": "Shin Megami Tensei Strange Journey Redux",
    "Shin Megami Tensei  Devil Summoner": "Shin Megami Tensei  Devil Summoner (PSP)",
    "Shin Megami Tensei III  Nocturne": "Shin Megami Tensei III  Nocturne MANIAX",
    "Devil Summoner  Soul Hackers": "Devil Summoner Soul Hackers (3DS)"
}

expandedCompendium = []

for demon in Compendium:
    if demon.game not in gamesWithRereleases:
        expandedCompendium.append(demon)
        continue

    rereleaseDemon = copy.copy(demon)
    rereleaseDemon.game = gamesWithRereleases[demon.game]

    rereleaseOnly = (
        "[Golden only]" in demon.race
        or "†" in demon.givenName
    )

    if rereleaseOnly:
        rereleaseDemon.givenName = rereleaseDemon.givenName.replace("†", "").strip()
        rereleaseDemon.race = rereleaseDemon.race.replace("[Golden only]", "").strip()
        if "Nocturne" in rereleaseDemon.game:
            nocturneIsASpecialGameDemonHDTurboHDRemixDemon = copy.copy(rereleaseDemon)
            nocturneIsASpecialGameDemonHDTurboHDRemixDemon.game = "Shin Megami Tensei III  Nocturne HD Remaster"
            expandedCompendium.append(nocturneIsASpecialGameDemonHDTurboHDRemixDemon)
            #I love Nocturne, honestly.
            #There's no actual roster change beyond handsome charming boy Raidou, but that's enough to special case Chronicle.
            nocturneIsASpecialGameDemonHDTurboHDRemixDemon.game = "Shin Megami Tensei III  Nocturne Chronicle"
            expandedCompendium.append(nocturneIsASpecialGameDemonHDTurboHDRemixDemon)
        expandedCompendium.append(rereleaseDemon)

    else:
        expandedCompendium.append(demon)
        expandedCompendium.append(rereleaseDemon)

Compendium = expandedCompendium

for demon in Compendium:
    if demon.level == "Innat":
        demon.level = 1
    if "(" in demon.givenName:
        demon.givenName = demon.givenName.split("(", 1)[0]
    while demon.givenName[-1].isalnum() == False:
        demon.givenName = demon.givenName[:-1]


Compendium.sort(
    key=lambda demon: (
        demon.game,
        demon.race
    )
)
def writeOutput():
    with open("compendiumdbraw.txt", "w", encoding="utf-8") as file:
        for demon in Compendium:
            file.write(f"{demon}\n")
def writeNames():
    names = set()

    for demon in Compendium:
        name = demon.canonicalName

        names.add(name)

    names = sorted(names)

    with open("uniquenamelist.txt", "w", encoding="utf-8") as file:
        for name in names:
            file.write(f"{name}\n")
#BEHOLD, MY DEMONS
writeOutput()
writeNames()
#for demon in Compendium:
 #   print(demon)