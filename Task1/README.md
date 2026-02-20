```markdown
# Task 1 – OOP Student Task Management System

## Description

This system is developed using Object-Oriented Programming (OOP) principles to manage student tasks.

The system supports both normal tasks and priority tasks using inheritance.

---

## Features

- Create Task
- Create Priority Task
- Mark Task as Completed
- Delete Task
- Display Tasks (Sorted by Deadline)
- Automatic Save and Load using JSON

---

## OOP Concepts Used

### 1. Encapsulation
Private attributes are used in the Task class:
- __id
- __name
- __deadline
- __status

Access is controlled using getter methods.

### 2. Inheritance
PriorityTask inherits from Task and extends it by adding priority attribute.

### 3. Polymorphism
The display() method is overridden in PriorityTask.

### 4. Composition
TaskManager manages multiple Task objects.

### 5. Modular Programming
The project is divided into:
- models/
- core/
- main.py

---

## Data Persistence

All tasks are saved to tasks.json using FileHandler.

When the system starts:
- Existing tasks are automatically loaded.

When exiting:
- Tasks are saved automatically.

---

## Sample Interaction

1. Add Normal Task
2. Add Priority Task
3. Mark Task as Completed
4. Delete Task
5. Display All Tasks
6. Save and Exit