todo_list = []

def show_menu():
    print("\n--- MENU ---")
    print("1. Add a new task")
    print("2. Show all tasks")
    print("3. Edit a task")
    print("4. Remove a task")
    print("5. Exit")

def add_task():
    task = input("Write the task you want to add: ")
    todo_list.append(task)
    print("Task saved!")

def view_tasks():
    if not todo_list:
        print("Your list is empty.")
    else:
        print("\nTasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    if todo_list:
        try:
            num = int(input("Enter the task number to edit: "))
            if 1 <= num <= len(todo_list):
                new_task = input("Write the new task: ")
                todo_list[num - 1] = new_task
                print("Task updated.")
            else:
                print("That number is not in the list.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if todo_list:
        try:
            num = int(input("Enter the task number to remove: "))
            if 1 <= num <= len(todo_list):
                removed = todo_list.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("That number is not in the list.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Pick an option (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
