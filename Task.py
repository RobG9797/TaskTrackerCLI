class Task:
    def __init__(self, id:int, task_name:str):
        self.status = 0
        self.id = id
        self.task_name = task_name

    def get_id(self):
        return self.id

    def change_task(self, new_task: str):
        self.task_name == new_task

    def get_status(self):
        return self.status

    def mark_in_progress(self):
        self.status = 1

    def mark_done(self):
        self.status = 2

    def get_name(self):
        return self.task_name