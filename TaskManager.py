import json
from NewUser import newUser
from Task import task
from PersonalTask import personalTask
from WorkTask import workTask

class taskManager:
    def __init__(self, filename="Data.json"):
        self.filename=filename
        self.users=[]
        try:
            file = open(self.filename, "r")
            self.users = json.load(file)
            file.close()
        except FileNotFoundError:
            self.users = []

    def save_json(self):
        file = open(self.filename, "w")
        json.dump(self.users, file, indent=2)
        file.close()

    def add_user(self,name="unknown",password="0000"):
        id_count=0
        for i in self.users:
            if i["id"]>id_count:
                id_count=i["id"]
        if name.isalpha():
            id_count+=1
            add_new_user=newUser(name,password,id_count)
            self.users.append(add_new_user.Person_As_dictionry())
            self.save_json()
            print(name+" added successfully with ID: "+str(id_count))
        else:
            print("this name isn't available, name should contains only letter ")

    def delete_user(self, user_id):
        for i in self.users:
            if i["id"]==user_id :
                confirm=input("you want to delete account [1]yes [2] no ?")
                if confirm=="1":
                    self.users.remove(i)
                    self.save_json()
                    print(f"User ID {user_id} deleted successfully")
                elif confirm=="2":
                    print("Deleting canceled")
                else:
                    print("invalid input")
                break
        else:
            print("User not found")


    def show_all_users(self):
        for i in self.users:
            print("name: "+i["name"] +" , ID: "+str(i["id"]))

    def login(self, user_id, password):
        for i in self.users:
            if i["id"]==user_id:
                if i["password"]==password:
                    print("************Welcome back, "+i["name"]+"************")
                    break
                else:
                    print("Invalid Password")
                    break
            else:
                print("Invalid ID")


    ##########################
    def add_personal_task(self, user_id, title, description, dueDate, category="general"):
        for i in self.users:
            if i["id"] == user_id:
                new_task = personalTask(title, description, dueDate, category)
                i["tasks"]["personal"].append(new_task.As_a_dictionary())
                self.save_json()
                print("Personal task"+title+ "added")
                return
        print("User not found")

    def add_work_task(self, user_id, title, description, dueDate, priority="low"):
        for i in self.users:
            if i["id"] == user_id:
                new_task = workTask(title, description, dueDate, priority)
                i["tasks"]["work"].append(new_task.As_a_dictionary())
                self.save_json()
                print("Work task "+title+" added")
                return
        print("User not found")


