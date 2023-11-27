# To-Do List Application (v1.0)

This simple To-Do List application allows you to manage your tasks by adding, marking as complete, viewing, and removing tasks. The application runs in an infinite loop until you choose to exit.

## Usage

1. **Add Task**
   - Choose option 1 to add a new task.
   - Enter the task when prompted.
   - The task will be added to the list of tasks and the list of uncompleted tasks.

2. **Mark Task as Complete**
   - Choose option 2 to mark a task as complete.
   - Enter the task index (number assigned to the task) when prompted.
   - The task will be marked as complete and moved to the list of completed tasks.

3. **View Tasks**
   - Choose option 3 to view the list of tasks.
   - The list will display each task with its status (Complete/Incomplete).

4. **Remove Completed Tasks**
   - Choose option 4 to remove completed tasks from the list.
   - The completed tasks will be cleared from the list of completed tasks, and the list of uncompleted tasks will be updated.

5. **Exit**
   - Choose option 5 to exit the application.

## Notes
- Tasks are stored in the `tasks` list.
- Completed tasks are stored in the `completed_tasks` list.
- Uncompleted tasks are stored in the `uncompleted_tasks` list.

### How to Run
1. Copy the code into a Python file (e.g., `todo_app.py`).
2. Run the Python file using a Python interpreter.

```bash
  python todo_app.py


