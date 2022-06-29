import requests
api_url = "http://localhost:9090/display"
response = requests.get(api_url)
print(response.text)