import tkinter as tk
from tkinter import ttk, messagebox
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

# ----------------- UI -----------------

root = tk.Tk()
root.title("Student Task Management System")
root.geometry("750x500")
root.configure(bg="#f5f5f5")

title = tk.Label(root, text="Student Task Management System",
                 font=("Arial", 18, "bold"), bg="#f5f5f5")
title.pack(pady=15)

main_frame = ttk.Frame(root, padding=15)
main_frame.pack(fill="both", expand=True)

# Input Section
input_frame = ttk.LabelFrame(main_frame, text="Add New Task", padding=10)
input_frame.grid(row=0, column=0, sticky="ew", pady=10)

ttk.Label(input_frame, text="Task ID").grid(row=0, column=0, padx=5, pady=5)
entry_id = ttk.Entry(input_frame)
entry_id.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Task Name").grid(row=1, column=0, padx=5, pady=5)
entry_name = ttk.Entry(input_frame, width=30)
entry_name.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Deadline (YYYY-MM-DD)").grid(row=2, column=0, padx=5, pady=5)
entry_deadline = ttk.Entry(input_frame)
entry_deadline.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Priority (Optional)").grid(row=3, column=0, padx=5, pady=5)
entry_priority = ttk.Entry(input_frame)
entry_priority.grid(row=3, column=1, padx=5, pady=5)

ttk.Button(input_frame, text="Add Task", command=add_task)\
    .grid(row=4, column=0, columnspan=2, pady=10)

# Task List Section
list_frame = ttk.LabelFrame(main_frame, text="Task List", padding=10)
list_frame.grid(row=1, column=0, sticky="nsew")

listbox = tk.Listbox(list_frame, width=90, height=10)
listbox.pack(pady=5)

button_frame = ttk.Frame(list_frame)
button_frame.pack(pady=5)

ttk.Button(button_frame, text="Mark Completed", command=mark_completed)\
    .grid(row=0, column=0, padx=5)

ttk.Button(button_frame, text="Delete Task", command=delete_task)\
    .grid(row=0, column=1, padx=5)

ttk.Button(button_frame, text="Save Tasks", command=save_tasks)\
    .grid(row=0, column=2, padx=5)

refresh_list()
root.mainloop()