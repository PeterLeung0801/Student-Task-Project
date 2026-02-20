from models.task import Task
from models.priority_task import PriorityTask
from core.task_manager import TaskManager
from core.file_handler import FileHandler
from datetime import datetime

def main():
    FILE_NAME = "tasks.json"
    file_handler = FileHandler(FILE_NAME)
    manager = TaskManager()

    loaded_tasks = file_handler.load()
    for task in loaded_tasks:
        manager.add_task(task)

    while True:
        print("\n=== Student Task Management System ===")
        print("1. Add Normal Task")
        print("2. Add Priority Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Display All Tasks (sorted by deadline)")
        print("6. Save and Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            tid = input("Enter task ID: ").strip()
            if manager.find_task(tid):
                print("Error: ID already exists!")
                continue
            name = input("Enter task name: ").strip()
            deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
            task = Task(tid, name, deadline)
            manager.add_task(task)
            print("Normal task added successfully!")

        elif choice == "2":
            tid = input("Enter task ID: ").strip()
            if manager.find_task(tid):
                print("Error: ID already exists!")
                continue
            name = input("Enter task name: ").strip()
            deadline = input("Enter deadline (YYYY-MM-DD): ").strip()
            priority = input("Enter priority (High/Medium/Low/Normal): ").strip() or "Normal"
            task = PriorityTask(tid, name, deadline, priority)
            manager.add_task(task)
            print("Priority task added successfully!")

        elif choice == "3":
            tid = input("Enter task ID to mark completed: ").strip()
            if manager.mark_task_completed(tid):
                print("Task marked as completed!")
            else:
                print("Task not found!")

        elif choice == "4":
            tid = input("Enter task ID to delete: ").strip()
            if manager.delete_task(tid):
                print("Task deleted!")
            else:
                print("Task not found!")

        elif choice == "5":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks yet!")
                continue

            sorted_tasks = sorted(
                tasks,
                key=lambda t: datetime.strptime(t.get_deadline(), "%Y-%m-%d")
            )

            print("\n=== All Tasks ===")
            for task in sorted_tasks:
                print(task.display())

        elif choice == "6":
            file_handler.save(manager.get_all_tasks())
            print("All tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()