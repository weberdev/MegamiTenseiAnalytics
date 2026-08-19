import json
import re
from collections import defaultdict

with open("redirect_map.json", encoding="utf-8") as f:
    redirectMap = json.load(f)

def resolveWikiName(wikiName):
    return redirectMap.get(wikiName, wikiName)

def comparisonKey(name):
    return re.sub(r"[^a-z0-9]", "", name.casefold())

# Read your unique wiki names
names = []

with open("uniquenamelist.txt", encoding="utf-8") as f:
    for line in f:
        name = line.strip()

        if name:
            names.append(name)


# Apply wiki redirects
canonicalNames = {
    resolveWikiName(name)
    for name in names
}


# Save the post-redirect unique list
with open("canonicalnamelist.txt", "w", encoding="utf-8") as f:
    for name in sorted(canonicalNames):
        f.write(name + "\n")


# Group names that become identical if punctuation/spaces are ignored
comparisonGroups = defaultdict(set)

for name in canonicalNames:
    key = comparisonKey(name)
    comparisonGroups[key].add(name)


# Write only suspicious groups
with open("name_collisions.txt", "w", encoding="utf-8") as f:
    for key in sorted(comparisonGroups):
        variants = sorted(comparisonGroups[key])

        if len(variants) > 1:
            f.write(f"{key}\n")

            for name in variants:
                f.write(f"    {name}\n")

            f.write("\n")


print("Original unique names:", len(names))
print("After redirects:", len(canonicalNames))
print("Redirects applied:", len(names) - len(canonicalNames))

tests = [
    "Ame no Uzume",
    "Ame-no-Uzume",
    "Ameno Uzume",
    "Girimehkala",
    "Girimekhala",
    "Pyro Jack",
    "Jack-o'-Lantern"
]

for name in tests:
    print(name, "->", resolveWikiName(name))