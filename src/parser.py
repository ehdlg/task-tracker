import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", help="Task description")

delete_parser = subparsers.add_parser("delete", help="Delete an existing task")
delete_parser.add_argument("id", help="Task's ID")

update_parser = subparsers.add_parser("update", help="Update an existing task")
update_parser.add_argument("id", help="Task's ID")
update_parser.add_argument("description", help="New taks description")


args = parser.parse_args()
