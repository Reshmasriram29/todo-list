# todo_list.py

# Initialize an empty list to store tasks
tasks = []

def add_task(task):
    """Add a new task to the list."""
    tasks.append(task)
    print(f'Task "{task}" added!')

def view_tasks():
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(task_number):
    """Remove a task from the list by its number."""
    try:
        task = tasks.pop(task_number - 1)
        print(f'Task "{task}" removed!')
    except IndexError:
        print("Invalid task number.")

def main():
    """Main function to run the Todo List application."""
    while True:
        print("\nTodo List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the Todo List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
