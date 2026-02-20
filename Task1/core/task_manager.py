class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        self.__tasks.append(task)

    def find_task(self, task_id):
        for task in self.__tasks:
            if task.get_id() == task_id:
                return task
        return None

    def mark_task_completed(self, task_id):
        task = self.find_task(task_id)
        if task:
            task.mark_completed()
            return True
        return False

    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.__tasks.remove(task)
            return True
        return False

    def get_all_tasks(self):
        return self.__tasks