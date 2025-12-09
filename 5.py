import requests
import json
import sys
import sqlite3
from pathlib import Path

# put database in the same folder as this script
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "pokemon.db"

# setting up database table
def init_db():
    """Create the SQLite database and table if they don't already exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            height INTEGER NOT NULL,
            weight INTEGER NOT NULL
        );
        """
    )

    conn.commit()
    conn.close()

# query the databse with select and where to create a summary dictionary
def get_pokemon_from_db(pokemon_name):
    """Attempt to fetch a pokemon's summary from local database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, height, weight FROM pokemon WHERE name = ?",
        (pokemon_name.lower(),),
    )
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    id_, name, height, weight = row
    return {
        "id": id_,
        "name": name,
        "height": height,
        "weight": weight,
    }


# if it isn't in the database use the API to build the dict and save to the database
def get_pokemon_from_api(pokemon_name):
    """Get pokemon data from PokeAPI and return summary dictionary."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    summary = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
    }

    return summary

def save_pokemon_to_db(summary):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT OR REPLACE INTO pokemon (id, name, height, weight)
        VALUES (?, ?, ?, ?)
        """,
        (summary["id"], summary["name"].lower(), summary["height"], summary["weight"]),
    )
    conn.commit()
    conn.close()

# used so api isn't called more times than needed
def get_pokemon_summary(pokemon_name):
    """
    Main function to get pokemon summary.
    1. check SQLite cache.
    2. if not found, call API and store result in cache.
    """

    # 1. Try the database first
    cached = get_pokemon_from_db(pokemon_name)
    if cached is not None:
        # Optional: you could log that this came from cache
        return cached

    # 2. Fallback to API if not in DB
    summary = get_pokemon_from_api(pokemon_name)
    # 3. Save to DB for next time
    save_pokemon_to_db(summary)
    return summary


if __name__ == "__main__":
    # Ensure DB and table exist
    init_db()

    if len(sys.argv) < 2:
        print("Usage: python 4.py <pokemon_name>")
        sys.exit(1)

    pokemon_name = sys.argv[1]

    result = get_pokemon_summary(pokemon_name)

    print("\nPokémon Summary")
    print("-" * 20)
    print(json.dumps(result, indent=4))

### to run for any pokemon in windows powershell go to the project folder this is saved in
### then run 5.py with the same Python version that used 3.11, plus a pokemon name
### e.g. cd "C:\Users\hibah\OneDrive - CP Media\test"
###      & "C:\Users\hibah\AppData\Local\Programs\Python\Python311\python.exe" 5.py pikachu

### or if running in pycharm terminal explicity sated which python interpreter to use + pokemon name
### e.g & "C:\Users\hibah\AppData\Local\Programs\Python\Python311\python.exe" 4.py pikachu