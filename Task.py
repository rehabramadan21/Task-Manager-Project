class task() :
    def __init__(self , title , description , dueDate , status="incomplete"):
        self.__title = title
        self.__description = description
        self.__dueDate = dueDate
        if status == "incomplete" or status == "in_progress" or status == "completed":
            self.__status = status
        else:
            print("invalid")


    def set_title(self , title):
        self.__title = title
    def get_title(self):
        print("title: " + self.__title)

    def set_description(self , description):
        self.__description = description
    def get_description(self):
        print("description: " + self.__description)

    def set_dueDate(self , dueDate):
        self.__dueDate = dueDate
    def get_dueDate(self):
        print("dueDate: " + self.__dueDate)

    def set_status(self , status):

        if status == "incomplete" or status == "in_progress" or status == "completed":
            self.__status = status
        else:
            print("invalid")
    def get_status(self):
        print("status: " + self.__status)

    def mark_completed(self):
        self.__status = "completed"
        print("THE TASK MARKED COMPLETED ")
    def display(self):
        print("title: " + self.__title)
        print("description: " + self.__description)
        print("dueDate: " + self.__dueDate)
        print("status: " + self.__status)

    #####################هنشوف لو محتاجناهاش نمسحها ####################
    def As_a_dictionry(self):
        return {
        "title": self.__title,
        "description": self.__description,
        "dueDate": self.__dueDate,
        "status": self.__status
        }

