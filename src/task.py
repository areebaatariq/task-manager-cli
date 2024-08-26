from dataclasses import dataclass, field

@dataclass
class Task:
    task_id: str
    description: str
    completed: bool = field(default=False)

    def mark_as_completed(self):
        self.completed = True

    def display(self):
        status = "Completed" if self.completed else "Pending"
        print(f"ID: {self.task_id}, Description: {self.description}, Status: {status}")
