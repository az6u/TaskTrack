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


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def remove_task(tasks):
    """Prompt the user to select and remove a task.

    Return True when a task is removed and False otherwise.
    """
    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)
    selection = input("Enter the number of the task to remove: ").strip()

    if not selection.isdigit():
        print("Please enter a valid task number.")
        return False

    task_number = int(selection)

    if task_number < 1 or task_number > len(tasks):
        print("That task number does not exist.")
        return False

    removed_task = tasks.pop(task_number - 1)
    print(f'Removed task: "{removed_task}"')
    return True


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
            if remove_task(tasks):
                save_tasks(tasks, TASKS_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
