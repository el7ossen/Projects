#!python

import requests, sys, json

response = requests.get("http://localhost:8080/index/subsites/test.txt")

print(response.text)