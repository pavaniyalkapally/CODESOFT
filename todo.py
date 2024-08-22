import json
import os

TASKS_FILE = 'tasks.json'
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': 'pending'
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} - {task['status']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}\n")

def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    task_num = int(input("Enter task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        title = input("Enter new title (leave blank to keep current): ")
        description = input("Enter new description (leave blank to keep current): ")
        due_date = input("Enter new due date (leave blank to keep current): ")

        if title:
            tasks[task_num]['title'] = title
        if description:
            tasks[task_num]['description'] = description
        if due_date:
            tasks[task_num]['due_date'] = due_date

        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def mark_as_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    task_num = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['status'] = 'completed'
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    task_num = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            mark_as_completed(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
