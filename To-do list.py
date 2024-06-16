import datetime

# Create an empty list to store the tasks
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append({"task": task, "status": "Pending", "created_at": datetime.datetime.now()})

# Function to mark a task as complete
def mark_complete(task):
    for item in todo_list:
        if item["task"] == task:
            if item["status"] == "Pending":
                item["status"] = "Complete"
                item["completed_at"] = datetime.datetime.now()
                return
            else:
                print("Task is already marked as complete.")
                return
    print("Task not found in the list.")

# Function to delete a task from the list
def delete_task(task):
    for item in todo_list:
        if item["task"] == task:
            todo_list.remove(item)
            return
    print("Task not found in the list.")

# Function to display all tasks in the list
def display_tasks():
    if len(todo_list) == 0:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for item in todo_list:
            print("- Task:", item["task"])
            print("  Status:", item["status"])
            print("  Created at:", item["created_at"])
            if item["status"] == "Complete":
                print("  Completed at:", item["completed_at"])
            print()

# Function to display pending tasks
def display_pending_tasks():
    pending_tasks = [item for item in todo_list if item["status"] == "Pending"]
    if len(pending_tasks) == 0:
        print("No pending tasks.")
    else:
        print("Pending Tasks:")
        for item in pending_tasks:
            print("- Task:", item["task"])
            print("  Created at:", item["created_at"])
            print()

# Function to display overdue tasks
def display_overdue_tasks():
    current_time = datetime.datetime.now()
    overdue_tasks = [item for item in todo_list if item["status"] == "Pending" and item["created_at"] < current_time]
    if len(overdue_tasks) == 0:
        print("No overdue tasks.")
    else:
        print("Overdue Tasks:")
        for item in overdue_tasks:
            print("- Task:", item["task"])
            print("  Created at:", item["created_at"])
            print()

# Main loop
while True:
    print()
    print("---- To-Do List Menu ----")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. Delete Task")
    print("4. Display All Tasks")
    print("5. Display Pending Tasks")
    print("6. Display Overdue Tasks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
        print("Task added successfully!")

    elif choice == "2":
        task = input("Enter task: ")
        mark_complete(task)
        print("Task marked as complete!")

    elif choice == "3":
        task = input("Enter task: ")
        delete_task(task)
        print("Task deleted successfully!")

    elif choice == "4":
        display_tasks()

    elif choice == "5":
        display_pending_tasks()

    elif choice == "6":
        display_overdue_tasks()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
