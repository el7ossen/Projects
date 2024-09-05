from pathlib import Path
import pandas as pd


#constants
path = Path.cwd()
filepath = f"{path}/todo.csv"
checknd = ['nd']
checkd = ['d']
df = pd.read_csv(filepath)
Desc = "None"
#---------- 

#Functions
def newtask():
    task = input("What's your task? ")
    dd = input("What's the due date? ")
    Desc = input("Describtion? ")
    data = {'Task':[task] , 'DD':[dd] , 'Progress':["nd"] , 'Desc':[Desc]}
    df = pd.DataFrame(data)
    df.to_csv(filepath, mode='a', index=False, header=False)
def readtask():
    print(df.shape[0])
def dtask():
    checked = pd.DataFrame(df)['Progress'].isin(checkd)
    print(pd.DataFrame(pd.read_csv(filepath))[checked])
def ndtask():
    checked = pd.DataFrame(df)['Progress'].isin(checknd)
    ndf = pd.DataFrame(pd.read_csv(filepath))[checked]
    print(ndf.to_markdown(tablefmt="pretty", stralign="left", index=None))
def dotask():
    ndtask()
    while True:
        op = int(input("\nwhich task would you like to do? ")) - 1
        try:
            opdf = df.iloc[[op]]
        except:
            print("That's not an option!")
            continue
        df.loc[op, 'Progress'] = "d"
        df.to_csv(filepath, index=False)
        print("Done.")
        break
#----------

#Program

print("Hello Hussain, what do you want to do?")
option= input("\n 1. Create new task\n 2. Do a task\n 3. View your uncompleted tasks\n 4. View completed tasks\n 5. View all tasks\n\noption: ")

if option == "1":
    newtask()
elif option == "2":
    dotask()
elif option == "3":
    ndtask()
elif option == "4":
    dtask()
elif option == "5":
    readtask()