tasks = []


def view_tasks():

    if len(tasks) <= 0:
        print("There are no tasks in your to do list.")
    else:
        print("\n-----TO DO LIST-----")
        for i, task in enumerate(tasks, start=1):
            print(f"{i} : {task}")

    option = input("\nPress 'M' to go back: ")
    if option.lower() == "m":
        menu()


def add_task():

    task = input("Enter new tasks: ")
    if task not in tasks:
        tasks.append(task)
        print("Task added")
    else:
        print("Task already exists!")

    option = input("\nPress 'A' to add another task or press 'M' to go back: ")
    if option.lower() == "a":
        add_task()
    elif option.lower() == "m":
        menu()


def remove_task():

    for i, task in enumerate(tasks, start=1):
        print(f"{i} : {task}")

    if len(tasks) != 0:
        while True:
            try:
                choice = int(input("Which task do you want to remove?: "))
                if 0 < choice <= len(tasks):
                    tasks.pop(choice - 1)
                    print("Task removed")
                    break
                else:
                    print("Task does not exist!")
                    break
            except ValueError:
                print(f"ERROR! Enter a valid!")
    else:
        print("There is nothing to remove!")

    choice = input("\nPress 'M' to go back: ")
    if choice.lower() == "m":
        menu()


def menu():

    print("\n-----OPTIONS-----")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Remove a task")

    try:
        option = int(input("\nEnter any option: "))

        if option == 1:
            view_tasks()
        elif option == 2:
            add_task()
        elif option == 3:
            remove_task()
        else:
            print("\nEnter a valid option!\n")
            menu()
    except ValueError:
        menu()


menu()
