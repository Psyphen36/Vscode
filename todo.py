tasks = []
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")
def show_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("Current tasks:")
    for index, task in enumerate(tasks):
        print(f"{index}. {task}")
    print()
def complete_task():
    print("Current tasks:")
    show_tasks()
    task_index = int(input("Enter the index of the task to mark as complete: "))
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index!")
        return
    completed_task = tasks.pop(task_index)
    print(f"Task '{completed_task}' marked as complete!")
def main():
    while True:
        print("===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            complete_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
