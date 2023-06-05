import requests
import pytest

data_set = {
    (1,'Leanne Graham','Romaguera-Crona'),
    (2,'Ervin Howell','Deckow-Crist'),
    (3,'Clementine Bauch','Romaguera-Jacobson'),
    (9,'Glenna Reichert','Yost and Sons')
}

@pytest.mark.parametrize('user_id,name,company_name',data_set)
def test_user_name_and_company_name(user_id,name,company_name):
    resp = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert resp.json()['name']== name
    assert resp.json()['company']['name']==company_name
