import sys
from tasks import add_task, update_task, delete_task, list_tasks, list_tasks_by_status

def main():
    argument = sys.argv[1:] # Place to store the arguments, ignoring the program name
    if not argument:
        print("ERROR: You must type arguments")
        return
    command = argument[0] # All comands will be int the first position of the argument list, after script name
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
        if argument[2].strip() == "todo" or argument[2].strip() == "in-progress" or argument[2].strip() == "done":
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
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, \n Created At: {task['createdAt']}, updatedAt: {task['updatedAt']}")
    elif command == "list_by_status":
        if len(argument) < 2:
            print("ERROR: you must provide the status to filter tasks")
            return
        status = argument[1].strip()
        tasks = list_tasks_by_status(status)
        print(f"Tasks with status '{status}':")
        if not tasks:
            print("No tasks found with this status.")
        else:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, \n Created At: {task['createdAt']}, updatedAt: {task['updatedAt']}")

if __name__ == "__main__":
    main()