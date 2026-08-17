import requests
from pathlib import Path
Path("raw_pages").mkdir(exist_ok=True)
import re

html = ""
pages = ["List_of_Devil_Summoner:_Raidou_Kuzunoha_vs._King_Abaddon_Demons", "List_of_Devil_Summoner:_Raidou_Kuzunoha_vs._The_Soulless_Army_Demons", "List_of_Devil_Summoner:_Soul_Hackers_Demons",  "List_of_Devil_Survivor_2_Demons", "List_of_Devil_Survivor_Overclocked_Demons", "List_of_Majin_Tensei_Demons", "List_of_Majin_Tensei_II:_Spiral_Nemesis_Demons", "List_of_Megami_Tensei_Demons", "List_of_Megami_Tensei_II_Demons", "List_of_Ronde_Demons", "List_of_Shin_Megami_Tensei_Demons", "List_of_Shin_Megami_Tensei_II_Demons", "List_of_Shin_Megami_Tensei_III:_Nocturne_Demons", "List_of_Shin_Megami_Tensei_IV_Apocalypse_Demons", "List_of_Shin_Megami_Tensei_IV_Demons", "List_of_Shin_Megami_Tensei_NINE_Demons", "List_of_Shin_Megami_Tensei_V_Demons", "List_of_Shin_Megami_Tensei_V:_Vengeance_Demons", "List_of_Shin_Megami_Tensei:_Devil_Summoner_Demons", "List_of_Shin_Megami_Tensei:_if..._Demons", "List_of_Shin_Megami_Tensei:_Strange_Journey_Demons", "List_of_Soul_Hackers_2_Demons", "List_of_Megami_Ibunroku_Persona_Demons", "List_of_Persona_2:_Innocent_Sin_Personas", "List_of_Persona_2:_Innocent_Sin_Demons", "List_of_Persona_2:_Eternal_Punishment_Personas", "List_of_Persona_2:_Eternal_Punishment_Demons", "List_of_Persona_3_Personas", "List_of_Persona_3_Reload_Personas", "List_of_Persona_3_Portable_Personas", "List_of_Persona_3_FES_Personas", "List_of_Persona_4_Personas", "List_of_Persona_5_Personas", "List_of_Persona_5_Royal_Personas", "List_of_Digital_Devil_Saga:_Avatar_Tuner_Demons", "List_of_Digital_Devil_Saga:_Avatar_Tuner_2_Demons", "List_of_Megami_Ibunroku_Persona_Personas", "List_of_Persona_Q_Personas", "List_of_Persona_Q2_Personas", "List_of_Shin_Megami_Tensei_IMAGINE_Demons","List_of_RAIDOU_Remastered:_The_Mystery_of_the_Soulless_Army_Demons"]
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
scrape()