import os
import pandas as pd

path = os.path.abspath(os.path.dirname(__file__))
filename = "todo.csv"
oid = pd.read_csv(path + "/todo.csv").iloc[-1,0]

task = input("What's your task?")
dd = input("What's the due date?")

data = {'ID':[oid+1] , 'Task':[task] , 'DD':[dd] , 'Progress':["nd"]}
df = pd.DataFrame(data)
df.to_csv(f'{path}/{filename}', mode='a', index=False, header=False)