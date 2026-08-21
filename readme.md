Why?

Needed a project, this seemed interesting, I wanted to figure out if there were major extinction events in the series.


This is a very scattered dataset, so there are a few things to note about my data sanitation, in no particular order.

Persona 2 IS and EP have separate wiki pages for demons and personas. I squashed those into one for each game, so Persona 2: Innocent Sin has a large appearance list without differentiation between demons and Personas, and Persona 2: Eternal Punishment has the same. I wasn't interested in splitting the dataset there, and my database schema wouldn't really support it. 

Innate Personas and similar for DDS are assigned a level of 1. Evolved Personas are also assigned a level of 1 as they have no defined base level in the compendium. This was an editorial choice: I had to have a level so that sorting would work, and I made the executive decision to pick 1.

I have games sorted by rerelease and game family. Persona 3 has been released at least four times, and creating a "Persona 3" category allows us to access unskewed data without letting Persona 3 stuff the ballot box. I did rereleases by bestiary change, except Nocturne, which techinically has a bestiary change between vanilla and MANIAX, and then swaps out Dante for Raidou in Chronicles, before the HD remaster returns both. There's enough weirdness there that it deserved to be expanded.

SMT I on the other hand seems to have only one bestiary expansion on the Sega CD, so there are two versions of it in the database. Likewise with SMT II.