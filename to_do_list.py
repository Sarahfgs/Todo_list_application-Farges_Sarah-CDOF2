tasks = []

def show_menu():
    print("\n1. View tasks\n2. Add task\n3. Delete task\n4. Complete task\n5. Exit")

def view_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. [ ] {task}")

def add_task():
    tasks.append(input("Enter a task: "))  # Mistake: No validation, appending string

def delete_task():
    view_tasks()
    task_num = int(input("Enter task number to delete: "))
    removed_task = tasks.pop(task_num)  # Mistake: Incorrect index
    print(f"Task '{removed_task}' deleted!")

def complete_task():
    view_tasks()
    task_num = int(input("Enter task number to complete: "))
    tasks[task_num] += " (completed)"  # Mistake: Incorrect task structure, it's a string now

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1': view_tasks()
        elif choice == '2': add_task()
        elif choice == '3': delete_task()
        elif choice == '4': complete_task()
        elif choice == '5': break
        else: print("Invalid option.")

if __name__ == "__main__":
    main()