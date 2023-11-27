# To-Do List Application (v3.0)

This is version 3.0 of the To-Do List application. Significant changes and improvements have been made to enhance code organization, modularity, and readability compared to the previous version (v2.2).

## Changes from v2.2

1. **Function Modularization**
   - The code has been organized into functions to improve modularity and readability.
   - Each major functionality (e.g., adding a task, marking a task as complete, viewing tasks) has its own dedicated function.

2. **Code Structuring**
   - The main part of the code has been encapsulated within a `main()` function.
   - The functions for printing the menu, adding a task, marking a task as complete, and viewing tasks are defined outside the main loop for better structure.

3. **Code Reusability**
   - Functions like `add_task()`, `mark_task_complete()`, `view_all_tasks()`, `view_completed_tasks()`, and `view_uncompleted_tasks()` can be easily reused in other parts of the program or extended for future modifications.

4. **Improved User Feedback**
   - User feedback messages have been refined for clarity and consistency across different functions.
   - Messages are displayed when there are no tasks to mark as complete, no completed tasks to display, or no completed tasks to remove.

5. **Error Handling**
   - Exception handling has been improved, providing more informative error messages for invalid inputs.

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
   - Choose option 6 to remove completed tasks from the list.
   - The completed tasks will be cleared from the list of completed tasks, and the list of uncompleted tasks will be updated.

7. **Exit**
   - Choose option 7 to exit the application.

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
