class GameInfo:
    def __init__(
        self,
        name,
        releaseYear,
        series=None,
        subseries=None,
        family=None,
        releaseType="original"
    ):
        self.name = name
        self.releaseYear = releaseYear
        self.series = series
        self.subseries = subseries
        self.family = family
        self.releaseType = releaseType
games = [
    GameInfo(
        "Persona 3",
        2006,
        series="Persona",
        family="Persona 3",
        releaseType="original"
    ),
    GameInfo(
        "Persona 3 FES",
        2007,
        series="Persona",
        family="Persona 3",
        releaseType="expanded_rerelease"
    ),
    GameInfo(
        "Persona 3 Portable",
        2009,
        series="Persona",
        family="Persona 3",
        releaseType="expanded_rerelease"
    ),
    GameInfo(
        "Persona 3 Reload",
        2024,
        series="Persona",
        family="Persona 3",
        releaseType="remake"
    ),
    GameInfo(
        "Shin Megami Tensei Devil Summoner",
        1995,
        series="Devil Summoner",
        subseries="Devil Summoner",
        family="Devil Summoner",
        releaseType="original"
    ),
    GameInfo(
        "Shin Megami Tensei Devil Summoner",
        1995,
        series="Devil Summoner",
        subseries="Devil Summoner",
        family="Devil Summoner",
        releaseType="original"
    ),
    GameInfo(
        "Shin Megami Tensei Devil Summoner (PSP)",
        2005,
        series="Devil Summoner",
        subseries="Devil Summoner",
        family="Devil Summoner",
        releaseType="expanded_rerelease"
    ),
    GameInfo(
        "Devil Summoner: Soul Hackers",
        1997,
        series="Devil Summoner",
        subseries="Soul Hackers",
        family="Soul Hackers",
        releaseType="original"
    ),

    GameInfo(
        "Devil Summoner: Soul Hackers (3DS)",
        2012,
        series="Devil Summoner",
        subseries="Soul Hackers",
        family="Soul Hackers",
        releaseType="expanded_rerelease"
    ),

    GameInfo(
        "Devil Summoner: Raidou Kuzunoha vs. The Soulless Army",
        2006,
        series="Devil Summoner",
        subseries="Raidou Kuzunoha",
        family="Raidou 1",
        releaseType="original"
    ),

    GameInfo(
        "Raidou Remastered: The Mystery of the Soulless Army",
        2025,
        series="Devil Summoner",
        subseries="Raidou Kuzunoha",
        family="Raidou 1",
        releaseType="remaster"
    ),

    GameInfo(
        "Devil Summoner 2: Raidou Kuzunoha vs. King Abaddon",
        2008,
        series="Devil Summoner",
        subseries="Raidou Kuzunoha",
        family="Raidou 2",
        releaseType="original"
    ),

    GameInfo(
        "Soul Hackers 2",
        2022,
        series="Devil Summoner",
        subseries="Soul Hackers",
        family="Soul Hackers 2",
        releaseType="original"
    ),
    GameInfo(
        "Shin Megami Tensei",
        1992,
        series="Mainline",
        subseries="SFC Trio",
        family="Shin Megami Tensei",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei II",
        1994,
        series="Mainline",
        subseries="SFC Trio",
        family="Shin Megami Tensei II",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei if...",
        1994,
        series="Mainline",
        subseries="SFC Trio",
        family="Shin Megami Tensei if...",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei NINE",
        2002,
        series="Online",
        subseries="NINE",
        family="Shin Megami Tensei NINE",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei IMAGINE",
        2002,
        series="Online",
        subseries="IMAGINE",
        family="Shin Megami Tensei IMAGINE",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei III: Nocturne",
        2003,
        series="Mainline",
        subseries="Nocturne",
        family="Shin Megami Tensei III",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei III: Nocturne Maniax",
        2004,
        series="Mainline",
        subseries="Nocturne",
        family="Shin Megami Tensei III",
        releaseType="expanded_rerelease"
    ),

    GameInfo(
        "Shin Megami Tensei III: Nocturne Chronicle",
        2008,
        series="Mainline",
        subseries="Nocturne",
        family="Shin Megami Tensei III",
        releaseType="expanded_rerelease"
    ),

    GameInfo(
        "Shin Megami Tensei III: Nocturne HD Remaster",
        2021,
        series="Mainline",
        subseries="Nocturne",
        family="Shin Megami Tensei III",
        releaseType="expanded_rerelease"
    ),

    GameInfo(
        "Shin Megami Tensei: Strange Journey",
        2009,
        series="Mainline",
        subseries="Strange Journey",
        family="Strange Journey",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei: Strange Journey Redux",
        2017,
        series="Mainline",
        subseries="Strange Journey",
        family="Strange Journey",
        releaseType="expanded_rerelease"
    ),

    GameInfo(
        "Shin Megami Tensei IV",
        2013,
        series="Mainline",
        subseries="Shin Megami Tensei IV",
        family="Shin Megami Tensei IV",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei IV: Apocalypse",
        2016,
        series="Mainline",
        subseries="Shin Megami Tensei IV",
        family="Shin Megami Tensei IV: Apocalypse",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei V",
        2021,
        series="Mainline",
        subseries="V",
        family="Shin Megami Tensei V",
        releaseType="original"
    ),

    GameInfo(
        "Shin Megami Tensei V: Vengeance",
        2024,
        series="Mainline",
        subseries="V",
        family="Shin Megami Tensei V",
        releaseType="expanded_rerelease"
    ),
]
