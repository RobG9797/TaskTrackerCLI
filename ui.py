class Ui:
    def __init__(self, tasktracker: TaskTracker):
        self.tasktracker = tasktracker

    def start(self):
        print("Welcome!")
        self.menu()
        user_response = input()
        strings = user_response.split(" ", 1)
        
        if strings[0] == "add":
            if len(strings > 1):
                self.tasktracker.add_task(strings[1])
            else:
                print("Error: please type something to add")



    def menu(self):
        print("Type: add '[the task name]' to add tasks")
        print("Type ....")
        print("Type ....")
        print("Type menu to see this menu again!")