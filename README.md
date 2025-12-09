# pokemon-api-task
Technical advisory consultant task.

Pycharm was used as the IDE. To run command lines in the pycharm terminal ensure that the correct python interpreter is stated (e.g. 3.11) and then state the script which is being run and the pokemon name. E.g. "C:\Users\hibah\AppData\Local\Programs\Python\Python311\python.exe" 5.py pikachu. Important for tasks 4 & 5.

This repository contains five Python scripts (1.py - 5.py) that implements functionality for interacting with the PokeAPI, extracting Pokemon data, command-line input and using a SQLite database.



1.py - calls the PokeAPI for Clefairy and prints the full JSON response

2.py - extracts `id`, `name`, `height`, and `weight` from the JSON and prints a simplified dictionary

3.py - wraps the logic into a function that accepts a Pokémon name and returns the summary dictionary

4.py - adds command-line argument handling so  user can run `python 4.py pikachu`

5.py - adds SQLite caching, checks the db first, if pokemon isn't found, the script fetches from the API and stores the results

pokemon.db - SQLite db automatically created by `5.py`. Stores cached pokemon data
