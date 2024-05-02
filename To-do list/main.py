import pathlib
import pandas as pd

path = pathlib.Path.cwd()
filename = "todo.csv"
filepath = f"{path}/{filename}"
checknd = ['nd']
checkd = ['d']
df = pd.read_csv(filepath)

def newtask():
    task = input("What's your task?")
    dd = input("What's the due date?")
    data = {'Task':[task] , 'DD':[dd] , 'Progress':["nd"]}
    df = pd.DataFrame(data)
    df.to_csv(filepath, mode='a', index=False, header=False)

def readtask():
    df = pd.read_csv(filepath)
    print(df.shape[0])

def dtasks():
    checked = pd.DataFrame(pd.read_csv(filepath))['Progress'].isin(checkd)
    print(pd.DataFrame(pd.read_csv(filename))[checked])

def ndtasks():
    checked = pd.DataFrame(pd.read_csv(filepath))['Progress'].isin(checknd)
    print(pd.DataFrame(pd.read_csv(filename))[checked])
    return checked

def dotask():
    ndtasks()
    while True:
        op = str(input("\nwhich task would you like to do? "))

dotask()