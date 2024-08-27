
# Task Manager CLI Application

## Overview

This Python application is a command-line interface (CLI) tool to manage tasks. Users can add, delete, mark tasks as completed, and list all tasks. The tasks are stored persistently in a JSON file, allowing the data to persist between runs.

## Project Structure

The project is organized as follows:

```
project-name/
    |_ README.md
    |_ src/
        |_ __init__.py
        |_ main.py
        |_ task.py
        |_ utils.py  
        |_ CLI.py  
```

## Requirements

- Python 3.10 or higher

## Installation

1. Clone this repository to your local machine.

    ```sh
    git clone https://github.com/your-repo/task-manager-cli.git
    ```

2. Navigate to the project directory.

    ```sh
    cd task-manager-cli
    ```

3. (Optional) Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

Run the application using the following command:

```sh
python src/main.py
```

### Menu Options

When the application starts, it presents the following options:

1. **Add Task**: Allows you to add a new task with a description.
2. **Delete Task**: Prompts for a task ID to delete the corresponding task.
3. **Mark Task as Completed**: Prompts for a task ID to mark the task as completed.
4. **List Tasks**: Lists all tasks with their status (Completed or Pending).
5. **Exit**: Exits the application.

### Example

Here’s what you can expect when you run the application:

```
Task Manager
1. Add Task
2. Delete Task
3. Mark Task as Completed
4. List Tasks
5. Exit
Choose an option: 
```

## Notes

- If you enter an invalid choice, the application will prompt: "Invalid choice. Please try again."
- Tasks are saved in `tasks.json`, located in the root directory of the project.

ur project directory and paste the content above into it. If you need further assistance, just let me know!