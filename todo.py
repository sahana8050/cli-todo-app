import os

FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        tasks = file.readlines()
    
    return [task.strip() for task in tasks]


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Show tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!\n")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


# Add task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed}\n")
        
    except (ValueError, IndexError):
        print("Invalid task number!\n")


def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO LIST ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()