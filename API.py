import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"bijelo dugme"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "ce1b109651mshe72a7ebf8d04b6dp17f04djsn9e412655e61b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)