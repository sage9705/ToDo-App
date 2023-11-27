# To-Do List Application (v4.0)

This is version 4.0 of the To-Do List application, featuring additional functionality and improvements compared to the previous version (v3.0).

## Changes from v3.0

1. **Menu Expansion**
   - The menu has been expanded to include an option for viewing history tasks.
   - Option 7 now allows users to view tasks that have been marked as complete and subsequently moved to the history.

2. **History Tasks List**
   - A new list, `history_tasks_list`, has been introduced to store completed tasks that have been moved from the main task list.
   - The `view_history_tasks()` function displays the history tasks with an indication of their completion status.

3. **Remove Completed Tasks Update**
   - The `remove_completed_tasks()` function now moves completed tasks to the history tasks list instead of discarding them entirely.
   - The main task list is updated to remove completed tasks.

4. **Code Structure**
   - The structure of the `main()` function has been modified to accommodate the new menu option and associated functionality.
   - The history tasks list is now a parameter in relevant functions.

## Usage

1. **Add Task**
   - Choose option 1 to add a new task.
   - Enter the task when prompted.
   - The task will be added to the list of tasks and the list of uncompleted tasks.

2. **Mark Task as Complete**
   - Choose option 2 to mark a task as complete.
   - Enter the task index (number assigned to the task) when prompted.
   - The task will be marked as complete and moved to the list of completed tasks.

3. **View All Tasks**
   - Choose option 3 to view the list of all tasks.
   - The list will display each task with its status (Complete/Incomplete).

4. **View Completed Tasks**
   - Choose option 4 to view the list of completed tasks.
   - The list will display completed tasks with a clear indication of their status.

5. **View Uncompleted Tasks**
   - Choose option 5 to view the list of uncompleted tasks.
   - The list will display uncompleted tasks with a clear indication of their status.

6. **Remove Completed Tasks**
   - Choose option 6 to move completed tasks to the history tasks list.
   - The completed tasks will be removed from the main task list but stored in the history tasks list.

7. **View History Tasks**
   - Choose option 7 to view the list of history tasks.
   - The list will display tasks that have been marked as complete and moved from the main task list to history.

8. **Exit**
   - Choose option 8 to exit the application.

## How to Run

1. Copy the code and paste it into a Python file, for example, `todo_app.py` or you can simply clone the repository.
2. Open a terminal or command prompt.
3. Navigate to the directory where `todo_app.py` is located.
4. Run the Python file using the following command:

   python todo_app.py



## Prerequisites

Ensure that you have Python installed on your system before running the application. If not, you can download and install Python from [python.org](https://www.python.org/).



## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/sage9705/ToDo-App/blob/main/LICENSE) file for details.
