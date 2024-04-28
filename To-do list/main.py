import os, csv

path = os.path.abspath(os.path.dirname(__file__))

with open(path + "/todo.txt") as file:
    print(file.read())

