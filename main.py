""""
def date_isValid(date="15-12"):
    global trueDate
    dash_count=0
    for dash in date:
        if dash == "-":
            dash_count+=1
    if dash_count == 1:
        parts=date.split("-") #[15,12]
        day=int(parts[0])
        month=int(parts[1])
        if month<=12 and month>0:
            if day<=31 and day>0: ##true date
                trueDate=[day,month]
                return  trueDate
            else:
                return 0
        else:
            return 0
    else:
        print("invalid date only allowed format 26-1")
        return 0


def take_due_Date():
    global today
    checkToday=True
    cheskDeadline=True
    while checkToday == True:

        today = input("what is the date[day-month]: ")
        if date_isValid(today)!=0:
            today=date_isValid(today)
            checkToday = False
        else:
            print("Try Again")

    while cheskDeadline == True:
        deadline=input("DEADLine DATE: ")
        if date_isValid(deadline)==trueDate :
            deadline=date_isValid(deadline)
            cheskDeadline =False
        else:
            print("Try Again")


    if deadline[1] >= today[1]:
        if deadline[0] > today[0]:
            daysLeft = deadline[0]-today[0]
            print("you have " + str(daysLeft)+" days")
        elif deadline[0] == today[0]:
            print("deadline is today")
        else:
            print("missed")

    else:
        print("missed")

"""
"""""
task=(title, description , dueDate , status="incomplete")
workTask=(title, description, dueDate, status="incomplete", priority="low"):
personalTask=(title , description , dueDate , status="incomplete",category="general")
"""""


from Task import task
from PersonalTask import personalTask
from WorkTask import workTask
from TaskManager import taskManager

from rich.console import Console
from rich.table import Table
import json
""""
console = Console()
table = Table(title="HELLO USER")


table.add_column("n")
table.add_column("task")
table.add_column("dis")
table.add_column("DeadLine")
console.print(table)
"""
#a=taskManager()
#a.add_user("rehab","2612")
#a.delete_user(9)
#a.add_user("sara",1200)
#a.show_all_users()
#a.login(1,"123")
#a.add_personal_task(1,"p task","this 1st p task","12-1","health")
#a.add_work_task(1,"p task","this p task","12-1","low")

