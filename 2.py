import requests

def clefairy_data():
    url = "https://pokeapi.co/api/v2/pokemon/clefairy"
    response = requests.get(url)

    # raise error if request fails
    response.raise_for_status()

    # convert API JSON response into python dictionary
    data = response.json()

    # dictionary
    poke_dictionary = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }

    print(poke_dictionary)

if __name__ == "__main__":
    clefairy_data()