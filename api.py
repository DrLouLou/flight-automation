import requests

url = "https://sky-scanner3.p.rapidapi.com/flights/search-everywhere"

querystring = {"fromEntityId":"NYCA"}

headers = {
	"X-RapidAPI-Key": "0f40cfcaefmsh50da143d39ef59ap10f44ejsnd17e91371aa7",
	"X-RapidAPI-Host": "sky-scanner3.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())