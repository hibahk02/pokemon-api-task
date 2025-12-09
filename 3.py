import requests
import json

# using a function so the logic stays reusable and testable
def pokemon_summary(pokemon_name):
    """
    Fetch a Pokémon by name and return a summary dictionary
    containing only: id, name, height, weight.
    """

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}" # convert the input so users may used mixed case sensitivity
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
    pokemon = "weedle"
    result = pokemon_summary(pokemon)

    # prints the output in a better format
    print("\nPokémon Summary\n" + "-" * 20)
    print(json.dumps(result, indent=4))
