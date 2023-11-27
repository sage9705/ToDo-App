#Terminal based to-do application
#v1.0
#Auhor: Edem Godwin Kumahor

tasks = []
completed_tasks = []
uncompleted_tasks = []

while True:
    print("+++++++++++++++++++++++++++++++")
    print("++        To-Do Menu:        ++")
    print("++                           ++")
    print("++ 1. Add Task               ++")
    print("++ 2. Mark Task as Complete  ++")
    print("++ 3. View Tasks             ++")
    print("++ 4. Remove Completed Tasks ++")
    print("++ 5. Exit                   ++")
    print("+++++++++++++++++++++++++++++++")

    choice = input("\nEnter option (1-5): \n")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "complete": False})
        uncompleted_tasks.append({"task": task, "complete": False})
        print("Task added successfully!\n\n")

    elif choice == "2":
        if not tasks:
            print("No tasks to mark as complete")
            continue

        try:
            index_input = input("Enter the task index(number assigned to task) to mark as complete: ")
            if index_input.isdigit():
                task_index = int(index_input) - 1

            if 0 <= task_index < len(tasks):
                tasks[task_index]["complete"] = True
                completed_tasks.append(tasks[task_index])
                uncompleted_tasks.remove(tasks[task_index])
                print("Task marked as complete!\n")
            else:
                print("Invalid task index")
        except ValueError:
            pass
                    #print("Invalid input. Enter a valid number")

    elif choice == "3":
        print("++======================================================++")
        print("++                    Tasks List                        ++")
        print("++                                                      ++")
        for i, task in enumerate(tasks):
            status = "Complete" if task["complete"] else "Incomplete"
            print(f"++  {i + 1}. {task['task']} - {status}")
            print("++======================================================++")
        print("\n")

    elif choice == "4":
        if not tasks:
            print("No tasks to remove")
            continue

        completed_tasks.clear()
        uncompleted_tasks.clear()

        for task in tasks:
            if task["complete"]:
                completed_tasks.append(task)
            else:
                uncompleted_tasks.append(task)

        tasks = uncompleted_tasks.copy()
        print("Completed tasks removed successfully")

    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")