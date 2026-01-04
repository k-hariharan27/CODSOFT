tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Task number to update: "))
        tasks[num-1] = input("Enter new task: ")
        print("Task updated.")

    elif choice == "4":
        show_tasks()
        num = int(input("Task number to delete: "))
        tasks.pop(num-1)
        print("Task deleted.")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
