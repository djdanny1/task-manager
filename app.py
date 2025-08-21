def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    name, priority, due_date = parts
                    tasks.append({"name": name, "priority": priority, "due_date": due_date})
                else:
                    print(f"Skipping invalid line in file: {line.strip()}")
    except FileNotFoundError:
        # Create empty file if it doesn't exist
        open("tasks.txt", "w").close()
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['name']} | {task['priority']} | {task['due_date']}\n")




def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    print("\nSort tasks by:")
    print("1. Priority (High → Low)")
    print("2. Due date (earliest first)")
    print("3. No sorting")
    choice = input("Choose an option: ")

    if choice == "1":
        # Define priority order
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        tasks_sorted = sorted(tasks, key=lambda x: priority_order.get(x['priority'], 4))
    elif choice == "2":
        tasks_sorted = sorted(tasks, key=lambda x: x['due_date'])
    else:
        tasks_sorted = tasks

    print("\nTasks:")
    for i, task in enumerate(tasks_sorted, 1):
        print(f"{i}. {task['name']} - Priority: {task['priority']}, Due: {task['due_date']}")


def add_task(tasks):
    name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ")
    due_date = input("Enter due date (DD-MM-YYYY): ")
    tasks.append({"name": name, "priority": priority, "due_date": due_date})
    save_tasks(tasks)
    print(f"Task '{name}' added!")

def delete_task(tasks):
    show_tasks(tasks)
    task_num = int(input("Enter the number of the task to delete: "))
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{removed['name']}' deleted!")
    else:
        print("Invalid task number.")

# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Try Again!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()