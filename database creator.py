import sqlite3
connection = sqlite3.connect('compendium.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Demon (
demon_id INTEGER PRIMARY KEY AUTOINCREMENT,
canonical_name TEXT NOT NULL,
source_mythology TEXT NOT NULL)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Game (
game_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
release_year INTEGER NOT NULL,
series TEXT,
subseries TEXT,
game_family TEXT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Appearance (
    appearance_id INTEGER PRIMARY KEY,
    demon_id INTEGER NOT NULL,
    game_id INTEGER NOT NULL,
    display_name TEXT NOT NULL,
    classification TEXT,
    level TEXT,
    FOREIGN KEY (demon_id) REFERENCES Demon(demon_id),
    FOREIGN KEY (game_id) REFERENCES Game(game_id)
)
""")