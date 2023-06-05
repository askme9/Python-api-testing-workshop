import requests
import pytest
import json

def test_get_response_status_200():
    resp = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert resp.status_code==200,"Expected status code is 200"

# when the user not found, we get 404 error
def test_get_response_satus_404():
    resp = requests.get("https://jsonplaceholder.typicode.com/users/999")
    assert resp.status_code==404,"Expected status code is 404"

def test_header_content_type():
    resp = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert resp.headers['Content-Type']=='application/json; charset=utf-8',"expected Content-Type is not matching"

def test_post_response_status_201():
    payload = {
        "userId":1,
        "title":"Here goes the post title",
        "body":"Here goes the post body",
    }
    resp = requests.post("https://jsonplaceholder.typicode.com/posts",data=payload)
    assert resp.status_code==201,"Expected status code is 201"


