import sys
from tasks import add_task, update_task, delete_task, list_tasks

def main():
    argument = sys.argv[1:]
    if not argument:
        print("ERROR: You must type arguments")
        return
    command = argument[0]
    if command == "add":
        description = " ".join(argument[1:]).strip()
        if not description:
            print("ERROR: You must provide a description for the task")
            return
        add_task(description)
    elif command == "update":
        if len(argument) < 2:
            print("ERROR: You must provide the task ID and the new description")
            return
        try:
            task_id = int(argument[1])
        except ValueError:
            print("ERROR: Task ID must be an integer")
            return
        new_status = argument[2].strip() if len(argument) > 2 else None  # Status update
        new_description = " ".join(argument[3:]).strip()
        if not new_description:
            print("ERROR: You must provide a new description for the task")
            return
        update_task(task_id, new_description, new_status)
        print(f"Task with ID {task_id} has been updated")
    elif command == "delete":
        if len(argument) < 2:
            print("ERROR: you must provide the task ID to delete")
            return
        try:
            task_id = int(argument[1])
        except ValueError:
            print("ERROR: Task ID must be an integer")
            return
        delete_task(task_id)
        print(f"Task with ID {task_id} has been deleted")
    elif command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAT']}, updatedAt: {task['updatedAt']}")

if __name__ == "__main__":
    main()