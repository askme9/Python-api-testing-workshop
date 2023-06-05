import requests

def test_for_place_name():
    response = requests.get("https://api.zippopotam.us/us/90210")
    body = response.json()
    assert body['places'][0]['place name']=='Beverly Hills'

def test_for_another_place():
    response = requests.get("https://api.zippopotam.us/it/50123")
    body = response.json()
    assert body['places'][0]['place name']=="Firenze"

def test_for_third_place_name():
    response = requests.get("https://api.zippopotam.us/ca/B2A")
    body = response.json()
    assert body['places'][0]['place name']=='North Sydney South Central'

