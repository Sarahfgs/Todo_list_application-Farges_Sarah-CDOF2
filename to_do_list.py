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
    task_num = int(input("Enter task number to delete: ")) - 1
    tasks.pop(task_num)  # Bug: Doesn't check if task_num is within valid range

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
