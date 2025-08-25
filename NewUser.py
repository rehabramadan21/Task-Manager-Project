class newUser:
    def __init__(self,name="unknown",password="0000",id=0):
        if name.isalpha():
            self.__name=name
            self.__password=password
            self.__id=id
        else: print("this name unavaliable")

    def set_name(self,newName="unknown"):
        if newName.isalpha():
            self.__name=newName
        else: print("this name unavaliable")
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