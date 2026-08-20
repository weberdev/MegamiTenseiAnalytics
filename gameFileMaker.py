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
def makeGameList():
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
            "Shin Megami Tensei  Devil Summoner",
            1995,
            series="Devil Summoner",
            subseries="Devil Summoner",
            family="Devil Summoner",
            releaseType="original"
        ),
        GameInfo(
            "Shin Megami Tensei  Devil Summoner (PSP)",
            2005,
            series="Devil Summoner",
            subseries="Devil Summoner",
            family="Devil Summoner",
            releaseType="expanded_rerelease"
        ),
        GameInfo(
            "Devil Summoner  Soul Hackers",
            1997,
            series="Devil Summoner",
            subseries="Soul Hackers",
            family="Soul Hackers",
            releaseType="original"
        ),

        GameInfo(
            "Devil Summoner Soul Hackers (3DS)",
            2012,
            series="Devil Summoner",
            subseries="Soul Hackers",
            family="Soul Hackers",
            releaseType="expanded_rerelease"
        ),

        GameInfo(
            "Devil Summoner  Raidou Kuzunoha vs. The Soulless Army",
            2006,
            series="Devil Summoner",
            subseries="Raidou Kuzunoha",
            family="Raidou 1",
            releaseType="original"
        ),

        GameInfo(
            "RAIDOU Remastered  The Mystery of the Soulless Army",
            2025,
            series="Devil Summoner",
            subseries="Raidou Kuzunoha",
            family="Raidou 1",
            releaseType="remaster"
        ),

        GameInfo(
            "Devil Summoner  Raidou Kuzunoha vs. King Abaddon",
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
            "Shin Megami Tensei (Sega CD)",
            1994,
            series="Mainline",
            subseries="SFC Trio",
            family="Shin Megami Tensei",
            releaseType="expanded_rerelease"
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
            "Shin Megami Tensei II (GBA)",
            2002,
            series="Mainline",
            subseries="SFC Trio",
            family="Shin Megami Tensei II",
            releaseType="expanded_rerelease"
        ),

        GameInfo(
            "Shin Megami Tensei  if...",
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
            "Shin Megami Tensei III  Nocturne",
            2003,
            series="Mainline",
            subseries="Nocturne",
            family="Shin Megami Tensei III",
            releaseType="original"
        ),

        GameInfo(
            "Shin Megami Tensei III  Nocturne MANIAX",
            2004,
            series="Mainline",
            subseries="Nocturne",
            family="Shin Megami Tensei III",
            releaseType="expanded_rerelease"
        ),

        GameInfo(
            "Shin Megami Tensei III  Nocturne Chronicle",
            2008,
            series="Mainline",
            subseries="Nocturne",
            family="Shin Megami Tensei III",
            releaseType="expanded_rerelease"
        ),

        GameInfo(
            "Shin Megami Tensei III  Nocturne HD Remaster",
            2021,
            series="Mainline",
            subseries="Nocturne",
            family="Shin Megami Tensei III",
            releaseType="expanded_rerelease"
        ),

        GameInfo(
            "Shin Megami Tensei  Strange Journey",
            2009,
            series="Mainline",
            subseries="Strange Journey",
            family="Strange Journey",
            releaseType="original"
        ),

        GameInfo(
            "Shin Megami Tensei  Strange Journey Redux",
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
            "Shin Megami Tensei IV Apocalypse",
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
            "Shin Megami Tensei V  Vengeance",
            2024,
            series="Mainline",
            subseries="V",
            family="Shin Megami Tensei V",
            releaseType="expanded_rerelease"
        ),
        GameInfo(
            "Devil Survivor",
            2009,
            series="Devil Survivor",
            subseries=None,
            family="Devil Survivor",
            releaseType="original"
        ),

        GameInfo(
            "Devil Survivor Overclocked",
            2011,
            series="Devil Survivor",
            subseries=None,
            family="Devil Survivor",
            releaseType="expanded_rerelease"
        ),

        GameInfo(
            "Devil Survivor 2",
            2011,
            series="Devil Survivor",
            subseries=None,
            family="Devil Survivor 2",
            releaseType="original"
        ),

        GameInfo(
            "Devil Survivor 2 Record Breaker",
            2015,
            series="Devil Survivor",
            subseries=None,
            family="Devil Survivor 2",
            releaseType="expanded_rerelease"
        ),

        GameInfo(
            "Majin Tensei",
            1994,
            series="Majin Tensei",
            subseries=None,
            family="Majin Tensei",
            releaseType="original"
        ),

        GameInfo(
            "Majin Tensei II  Spiral Nemesis",
            1995,
            series="Majin Tensei",
            subseries=None,
            family="Majin Tensei II",
            releaseType="original"
        ),

        GameInfo(
            "Ronde",
            1997,
            series="Majin Tensei",
            subseries=None,
            family="Ronde",
            releaseType="original"
        ),
        # Digital Devil Saga
        GameInfo(
            "Digital Devil Saga  Avatar Tuner",
            2004,
            series="Digital Devil Saga",
            subseries=None,
            family="Digital Devil Saga",
            releaseType="original"
        ),

        GameInfo(
            "Digital Devil Saga  Avatar Tuner 2",
            2005,
            series="Digital Devil Saga",
            subseries=None,
            family="Digital Devil Saga 2",
            releaseType="original"
        ),

        # Persona 1
        GameInfo(
            "Megami Ibunroku Persona",
            1996,
            series="Persona",
            subseries=None,
            family="Persona",
            releaseType="original"
        ),


        # Persona 2
        GameInfo(
            "Persona 2  Innocent Sin",
            1999,
            series="Persona",
            subseries="Persona 2",
            family="Persona 2: Innocent Sin",
            releaseType="original"
        ),

        GameInfo(
            "Persona 2  Eternal Punishment",
            2000,
            series="Persona",
            subseries="Persona 2",
            family="Persona 2: Eternal Punishment",
            releaseType="original"
        ),

        # Persona 4
        GameInfo(
            "Persona 4",
            2008,
            series="Persona",
            subseries=None,
            family="Persona 4",
            releaseType="original"
        ),

        GameInfo(
            "Persona 4 Golden",
            2012,
            series="Persona",
            subseries=None,
            family="Persona 4",
            releaseType="expanded_rerelease"
        ),

        # Persona 5
        GameInfo(
            "Persona 5",
            2016,
            series="Persona",
            subseries=None,
            family="Persona 5",
            releaseType="original"
        ),

        GameInfo(
            "Persona 5 Royal",
            2019,
            series="Persona",
            subseries=None,
            family="Persona 5",
            releaseType="expanded_rerelease"
        ),

        # Persona Q
        GameInfo(
            "Persona Q",
            2014,
            series="Persona",
            subseries="Persona Q",
            family="Persona Q",
            releaseType="original"
        ),

        GameInfo(
            "Persona Q2",
            2018,
            series="Persona",
            subseries="Persona Q",
            family="Persona Q2",
            releaseType="original"
        ),

        GameInfo(
            "Megami Tensei",
            1987,
            series= "Mainline",
            subseries = "FC Duo",
            family = "Megami Tensei",
            releaseType = "original"
        ),
        GameInfo(
            "Megami Tensei II",
            1990,
            series = "Mainline",
            subseries = "FC Duo",
            family = "Megami Tensei II",
            releaseType = "original"
        )

    ]
    return games

