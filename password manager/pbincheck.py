import requests

res = requests.get("https://pastebin.com/raw/1q2Mv9hn")

check = res.text

print(check)