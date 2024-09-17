import json

DEFAULT_FILE_VALUE: list = []


def get_tasks() -> list:
    try:
        with open("../data.json", "r") as tasks_file:
            raw_data = tasks_file.read()
            data = json.loads(raw_data)

            return data
    except Exception:
        persist_data(DEFAULT_FILE_VALUE)

        return DEFAULT_FILE_VALUE


def add_task(new_task):
    tasks = get_tasks()

    tasks.append(new_task)

    persist_data(tasks)


def persist_data(new_tasks: list) -> None:
    with open("../data.json", "w+") as f:
        json.dump(new_tasks, f)
