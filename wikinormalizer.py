import requests
import json

API = "https://megamitensei.fandom.com/api.php"



def resolveRedirects(titles):
    params = {
        "action": "query",
        "titles": "|".join(titles),
        "redirects": 1,
        "format": "json"
    }

    response = requests.get(API, params=params)
    response.raise_for_status()
    return response.json()

names = []
with open("uniquenamelist.txt") as f:
    for line in f:
        names.append(line.strip())


batchSize = 50
redirectMap = {}

for i in range(0, len(names), batchSize):
    batch = names[i:i + batchSize]
    data = resolveRedirects(batch)

    redirects = data.get("query", {}).get("redirects", [])

    for redirect in redirects:
        redirectMap[redirect["from"]] = redirect["to"]

with open("redirect_map.json", "w", encoding="utf-8") as file:
    json.dump(
        redirectMap,
        file,
        ensure_ascii=False,
        indent=2
    )

print("Names checked:", len(names))
print("Redirects found:", len(redirectMap))