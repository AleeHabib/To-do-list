def menu():

    print("\n-----OPTIONS-----")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Remove a task")

    try:
        option = int(input("\nEnter any option: "))

        if option == 1:
            # view_tasks()
            pass
        elif option == 2:
            # add_task()
            pass
            pass
        elif option == 3:
            # remove_task()
            pass
        else:
            print("\nEnter a valid option!\n")
            menu()
    except ValueError:
        menu()


menu()
