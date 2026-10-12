"""A command-line task manager created for CPS 310.

This checkpoint represents the TaskTrack project after ICA05 and before
the unit testing unit.
"""

TASKS_FILE = "tasks.txt"


def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


def add_task(tasks):
    """Prompt the user for a task and add it to the task list.

    Return True when a task is added and False when the input is empty.
    """
    task = input("Enter a new task: ").strip()

    if not task:
        print("A task cannot be empty.")
        return False

    tasks.append(task)
    print("Task added successfully.")
    return True


def remove_task(tasks, selection):
    """Remove a task from the list when the user selects a valid number."""
    if not tasks:
        print("No tasks available to remove.")
        return False

    try:
        task_number = int(selection)
    except ValueError:
        print("Please enter a valid task number.")
        return False

    if task_number < 1 or task_number > len(tasks):
        print("Task number out of range.")
        return False

    removed_task = remove_task_by_number(tasks, task_number)
    if removed_task is None:
        print("Task number out of range.")
        return False

    print(f"Task removed: {removed_task}")
    return True


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_task_by_number(tasks, task_number):
    """Remove a task by its displayed number and return the removed task.

    Return None when the task number is outside the valid range.
    """
    if task_number < 1 or task_number > len(tasks):
        return None

    return tasks.pop(task_number - 1)


def load_tasks(filename):
    """Load tasks from a text file and return them as a list."""
    tasks = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        return []

    return tasks


def save_tasks(tasks, filename):
    """Save all tasks to a text file, one task per line."""
    with open(filename, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")


def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            if add_task(tasks):
                save_tasks(tasks, TASKS_FILE)
        elif choice == "3":
            view_tasks(tasks)
            selection = input("Which task should be removed? ")
            if remove_task(tasks, selection):
                save_tasks(tasks, TASKS_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
