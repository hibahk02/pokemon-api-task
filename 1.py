import requests # the standard library for making http calls in python

# function used so that it is organised and repeatable
def clefairy_data():
    url = "https://pokeapi.co/api/v2/pokemon/clefairy" # storing API endpoint as a variable
    response = requests.get(url) # send a GET request to endpoint. This gives a response with data

    # raise error if API returns an error
    response.raise_for_status()

    # API returns JSON format - this converts into python dictionary
    data = response.json()
    print(data)

# only runs code when the script is run directly
if __name__ == "__main__":
    clefairy_data()