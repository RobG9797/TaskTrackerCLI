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
        for task in self.task_list:
            if task.get_id() == id:
                task.change_task(new_task)
                return
        print("Error: no task with that ID")

    def delete_task(self, id:int):
        for task in self.task_list:
            if task.get_id() == id:
                self.task_list.remove(task)
                return
        print("Error: no task with that ID")

    def list_done(self):
        done_tasks = []
        for task in self.task_list:
            if task.get_status() == 2:
                done_tasks.append(task)
        print("Completed tasks:")
        for task in done_tasks:
            print(f"ID {task.get_id()}: {task.get_name()}")

    def list_in_progress(self):
        in_progress_tasks = []
        for task in self.task_list:
            if task.get_status() == 1:
                in_progress_tasks.append(task)
        print("In progress tasks:")
        for task in in_progress_tasks:
            print(f"ID {task.get_id()}: {task.get_name()}")

    def list_to_do(self):
        unstarted_tasks = []
        for task in self.task_list:
            if task.get_status() == 0:
                unstarted_tasks.append(task)
        print("To do:")
        for task in unstarted_tasks:
            print(f"ID {task.get_id()}: {task.get_name()}")

    def mark_in_progress(self, id: int):
        for task in self.task_list:
            if task.get_id() == id:
                task.mark_in_progress()
                return
        print("Error: no task with that ID")

    def mark_done(self, id: int):
        for task in self.task_list:
            if task.get_id() == id:
                task.mark_done()
                return
        print("Error: no task with that ID")


    


tracker = TaskTracker()
tracker.add_task("Walk dog")
tracker.update_task(1, "walk cat")
tracker.list_to_do()


    
        
