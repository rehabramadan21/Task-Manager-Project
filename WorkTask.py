from Task import task
class workTask(task):
    def __init__(self, title, description, dueDate, status="incomplete", priority="low"):
        super().__init__(title, description, dueDate, status)

        if priority == "low" or priority == "medium" or priority == "high":
            self.__priority = priority
        else:
            print("invalid priority")

    def set_priority(self, priority):
        if priority == "low" or priority == "medium" or priority == "high":
            self.__priority = priority
        else:
            print("invalid priority")

    def get_priority(self):
        print("priority: " + self.__priority)

    def get_task_type(self):
        print("This is a work task")

    def display(self):
        super().display()
        print("priority: " + self.__priority)
        #######################
    def As_a_dictionry(self):
        prio_dict = super().As_a_dictionry()
        prio_dict["priority"] = self.__priority
        prio_dict["type"] = "work"
        return prio_dict

