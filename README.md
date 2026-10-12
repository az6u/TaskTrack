# TaskTrack

TaskTrack is a command-line task manager created for CPS 310. It allows users to view, add, and remove tasks while saving the task list to a text file so tasks remain available between program runs.

## Current Features

- View all saved tasks in a numbered list.
- Add new tasks.
- Reject empty task input.
- Remove an existing task by number.
- Reject nonnumeric and out-of-range task selections.
- Save task changes to `tasks.txt`.
- Load previously saved tasks when the program starts.

## Requirements

- Python 3

## Project Files

- `tasktrack.py` — Contains the TaskTrack program and menu logic.
- `tasks.txt` — Stores the current task list, one task per line.
- `.gitignore` — Prevents common local Python and environment files from being tracked by Git.
- `README.md` — Explains the project, its files, and how to run it.
- `REFLECTION.md` — Contains the ICA04 reflection questions.
- `collaboration_notes.txt` — Contains the final resolved line from the ICA05 merge-conflict exercise.

## Running the Program

Open a terminal in the `TaskTrack` project folder.

### Windows

```text
python tasktrack.py
```

If needed:

```text
py tasktrack.py
```

### macOS

```text
python3 tasktrack.py
```

## Task Persistence

When TaskTrack starts, it reads tasks from `tasks.txt`. After a task is successfully added or removed, the program rewrites `tasks.txt` so the updated list is available the next time the program runs.

If `tasks.txt` does not exist, TaskTrack starts with an empty task list instead of crashing.

## Sample Interaction

```text
TaskTrack Menu
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
Choose an option: 1

Tasks:
1. Complete CPS 310 assignment
2. Review Git commands
3. Study for upcoming quiz

Choose an option: 2
Enter a new task: Practice Python
Task added successfully.

Choose an option: 3

Tasks:
1. Complete CPS 310 assignment
2. Review Git commands
3. Study for upcoming quiz
4. Practice Python
Enter the number of the task to remove: 2
Removed task: "Review Git commands"
```

## Current Limitations

- Tasks contain plain text only.
- Tasks do not include priorities, due dates, or completion status.
- The program does not yet include automated unit tests.

## Version Control

TaskTrack uses Git for local version control and GitHub as its remote repository. Developers create a `commit` to record a meaningful project change, `push` local commits to GitHub, and `pull` remote changes into the local repository.
