import requests

url = "https://api.pokemonbattle.me"

headers = {
    "Content-Type" : "application/json",
    "trainer_token" : "8e17725393834c9f4eecf6d950e5a419"
}

body = {
  "name": "Doras pokemon",
  "photo": "https://dolnikov.ru/pokemons/albums/016.png"
}

response = requests.post(url = f"{url}/v2/pokemons", json = body, headers=headers)
print(response.text)

body = {
  "pokemon_id": "15524",
  "name": "New Name",
  "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.put(url = f"{url}/v2/pokemons", json = body, headers=headers)
print(response.text)

body = {
  "pokemon_id": "15524"
}

response = requests.post(url = f"{url}/v2/trainers/add_pokeball", json = body, headers=headers)
print(response.text)