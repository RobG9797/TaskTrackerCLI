from Task import Task

class TaskTracker:
    def __init__(self):
        self.task_list = []
        self.count = 1

    def add_task(self, task:str):
        self.task_list.append(Task(self.count, task))
        print(f"Task added successfully (ID: {self.count})")
        self.count += 1
        return 

    def update_task(self, id:int, new_task:str):
        found = 0
        for Task in self.task_list:

        
        if id in self.task_list:
            self.task_list[id] = new_task
            return
        return "Error: no current task with that ID"

    


tracker = TaskTracker()
tracker.add_task("Walk dog")
tracker.update_task(1, "walk cat")


    
        
