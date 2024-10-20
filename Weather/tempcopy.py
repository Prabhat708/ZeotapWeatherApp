import requests

url = "https://visual-crossing-weather.p.rapidapi.com/forecast"
city=input()
 
querystring = {"contentType":"json","unitGroup":"us","aggregateHours":"24","location":city,"shortColumnNames":"false"}

headers = {
	"x-rapidapi-key": "6d4c702e3amsh4ac7e191e51c090p1954c0jsnb0fec7c5a1f7",
	"x-rapidapi-host": "visual-crossing-weather.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())