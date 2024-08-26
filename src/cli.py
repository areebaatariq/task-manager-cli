from dataclasses import dataclass
from src.utils import TaskManager

@dataclass
class CLI:
    file_path: str
    manager: TaskManager = None  # Default to None, will be initialized in __post_init__

    def __post_init__(self):
        # Initialize TaskManager after the object is created
        self.manager = TaskManager(self.file_path)

    def show_menu(self):
        print("Task Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

    def get_user_input(self):
        try:
            return int(input("Choose an option: "))
        except ValueError:
            return 0

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_user_input()
            if choice == 1:
                description = input("Enter task description: ")
                self.manager.add_task(description)
            elif choice == 2:
                try:
                    task_id = input("Enter task ID to delete: ").strip()
                    if not task_id:
                        raise ValueError("No task ID provided.")  # Raise an error if the input is empty
                    self.manager.delete_task(task_id)
                except ValueError as e:
                    print(f"Invalid input: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            elif choice == 3:
                try:
                    task_id = input("Enter task ID to mark as completed: ").strip()
                    self.manager.mark_as_completed(task_id)
                except ValueError:
                    print("Invalid ID. Please enter a valid UUID.")
            elif choice == 4:
                self.manager.list_tasks()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
