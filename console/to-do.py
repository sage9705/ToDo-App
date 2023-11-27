#Terminal based to-do application
#v3.0
#Auhor: Edem Godwin Kumahor

# Initialize empty lists to store tasks, completed tasks, and uncompleted tasks
# Function to print the To-Do Menu
def print_menu():
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

# Function to add a task to the tasks and uncompleted_tasks lists
def add_task(tasks, uncompleted_tasks):
    task = input("Enter the task: ")
    new_task = {"task": task, "complete": False}
    tasks.append(new_task)
    uncompleted_tasks.append(new_task)
    print("Task added successfully!\n\n")

# Function to mark a task as complete and update the uncompleted_tasks list
def mark_task_complete(tasks, uncompleted_tasks):
    if not tasks:
        print("No tasks to mark as complete")
        return

    try:
        index_input = input("Enter the task index (number assigned to task) to mark as complete: ")
        if index_input.isdigit():
            task_index = int(index_input) - 1

            if 0 <= task_index < len(tasks):
                task = tasks[task_index]

                if not task["complete"]:
                    task["complete"] = True
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

# Function to display the list of all tasks with their statuses
def view_all_tasks(tasks):
    print("++======================================================++")
    print("++                    All Tasks List                    ++")
    print("++                                                      ++")
    for i, task in enumerate(tasks):
        status = "Complete" if task["complete"] else "Incomplete"
        print(f"++  {i + 1}. {task['task']} - {status}")
        print("++======================================================++")
    print("\n\n")

# Function to display the list of completed tasks
def view_completed_tasks(tasks):
    completed_tasks = [task for task in tasks if task["complete"]]
    
    if not completed_tasks:
        print("No completed tasks to display")
        return
    
    print("++======================================================++")
    print("++                   Completed Tasks                    ++")
    print("++                                                      ++")
    for i, task in enumerate(completed_tasks):
        print(f"++  {i + 1}. {task['task']} - Complete")
        print("++======================================================++")
    print("\n\n")

# Function to display the list of uncompleted tasks
def view_uncompleted_tasks(uncompleted_tasks):
    print("++======================================================++")
    print("++                 Uncompleted Tasks                    ++")
    print("++                                                      ++")
    for i, task in enumerate(uncompleted_tasks):
        print(f"++  {i + 1}. {task['task']} - Incomplete")
        print("++======================================================++")
    print("\n\n")

# Function to remove completed tasks from the tasks and uncompleted_tasks lists
def remove_completed_tasks(tasks, uncompleted_tasks):
    if not any(task["complete"] for task in tasks):
        print("No completed tasks to remove")
        return

    completed_tasks = [task for task in tasks if task["complete"]]
    for task in completed_tasks:
        tasks.remove(task)
    uncompleted_tasks[:] = [task for task in tasks if not task["complete"]]
    print("Completed tasks removed successfully")

# Main function to run the To-Do List application
def main():
    tasks = []              # List to store all tasks
    uncompleted_tasks = []  # List to store uncompleted tasks

    while True:
        print_menu()
        choice = input("\nEnter option (1-7): ")

        if choice == "1":
            add_task(tasks, uncompleted_tasks)
        elif choice == "2":
            mark_task_complete(tasks, uncompleted_tasks)
        elif choice == "3":
            view_all_tasks(tasks)
        elif choice == "4":
            view_completed_tasks(tasks)
        elif choice == "5":
            view_uncompleted_tasks(uncompleted_tasks)
        elif choice == "6":
            remove_completed_tasks(tasks, uncompleted_tasks)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Run the application if the script is executed directly
if __name__ == "__main__":
    main()

