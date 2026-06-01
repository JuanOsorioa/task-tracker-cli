from storage import load_tasks, save_tasks
from datetime import datetime

def add_task(description):
    tasks_list = load_tasks()
    if not tasks_list:
        new_id = 1 #Id start in 1 if anyother do not exist
    else:
        new_id = max(task["id"] for task in tasks_list) + 1 #Auto-incremented id system
    now_iso = datetime.now().isoformat()
    # Use iso format for date, it is a standard format and can be easily parsed later
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now_iso,
        "updatedAt": now_iso
    }

    tasks_list.append(new_task) #Add new task to task_list
    save_tasks(tasks_list) #Send tasks list to json
    print(f"Task saved with ID {new_id}")
