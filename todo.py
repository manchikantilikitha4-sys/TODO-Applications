tasks = []

# Load existing tasks
try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "3":
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
        else:
            print("Invalid task number")

    elif choice == "4":
        break

    else:
        print("Invalid choice")

    # Save tasks to file
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
            while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        new_task = input("Enter task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == "3":
        try:
            task_num = int(input("Enter task number to remove: "))
            tasks.pop(task_num - 1)
            print("Task removed!")
        except (ValueError, IndexError):
            print("Invalid task number.")

    elif choice == "4":
        # Bonus: Save tasks to file before exiting
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, please try again.")
        