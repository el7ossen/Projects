import pathlib
import pandas as pd

path = pathlib.Path.cwd()
filename = "todo.csv"
filepath = f"{path}/{filename}"
checknd = ['nd']
checkd = ['d']

def dtasks():
    checked = pd.DataFrame(pd.read_csv(filepath))['Progress'].isin(checkd)
    print(pd.DataFrame(pd.read_csv(filepath))[checked])

def ndtasks():
    checked = pd.DataFrame(pd.read_csv(filepath))['Progress'].isin(checknd)
    print(pd.DataFrame(pd.read_csv(filepath))[checked])