# pokemon-api-task
Technical advisory consultant task.
This repository contains five Python scripts (1.py - 5.py) that implements functionality for interacting with the PokeAPI, extracting Pokemon data, command-line input and using a SQLite database.
The final script (5.py) includes complete caching logic so that each Pokemon is only fetched from the API once. All other runs will load the Pokémon directly from the local SQLite database (pokemon.db).


1.py - calls the PokeAPI for Clefairy and prints the full JSON response

2.py - extracts `id`, `name`, `height`, and `weight` from the JSON and prints a simplified dictionary

3.py - wraps the logic into a function that accepts a Pokémon name and returns the summary dictionary

4.py - adds command-line argument handling so  user can run `python 4.py pikachu`

5.py - adds SQLite caching, checks the db first, if pokemon isn't found, the script fetches from the API and stores the results
pokemon.db - SQLite db automatically created by `5.py`. Stores cached pokemon data
