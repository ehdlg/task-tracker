from datetime import datetime

from colorama import Fore

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

    print(f"{Fore.GREEN}Task added succesfully (ID: {new_task.get('id')})")


def delete_task(id: int):
    tasks = get()

    for index, task in enumerate(tasks):
        task_id = task.get("id", None)

        if task_id == id:
            del tasks[index]
            save(tasks)

            print(f"{Fore.GREEN}Task {id} deleted")
            exit()

    return task_not_found(id)


def update_task(id: int, new_description: str):
    tasks = get()

    for index, task in enumerate(tasks):
        task_id = task.get("id", None)
        print(task_id, id)

        if task_id == id:
            print("task updating...")
            task.update({
                "description": new_description,
                "updated_at": str(datetime.now()),
            })

            save(tasks)

            print(f"{Fore.GREEN}Task {id} suffesfully updated")
            exit()

    return task_not_found(id)


def task_not_found(id: int):
    print(f"{Fore.YELLOW}Task {id} not found")

    exit()
