import requests
import json

resp = requests.get("https://www.zippopotam.us/us/90210")
# to print the response status code
print(f"response status code is {resp.status_code}")

# headers property is simply a python dictionary that contain the all of the headers assoiciated with response
print(f"response headres are {resp.headers}")
# we use content property, to print the response body
print(f"response content is {resp.content}")
# pretty print the json response body
print(f"response body is {json.dumps(resp.json(),indent=4)}")


