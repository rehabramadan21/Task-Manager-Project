from Task import task
class personalTask(task):
    def __init__(self, title , description , dueDate , status="incomplete",category="general"):
        super(personalTask, self).__init__(title , description , dueDate , status="incomplete")
        self.__category=category

    def set_category(self,category="general"):
        self.__category=category
    def get_category(self):
        return self.__category
    def get_type(self):
        print("Personal Task")
    def display(self):
        super().display()
        print("Category: "+ self.__category)

    def As_a_dictionary(self):
        personal_dictionary=super().As_a_dictionary()
        personal_dictionary["category"] = self.__category
        return personal_dictionary

