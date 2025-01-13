tasks = []

def show_menu():
    print("\n1. View tasks\n2. Add task\n3. Delete task\n4. Complete task\n5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    for i, task in enumerate(tasks):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i+1}. {status} {task['task']}")

def add_task():
    task_description = input("Enter a task: ")  # No input validation
    tasks.append({'task': task_description, 'completed': False})

def delete_task():
    view_tasks()
    if not tasks:  # Check if there are no tasks to delete
        print("No tasks to delete.")
        return

    task_num = input("Enter task number to delete: ")
    if not task_num.isdigit():  # Ensure the input is a number
        print("Error: Please enter a valid number.")
        return

    task_num = int(task_num) - 1
    if task_num < 0 or task_num >= len(tasks):  # Validate the task number
        print("Error: Invalid task number.")
    else:
        deleted_task = tasks.pop(task_num)
        print(f"Task '{deleted_task['task']}' has been deleted.")

def complete_task():
    view_tasks()
    task_num = int(input("Enter task number to complete: ")) - 1
    tasks[task_num]['completed'] = True

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
