# ToDo List Application
#v4.0
#Author: Edem Godwin Kumahor


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
    print("++ 7. View History Tasks     ++")
    print("++ 8. Exit                   ++")
    print("+++++++++++++++++++++++++++++++")

def add_task(tasks, uncompleted_tasks):
    task = input("Enter the task: ")
    new_task = {"task": task, "complete": False}
    tasks.append(new_task)
    uncompleted_tasks.append(new_task)
    print("Task added successfully!\n\n")

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

def view_all_tasks(tasks):    
    print("++======================================================++")
    print("++                    All Tasks List                    ++")
    print("++                                                      ++")
    for i, task in enumerate(tasks):
        status = "Complete" if task["complete"] else "Incomplete"
        print(f"++  {i + 1}. {task['task']} - {status}")
        print("++======================================================++")
    print("\n\n")

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

def view_uncompleted_tasks(uncompleted_tasks):
    print("++======================================================++")
    print("++                 Uncompleted Tasks                    ++")
    print("++                                                      ++")
    for i, task in enumerate(uncompleted_tasks):
        print(f"++  {i + 1}. {task['task']} - Incomplete")
        print("++======================================================++")
    print("\n\n")

def remove_completed_tasks(tasks, uncompleted_tasks, history_tasks_list):
    completed_tasks = [task for task in tasks if task["complete"]]

    if not completed_tasks:
        print("No completed tasks to remove")
        return

    history_tasks_list.extend(completed_tasks)
    tasks[:] = [task for task in tasks if not task["complete"]]
    uncompleted_tasks[:] = [task for task in tasks if not task["complete"]]
    print("Completed tasks removed successfully")


def view_history_tasks(history_tasks_list):
    if not history_tasks_list:
        print("No history tasks to display")
        return

    print("++======================================================++")
    print("++                History Tasks List                    ++")
    print("++                                                      ++")
    for i, task in enumerate(history_tasks_list):
        print(f"++  {i + 1}. {task['task']} - Complete")
        print("++======================================================++")
    print("\n\n")

def main():
    tasks = []
    uncompleted_tasks = []
    history_tasks_list = []

    while True:
        print_menu()
        choice = input("\nEnter option (1-8): ")

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
            remove_completed_tasks(tasks, uncompleted_tasks, history_tasks_list)
        elif choice == "7":
            view_history_tasks(history_tasks_list)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
