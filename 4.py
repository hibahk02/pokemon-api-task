import requests
import json
import sys   # read command line arguments

def pokemon_summary(pokemon_name):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    # dictionary
    summary = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }

    return summary


if __name__ == "__main__":
    # checks if the user has passed an argument
    if len(sys.argv) < 2:
        print("Usage: python 4.py <pokemon_name>")
        sys.exit(1)

    # reads anything the user has typed after the script name
    pokemon_name = sys.argv[1]

    # calls earlier function and passes the users argument
    result = pokemon_summary(pokemon_name)

    # prints result
    print(json.dumps(result, indent=4))

### to run for any pokemon in windows powershell go to the project folder this is saved in
### then run 4.py with the same Python version that used 3.11, plus a pokemon name
### e.g. cd "C:\Users\hibah\OneDrive - CP Media\test"
###      & "C:\Users\hibah\AppData\Local\Programs\Python\Python311\python.exe" 4.py pikachu

### or if running in pycharm terminal explicity sated which python interpreter to use + pokemon name
### e.g & "C:\Users\hibah\AppData\Local\Programs\Python\Python311\python.exe" 4.py pikachu
