class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. [{'Done' if task['completed'] else 'Not Done'}] {task['name']}")

    def add_task(self, name):
        self.tasks.append({'name': name, 'completed': False})
        print(f"Task '{name}' added to your to-do list.")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number. Please enter a valid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' removed from your to-do list.")
        else:
            print("Invalid task number. Please enter a valid task number.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application Instructions:")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            task_name = input("Enter the task: ")
            todo_list.add_task(task_name)
        elif choice == "3":
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == "4":
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()