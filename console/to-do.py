#Terminal based to-do application
#v2.0
#Auhor: Edem Godwin Kumahor

# Initialize empty lists to store tasks, completed tasks, and uncompleted tasks
tasks = []
completed_tasks = []
uncompleted_tasks = []

# Infinite loop for the To-Do List application
while True:
    # Display the To-Do Menu
    print("+++++++++++++++++++++++++++++++")
    print("++        To-Do Menu:        ++")
    print("++                           ++")
    print("++ 1. Add Task               ++")
    print("++ 2. Mark Task as Complete  ++")
    print("++ 3. View All Tasks         ++")
    print("++ 4. View Completed Tasks   ++")
    print("++ 5. View Uncompleted Tasks ++")
    print("++ 6. Remove Completed Tasks ++")
    print("++ 7. Exit                   ++")
    print("+++++++++++++++++++++++++++++++")

    # Get user choice
    choice = input("\nEnter option (1-7): ")

    # Option 1: Add Task
    if choice == "1":
        task = input("Enter the task: ")
        new_task = {"task": task, "complete": False}
        tasks.append(new_task)
        uncompleted_tasks.append(new_task)
        print("Task added successfully!\n\n")

    # Option 2: Mark Task as Complete
    elif choice == "2":
        # Check if there are tasks to mark as complete
        if not tasks:
            print("No tasks to mark as complete")
            continue

        try:
            index_input = input("Enter the task index(number assigned to task) to mark as complete: ")
            
            # Check if the input is a valid number
            if index_input.isdigit():
                task_index = int(index_input) - 1

                # Check if the task index is within the valid range
                if 0 <= task_index < len(tasks):
                    task = tasks[task_index]

                    # Check if the task is not already marked as complete
                    if not task["complete"]:
                        task["complete"] = True
                        completed_tasks.append(task)
                        uncompleted_tasks.remove(task)
                        print("Task marked as complete!")
                    else:
                        print("Task is already marked as complete")
                else:
                    print("Invalid task index")
            else:
                raise ValueError("Invalid input. Enter a valid number")
        except ValueError as e:
            print(e)

    # Option 3: View All Tasks
    elif choice == "3":
        print("++======================================================++")
        print("++                    All Tasks List                    ++")
        print("++                                                      ++")
        for i, task in enumerate(tasks):
            status = "Complete" if task["complete"] else "Incomplete"
            print(f"++  {i + 1}. {task['task']} - {status}")
            print("++======================================================++")
        print("\n\n")

    # Option 4: View Completed Tasks
    elif choice == "4":
        print("++======================================================++")
        print("++                   Completed Tasks                    ++")
        print("++                                                      ++")
        for i, task in enumerate(completed_tasks):
            print(f"++  {i + 1}. {task['task']} - Complete")
            print("++======================================================++")
        print("\n\n")

    # Option 5: View Uncompleted Tasks
    elif choice == "5":
        print("++======================================================++")
        print("++                 Uncompleted Tasks                    ++")
        print("++                                                      ++")
        for i, task in enumerate(uncompleted_tasks):
            print(f"++  {i + 1}. {task['task']} - Incomplete")
            print("++======================================================++")
        print("\n\n")

    # Option 6: Remove Completed Tasks
    elif choice == "6":
        # Check if there are completed tasks to remove
        if not completed_tasks:
            print("No completed tasks to remove")
            continue

        # Update tasks and uncompleted_tasks lists by removing completed tasks
        tasks = [task for task in tasks if not task["complete"]]
        uncompleted_tasks = [task for task in tasks if not task["complete"]]
        print("Completed tasks removed successfully")

    # Option 7: Exit
    elif choice == "7":
        print("Exiting...")
        break

    # Invalid choice: Provide user feedback
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
