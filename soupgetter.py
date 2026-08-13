import requests
from bs4 import BeautifulSoup
from pathlib import Path
Path("raw_pages").mkdir(exist_ok=True)

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
pages = ["List_of_Devil_Summoner:_Raidou_Kuzunoha_vs._King_Abaddon_Demons", "List_of_Devil_Summoner:_Raidou_Kuzunoha_vs._The_Soulless_Army_Demons", "List_of_Devil_Summoner:_Soul_Hackers_Demons",  "List_of_Devil_Survivor_2_Demons", "List_of_Devil_Survivor_Overclocked_Demons", "List_of_Majin_Tensei_Demons", "List_of_Majin_Tensei_II:_Spiral_Nemesis_Demons", "List_of_Megami_Tensei_Demons", "List_of_Megami_Tensei_II_Demons", "List_of_Ronde_Demons", "List_of_Shin_Megami_Tensei_Demons", "List_of_Shin_Megami_Tensei_II_Demons", "List_of_Shin_Megami_Tensei_III:_Nocturne_Demons", "List_of_Shin_Megami_Tensei_IV_Apocalypse_Demons", "List_of_Shin_Megami_Tensei_IV_Demons", "List_of_Shin_Megami_Tensei_NINE_Demons", "List_of_Shin_Megami_Tensei_V_Demons", "List_of_Shin_Megami_Tensei_V:_Vengeance_Demons", "List_of_Shin_Megami_Tensei:_Devil_Summoner_Demons", "List_of_Shin_Megami_Tensei:_if..._Demons", "List_of_Shin_Megami_Tensei:_Strange_Journey_Demons", "List_of_Soul_Hackers_2_Demons", "List_of_Megami_Ibunroku_Persona_Demons", "List_of_Persona_2:_Innocent_Sin_Personas", "List_of_Persona_2:_Innocent_Sin_Demons", "List_of_Persona_2:_Eternal_Punishment_Personas", "List_of_Persona_2:_Eternal_Punishment_Demons", "List_of_Persona_3_Personas", "List_of_Persona_3_Reload_Personas", "List_of_Persona_3_Portable_Personas", "List_of_Persona_3_FES_Personas", "List_of_Persona_4_Personas", "List_of_Persona_5_Personas", "List_of_Persona_5_Royal_Personas"]
def scrape():
    url = "https://megamitensei.fandom.com/api.php"
    for p in pages:
        params = {
            "action": "parse",
            "page": p,
            "prop": "text",
            "format": "json"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if "parse" not in data:
            print("FAILED:", p)
            print(data)
            continue

        html = data["parse"]["text"]["*"]

        filename = p.replace(":", "_") + ".html"
        Path("raw_pages", filename).write_text(html, encoding="utf-8")
#scrape()
def parseCompendium():
    for file in Path("raw_pages").glob("*.html"):
        html = file.read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")
        gameName = file.stem
        gameName = gameName.replace("_", " ")
        gameName = gameName.removeprefix("List of ")
        gameName = gameName.removesuffix(" Demons")
        gameName = gameName.removesuffix(" Personas")
        headings = soup.find_all("h2")

        for category in headings:
            table = category.find_next_sibling("table")

            if table is None:
                continue
            headers = [th.get_text(strip=True) for th in table.find_all("th")]

            if "Level" not in headers:
                continue
            if "Demon" in headers:
                nameIndex = headers.index("Demon")
            elif "Persona" in headers:
                nameIndex = headers.index("Persona")
            elif "Name" in headers:
                nameIndex = headers.index("Name")
            else:
                continue

            levelIndex = headers.index("Level")



            race = category.get_text(strip=True)
            race = race[:-2]

            rows = table.find_all("tr")

            for row in table.find_all("tr"):
                cells = row.find_all("td")

                if len(cells) <= max(nameIndex, levelIndex):
                    continue

                givenName = cells[nameIndex].get_text(strip=True)
                level = cells[levelIndex].get_text(strip=True)
                lastChar= givenName[:1]
                if lastChar == "*":
                    givenName = givenName[:-1]

                level = cells[1].get_text(strip=True)

                demon = Demon_Instance(givenName, race, level, gameName)
                print(demon)
                Compendium.append(demon)
parseCompendium()

#BEHOLD, MY DEMONS
#for demon in Compendium:
 #   print(demon)