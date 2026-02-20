from models.task import Task

class PriorityTask(Task):
    def __init__(self, task_id, name, deadline, priority="Normal"):
        super().__init__(task_id, name, deadline)
        self.__priority = priority

    def get_priority(self):
        return self.__priority

    def display(self):
        return f"🔥 {self.get_id()} | {self.get_name()} | {self.get_status()} | {self.get_deadline()} | Priority: {self.__priority}"