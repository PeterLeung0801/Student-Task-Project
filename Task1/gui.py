import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from models.task import Task
from models.priority_task import PriorityTask
from core.task_manager import TaskManager
from core.file_handler import FileHandler

FILE_NAME = "tasks.json"

manager = TaskManager()
file_handler = FileHandler(FILE_NAME)

for task in file_handler.load():
    manager.add_task(task)

def refresh_list():
    listbox.delete(0, tk.END)
    tasks = sorted(
        manager.get_all_tasks(),
        key=lambda t: datetime.strptime(t.get_deadline(), "%Y-%m-%d")
    )
    for task in tasks:
        listbox.insert(tk.END, task.display())

def add_task():
    tid = entry_id.get()
    name = entry_name.get()
    deadline = entry_deadline.get()
    priority = entry_priority.get()

    if manager.find_task(tid):
        messagebox.showerror("Error", "ID already exists!")
        return

    if priority:
        task = PriorityTask(tid, name, deadline, priority)
    else:
        task = Task(tid, name, deadline)

    manager.add_task(task)
    refresh_list()

def mark_completed():
    selection = listbox.curselection()
    if not selection:
        return
    task_text = listbox.get(selection[0])
    tid = task_text.split("|")[0].replace("🔥", "").strip()
    manager.mark_task_completed(tid)
    refresh_list()

def delete_task():
    selection = listbox.curselection()
    if not selection:
        return
    task_text = listbox.get(selection[0])
    tid = task_text.split("|")[0].replace("🔥", "").strip()
    manager.delete_task(tid)
    refresh_list()

def save_tasks():
    file_handler.save(manager.get_all_tasks())
    messagebox.showinfo("Saved", "Tasks saved successfully!")

root = tk.Tk()
root.title("Student Task Management System")

tk.Label(root, text="Task ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Task Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Deadline (YYYY-MM-DD)").pack()
entry_deadline = tk.Entry(root)
entry_deadline.pack()

tk.Label(root, text="Priority (Optional)").pack()
entry_priority = tk.Entry(root)
entry_priority.pack()

tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Mark Completed", command=mark_completed).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()
tk.Button(root, text="Save", command=save_tasks).pack()

listbox = tk.Listbox(root, width=80)
listbox.pack()

refresh_list()

root.mainloop()