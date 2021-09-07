import requests

url = "https://api.ihansen.org/img/detail?page=0&perPage=9&index&orderBy=likes&favorites&tag=night"

payload={}
headers = {
  'Cookie': 'userid=7b3d3d90a473456ebac473c28ce1d1e3'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)