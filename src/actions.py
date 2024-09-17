from datetime import datetime

from data_service import add, get, get_id, save


def add_task(description: str):
    new_task = {
        "id": get_id(),
        "description": description,
        "completed": False,
        "created_at": str(datetime.now()),
        "updated_at": None,
    }

    add(new_task)

    print(f"Task added succesfully (ID: {new_task.get('id')})")


def delete_task(id: int):
    tasks = get()

    for index, task in enumerate(tasks):
        task_id = task.get("id", None)

        if task_id == id:
            del tasks[index]
            save(tasks)

            print(f"Task {id} deleted")
            exit()

    print(f"Task {id} not found")
    exit()
