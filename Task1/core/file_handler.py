import json
from models.task import Task
from models.priority_task import PriorityTask

class FileHandler:
    def __init__(self, filename):
        self.__filename = filename

    def save(self, tasks):
        data = []
        for task in tasks:
            task_data = {
                "id": task.get_id(),
                "name": task.get_name(),
                "deadline": task.get_deadline(),
                "status": task.get_status(),
                "type": task.__class__.__name__
            }
            if isinstance(task, PriorityTask):
                task_data["priority"] = task.get_priority()
            data.append(task_data)

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load(self):
        tasks = []
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            for item in data:
                if item["type"] == "PriorityTask":
                    task = PriorityTask(
                        item["id"],
                        item["name"],
                        item["deadline"],
                        item.get("priority", "Normal")
                    )
                else:
                    task = Task(
                        item["id"],
                        item["name"],
                        item["deadline"]
                    )

                if item["status"] == "已完成":
                    task.mark_completed()

                tasks.append(task)

        except FileNotFoundError:
            pass

        return tasks