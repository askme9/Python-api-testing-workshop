import requests

# Exercise-1.1
# Perform Get request to http://api.zippopotam.us/us/90210
# Check that the response status code equals 200
def test_status_code_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code==200,"Expected status code is 200"

# Exercise 1.2
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the value of the response header 'Content-Type' equals 'application/json'
def test_header_content_type():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_headers = response.headers
    assert response_headers['Content-Type']=='application/json',"response header 'Content-Type' is not equals to 'application/json'"

# Exercise 1.3
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'country' has a value equal to 'United States'
def test_response_body_country():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body['country']=='United States',"response body element 'country' is not equal to 'United States'"

# Exercise 1.4
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the first 'place name' element in the list of places
# has a value equal to 'Beverly Hills'
def test_response_place_name():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body['places'][0]['place name']=='Beverly Hills',"place name value is not equal to 'Beverly Hills'"

# Exercise 1.5
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'places' has an array
# value with a length of 1 (i.e., there's one place that corresponds
# to the US zip code 90210)
def test_response_places():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    print(type(response_body['places']))
    print(len(response_body['places']))

