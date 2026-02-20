class Task:
    def __init__(self, task_id, name, deadline):
        self.__id = task_id
        self.__name = name
        self.__deadline = deadline
        self.__status = "未完成"

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_deadline(self):
        return self.__deadline

    def get_status(self):
        return self.__status

    def mark_completed(self):
        self.__status = "已完成"

    def display(self):
        return f"{self.__id} | {self.__name} | {self.__status} | {self.__deadline}"