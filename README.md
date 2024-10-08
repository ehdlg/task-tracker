# Task Tracker CLI

This is a simple command-line interface (CLI) application for managing tasks. It was built as part of the [roadmap.sh Task Tracker project](https://roadmap.sh/projects/task-tracker) to practice and familiarize myself with Python, developing skills such as efficient handling of lists, lambdas, dictionaries, `argparser`, dates, reading/writing files and working with the `json` module.

## Features

The application allows users to manage tasks through terminal commands. Tasks are stored in a JSON file, and the following actions can be performed:

- Add, update, and delete tasks.
- Mark a task as "in progress", "done", or "todo".
- List all tasks.
- List tasks by status (pending, in progress, or completed).

## Requirements

- **Python**

- **Pip**

## Installation

To install the Task Tracker CLI from PyPI, use the following command:

```bash
pip install tasktracker-ehdlg
```

Then you can use the tool with the script `task-tracker-ehdlg`.

You can also install and use the program following these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/ehdlg/task-tracker
   cd task-tracker
   ```

2. Intall the required packages with Pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## Commands

The application accepts several commands to interact with the tasks:

```bash
    add <description>           Add a new task.
    delete <id>                 Delete an existing task.
    update <id> <description>   Update an existing task.
    mark-in-progress <id>       Mark the task as 'in progress'.
    mark-done <id>              Mark the task as 'done'.
    mark-todo <id>              Mark the task as 'todo'.
    list [filter]               List the tasks in a table.

options:
  -h, --help            Show the help message and exit.
```

## Usage Examples

1. Add a new task:

   ```bash
     python main.py add "Study Python"
   ```

2. Update a task:

   ```bash
     python main.py update 1 "Study advanced Python"
   ```

3. Delete a task:

   ```bash
     python main.py delete 1
   ```

4. Mark a task as 'in progress':

   ```bash
     python main.py mark-in-progress 1
   ```

5. Mark a task as 'done':

   ```bash
     python main.py mark-done 1
   ```

6. Mark a task as 'todo':

   ```bash
     python main.py mark-todo 1
   ```

7. List all tasks:

   ```bash
     python main.py list
   ```

8. List done tasks:

   ```bash
     python main.py list done
   ```

### Learnings

This project has allowed me to gain fluency in Python by working with:

- Efficient handling of lists and lambdas.
- Using dictionaries to manage tasks and their statuses
- Installing and using packages from the standard library.
- Reading and writing JSON files to persist using the json module.
- Using the argparse module to process command-line arguments.
- Handling dates to add timestamps to tasks.

### Objectives

The goal of this project is to continue improving my Python skills, deepening my understanding of the language, and familiarizing myself with developing CLI applications that interact with files and handle terminal arguments
