import pytest
import requests

def test_status_code():
  url = "https://api.pokemonbattle.me/v2/trainers"
  response = requests.get(url)
  assert response.status_code == 200

def test_check_response():
  url = "https://api.pokemonbattle.me/v2/trainers?trainer_id=2289"
  response = requests.get(url)
  assert response.json()["data"][0]["trainer_name"] == "DaRiA"