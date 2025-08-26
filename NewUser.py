class newUser:
    def __init__(self,name="unknown",password="0000",id=0):
        self.__name=name
        self.__password=password
        self.__id=id

    def set_pass(self, newPassword,currentPassword):
        if currentPassword == self.__password :
            self.__password=newPassword
        else:
            print("you can't change password without enter your current password correctly")

    def get_name(self):
        return self.__name
    def get_password(self):
        return self.__password
    def get_id(self):
        return self.__id
    def dispalyUser(self):
        print("name : " +str(self.__name))
        print("ID: "+str(self.__id))
        print("password: "+str(self.__password))
    def Person_As_dictionry(self):
        return {
            "name": self.__name,
            "id":self.__id,
            "password":self.__password,
            "tasks":{
                "personal":[],
                "work":[]
            }
        }
