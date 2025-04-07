import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data = {
    "title":"This field my old friend"
}

get_response = requests.put(endpoint,json=data) #HTTP request
print(get_response.json())