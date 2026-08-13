from bs4 import BeautifulSoup
from pathlib import Path
Path("raw_pages").mkdir(exist_ok=True)
import re

class Demon_Instance:
    def __init__(self, givenName, race, level, game):
        self.givenName = givenName
        self.race = race
        self.level = level
        self.game = game

    def __str__(self):
        return self.givenName + " | " + self.race + " | " + str(self.level) + " | " + self.game
Compendium = []
html = ""
#pages = ["List_of_Devil_Summoner:_Raidou_Kuzunoha_vs._King_Abaddon_Demons", "List_of_Devil_Summoner:_Raidou_Kuzunoha_vs._The_Soulless_Army_Demons", "List_of_Devil_Summoner:_Soul_Hackers_Demons",  "List_of_Devil_Survivor_2_Demons", "List_of_Devil_Survivor_Overclocked_Demons", "List_of_Majin_Tensei_Demons", "List_of_Majin_Tensei_II:_Spiral_Nemesis_Demons", "List_of_Megami_Tensei_Demons", "List_of_Megami_Tensei_II_Demons", "List_of_Ronde_Demons", "List_of_Shin_Megami_Tensei_Demons", "List_of_Shin_Megami_Tensei_II_Demons", "List_of_Shin_Megami_Tensei_III:_Nocturne_Demons", "List_of_Shin_Megami_Tensei_IV_Apocalypse_Demons", "List_of_Shin_Megami_Tensei_IV_Demons", "List_of_Shin_Megami_Tensei_NINE_Demons", "List_of_Shin_Megami_Tensei_V_Demons", "List_of_Shin_Megami_Tensei_V:_Vengeance_Demons", "List_of_Shin_Megami_Tensei:_Devil_Summoner_Demons", "List_of_Shin_Megami_Tensei:_if..._Demons", "List_of_Shin_Megami_Tensei:_Strange_Journey_Demons", "List_of_Soul_Hackers_2_Demons", "List_of_Megami_Ibunroku_Persona_Demons", "List_of_Persona_2:_Innocent_Sin_Personas", "List_of_Persona_2:_Innocent_Sin_Demons", "List_of_Persona_2:_Eternal_Punishment_Personas", "List_of_Persona_2:_Eternal_Punishment_Demons", "List_of_Persona_3_Personas", "List_of_Persona_3_Reload_Personas", "List_of_Persona_3_Portable_Personas", "List_of_Persona_3_FES_Personas", "List_of_Persona_4_Personas", "List_of_Persona_5_Personas", "List_of_Persona_5_Royal_Personas", "List_of_Digital_Devil_Saga:_Avatar_Tuner_Demons", "List_of_Digital_Devil_Saga:_Avatar_Tuner_2_Demons", ""List_of_Megami_Ibunroku_Persona_Personas"]

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


    return race.strip()

def parseCompendium():
    import re

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

                givenName = nameLink.get_text(" ", strip=True)

                if not givenName:
                    continue

                # Clean markers such as *
                while givenName and not givenName[-1].isalnum():
                    givenName = givenName[:-1].rstrip()

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
                    gameName
                )

                Compendium.append(demon)

    for file in Path("raw_pages").glob("*.html"):
        html = file.read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")

        gameName = file.stem
        gameName = gameName.replace("_", " ")
        gameName = gameName.removeprefix("List of ")
        gameName = gameName.removesuffix(" Demons")
        gameName = gameName.removesuffix(" Personas")

        if gameName == "Megami Ibunroku Persona":
            parsePersona1Table()
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

                headers = [th.get_text(strip=True) for th in table.find_all("th")]

                if "Level" not in headers:
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

                levelIndex = headers.index("Level")

                for row in table.find_all("tr"):
                    cells = row.find_all(["td", "th"])

                    # Avoid header rows and malformed rows
                    if len(cells) <= max(nameIndex, levelIndex):
                        continue

                    givenName = cells[nameIndex].get_text(strip=True)
                    level = cells[levelIndex].get_text(strip=True)

                    if givenName == "":
                        continue


                    if level.isnumeric()== False:
                        level = level[:-1]

                    # Skip header-like rows accidentally picked up by find_all(["td","th"])
                    if givenName in ["Demon", "Persona", "Name", "Boss"]:
                        continue

                    race = normalizeRace(race)
                    if not race.isascii():
                        continue
                    demon = Demon_Instance(
                        givenName,
                        race,
                        level,
                        gameName
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

                        headers = [
                            th.get_text(strip=True)
                            for th in table.find_all("th")
                        ]

                        if "Level" not in headers:
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

                        levelIndex = headers.index("Level")

                        for row in table.find_all("tr"):
                            cells = row.find_all(["td", "th"])

                            if len(cells) <= max(nameIndex, levelIndex):
                                continue

                            givenName = cells[nameIndex].get_text(strip=True)
                            level = cells[levelIndex].get_text(strip=True)

                            if givenName == "":
                                continue



                            if givenName in ["Demon", "Persona", "Name", "Boss"]:
                                continue
                            while race[-1].isalnum() == False:
                                race = race[:-1]

                            if level.isnumeric() == False:
                                level = level[:-1]
                            race = normalizeRace(race)
                            if not race.isascii():
                                continue
                            
                            demon = Demon_Instance(
                                givenName,
                                race,
                                level,
                                gameName
                            )

                            Compendium.append(demon)

                    element = element.find_next_sibling()
parseCompendium()
def writeOutput():
    with open("compendiumdbraw.txt", "w", encoding="utf-8") as file:
        for demon in Compendium:
            file.write(f"{demon}\n")
#BEHOLD, MY DEMONS
writeOutput()
#for demon in Compendium:
 #   print(demon)