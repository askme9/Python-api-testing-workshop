# create a data set
import pytest
import requests

data_set = [
    ('us',90210,'Beverly Hills'),
    ('it',50123,'Firenze'),
    ('ca','B2A','North Sydney South Central')
]

# add the parameterize marker in pytest

@pytest.mark.parametrize('country_code,zip_code,expected_place',data_set)
def test_for_place_name(country_code,zip_code,expected_place):
    response = requests.get(f"https://api.zippopotam.us/{country_code}/{zip_code}")
    body = response.json()
    assert body['places'][0]['place name'] == expected_place
