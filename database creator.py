import sqlite3

import redirectparser
import parser
import os

if os.path.exists("compendium.db"):
    os.remove("compendium.db")

parser.Compendium.clear()
parser.parseCompendium()

Compendium = parser.Compendium

def getOrCreateGame(name, releaseYear=None):
    cursor.execute(
        "SELECT game_id FROM Game WHERE name = ?",
        (name,)
    )

    row = cursor.fetchone()

    if row is not None:
        return row[0]

    cursor.execute(
        """
        INSERT INTO Game (name, release_year)
        VALUES (?, ?)
        """,
        (name, releaseYear)
    )

    return cursor.lastrowid



def getOrCreateDemon(canonicalName, wikiName):
    cursor.execute(
        """
        SELECT demon_id
        FROM Demon
        WHERE canonical_name = ?
        """,
        (canonicalName,)
    )
    row = cursor.fetchone()

    if row is not None:
        return row[0]

    cursor.execute(
        """
        INSERT INTO Demon (
            canonical_name,
            wiki_name
        )
        VALUES (?, ?)
        """,
        (
            canonicalName,
            wikiName
        )
    )

    return cursor.lastrowid

def insertAppearance(
    demonID,
    gameID,
    givenName,
    classification,
    level
):
    cursor.execute(
        """
        INSERT INTO Appearance (
            demon_id,
            game_id,
            given_name,
            classification,
            level
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            demonID,
            gameID,
            givenName,
            classification,
            level
        )
    )

connection = sqlite3.connect("compendium.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")



cursor.execute("""
CREATE TABLE IF NOT EXISTS GameFamily (
    family_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Game (
    game_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    release_year INTEGER,
    series TEXT,
    subseries TEXT,
    family_id INTEGER,
    FOREIGN KEY (family_id)
        REFERENCES GameFamily(family_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Demon (
    demon_id INTEGER PRIMARY KEY,
    canonical_name TEXT NOT NULL,
    wiki_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Mythology (
    mythology_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS DemonMythology (
    demon_id INTEGER NOT NULL,
    mythology_id INTEGER NOT NULL,
    PRIMARY KEY (demon_id, mythology_id),
    FOREIGN KEY (demon_id)
        REFERENCES Demon(demon_id),
    FOREIGN KEY (mythology_id)
        REFERENCES MYTHOLOGY(mythology_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Appearance (
    appearance_id INTEGER PRIMARY KEY,
    demon_id INTEGER NOT NULL,
    game_id INTEGER NOT NULL,
    given_name TEXT NOT NULL,
    classification TEXT,
    level TEXT,
    FOREIGN KEY (demon_id) REFERENCES Demon(demon_id),
    FOREIGN KEY (game_id) REFERENCES Game(game_id)
)
""")

for demon in Compendium:
    resolvedCanonicalName = redirectparser.resolveWikiName(demon.canonicalName)

    demonID = getOrCreateDemon(
        resolvedCanonicalName,
        demon.canonicalName
    )

    gameID = getOrCreateGame(demon.game)

    insertAppearance(
        demonID,
        gameID,
        demon.givenName,
        demon.race,
        demon.level
    )
cursor.execute("""
UPDATE Demon
SET canonical_name = ?
WHERE canonical_name = ?
""", ("Maya", "Maya (demon, Mayan)"))

cursor.execute("""
UPDATE Demon
SET canonical_name = ?
WHERE canonical_name = ?
""", ("Maya", "Maya (demon, Hindu)"))

connection.commit()
connection.close()