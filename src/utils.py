import json
import uuid
from dataclasses import dataclass, field
from typing import List
from src.task import Task

@dataclass
class TaskManager:
    file_path: str
    tasks: List[Task] = field(default_factory=list)

    def __post_init__(self):
        self.tasks = self.load_tasks()

    def add_task(self, description: str):
        # Generate a unique identifier for the task
        task_id = str(uuid.uuid4())[:3]
        task = Task(task_id, description)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{description}' added successfully with ID {task_id}.")

    def delete_task(self, task_id: str):
        if not self.tasks:
            print("No tasks available to delete.")
            return

        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

        if len(self.tasks) < initial_count:
            self.save_tasks()
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"No task found with ID {task_id}.")

    def mark_as_completed(self, task_id: str):
        if not self.tasks:
            print("No tasks available to mark as completed.")
            return

        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_completed()
                self.save_tasks()
                print(f"Task with ID {task_id} marked as completed.")
                break
        else:
            print(f"No task found with ID {task_id}.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                task.display()

    def load_tasks(self) -> List[Task]:
        try:
            with open(self.file_path, 'r') as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        tasks_data = [{'task_id': task.task_id, 'description': task.description, 'completed': task.completed} for task
                      in self.tasks]
        with open(self.file_path, 'w') as file:
            json.dump(tasks_data, file, indent=4)
