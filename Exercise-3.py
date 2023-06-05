import requests
import pytest
import json

def test_get_response_validation_1():
    resp = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert resp.json()['name']=='Leanne Graham',"Name is not matching with expected name"
    assert resp.json()['company']['name']=='Romaguera-Crona',"Company name is not matching with expected company name"
    assert resp.json()['address']['street']=='Kulas Light',"Street name is not matching with expected street name"


def test_get_response_validation_2():
    resp = requests.get("https://jsonplaceholder.typicode.com/users")
    assert resp.json()[1]['name']=="Ervin Howell","First users name is not matching with expected name"
    assert resp.json()[7]['company']['name']=="Abernathy Group","Eigth users company name is not matching with expected comany name"


