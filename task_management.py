tasks = [
    {
        "task_id": 1,
        "task_name": "Complete ANN & CNN revision",
        "priority": "High",
        "due_date": "31/10/2026",
        "status": "Pending"
    },
    {
        "task_id": 2,
        "task_name": "Everyday Practice Python problems",
        "priority": "Medium",
        "due_date": "01/11/2026",
        "status": "Completed"
    },
    {
        "task_id": 3,
        "task_name": "Exercise every day",
        "priority": "High",
        "due_date": "31/10/2026",
        "status": "Completed"
    }
]


def add_task(task_id, task_name, priority, due_date, status):
    task = {}
    task["task_id"] = task_id
    task["task_name"] = task_name
    task["priority"] = priority
    task["due_date"] = due_date
    task["status"] = status
    tasks.append(task)
    print(f"Your new task : {task}")


def view_all_task():
    if tasks:
        print("Your all tasks are given below :")
        for task_dict in tasks:
            print(task_dict)
    else:
        print("No task present")


def edit_task(task_id, task_name, priority, due_date, status):

    for task_dict in tasks:
        id = task_dict["task_id"]
        if id == task_id:
            task_dict["task_name"] = task_name
            task_dict["priority"] = priority
            task_dict["due_date"] = due_date
            task_dict["status"] = status
            print(f"Updated task details : {task_dict}")
            break


def delete_task(task_id):

    for task_dict in tasks:
        id = task_dict["task_id"]
        if id == task_id:
            tasks.remove(task_dict)
            view_all_task()
            break


def task_status_change(task_id, status):
    for task_dict in tasks:
        id = task_dict["task_id"]
        if id == task_id:
            task_dict["status"] = status
            print(task_dict)
            break


def sort_tasks():

    for task_dict in tasks:
        priority = task_dict["priority"].strip().lower()

        if priority == "high":
            print(task_dict)

    for task_dict in tasks:
        priority = task_dict["priority"].strip().lower()

        if priority == "medium":
            print(task_dict)

    for task_dict in tasks:
        priority = task_dict["priority"].strip().lower()

        if priority == "low":
            print(task_dict)


def search_task(task_id):

    for task_dict in tasks:
        id = task_dict["task_id"]
        if id == task_id:
            print(task_dict)
            break


def present_task_id(task_id):
    for task_dict in tasks:
        id = task_dict["task_id"]
        if task_id == id:
            return True
    else:
        return False


while True:
    try:
        user_input = int(input(
            "Select an operation:\n"
            "Press 1: Add a task\n"
            "Press 2: view all tasks\n"
            "Press 3: Edit task\n"
            "Press 4: Delete task\n"
            "Press 5: Change task status\n"
            "Press 6: Sort all tasks\n"
            "Press 7: Search a task\n"
            "Press 8: Exit the loop\n"
            "Enter your choice: "
        ))
        if user_input == 1:
            user_preference = input(
                "Would you like to view all existing tasks before adding a new task?\n"
                "Enter yes or no: "
            ).lower()

            if user_preference == "yes":
                view_all_task()

                user_next_preference = input(
                    "Can you add new task?\n"
                    "So write yes or no: ").lower()

                if user_next_preference == "yes":
                    id = int(input("Enter task ID : "))
                    task_id_value = present_task_id(id)

                    if task_id_value != True:
                        name = input("Enter task name : ")
                        priority = input(
                            "Enter task priority (High/Low/Medium) : ").lower()

                        if priority in ["high", "low", "medium"]:
                            due_date = input("Enter due date (dd/mm/yyyy) : ")
                            status = input(
                                "Enter give task status (pending/completed) : ").lower()

                            if status in ["pending", "completed"]:
                                add_task(id, name, priority, due_date, status)
                            else:
                                print("status in pending or completed")

                        else:
                            print("priority in high or low or medium")

                    else:
                        print("ID value always unique")

            elif user_preference == "no":
                id = int(input("Enter task ID : "))
                task_id_value = present_task_id(id)

                if task_id_value != True:
                    name = input("Enter task name : ")
                    priority = input(
                        "Enter task priority (High/Low/Medium) : ").lower()

                    if priority in ["high", "low", "medium"]:
                        due_date = input("Enter due date (dd/mm/yyyy) : ")
                        status = input(
                            "Enter give task status (pending/completed) : ").lower()

                        if status in ["pending", "completed"]:
                            add_task(id, name, priority, due_date, status)
                        else:
                            print("status in pending or completed")

                    else:
                        print("priority in high or low or medium")

                else:
                    print("ID value always unique")

            else:
                print("write only yes or no")

        elif user_input == 2:
            view_all_task()

        elif user_input == 3:
            id = int(input("Enter task ID: "))
            id_value = present_task_id(id)
            if id_value == True:
                print("Existing task details: ")
                search_task(id)

                update_name = input(
                    "Enter updated task name ")
                update_priority = input(
                    "Enter updated task priority (High/Low/Medium) :").lower()

                if update_priority.strip() in ["high", "low", "medium"]:
                    update_date = input("Enter updated date (dd/mm/yyyy): ")
                    update_status = input(
                        "Enter updated status (pending/completed): ").lower()

                    if update_status.strip() in ["pending", "completed"]:
                        edit_task(id, update_name, update_priority,
                                  update_date, update_status)

                    else:
                        print("status in pending or completed")
                else:
                    print("priority in high or low or medium")

            else:
                print("Task ID not present")

        elif user_input == 4:
            id = int(input("Enter task ID: "))
            id_value = present_task_id(id)
            if id_value == True:
                delete_task(id)
            else:
                print("ID value not found")

        elif user_input == 5:
            id = int(input("Enter task ID: "))
            id_value = present_task_id(id)

            if id_value == True:
                print("Current status of this task : ")
                search_task(id)
                task_status = input(
                    "Enter task status (pending/completed) :  ").lower()

                if task_status.strip() in ["pending", "completed"]:
                    task_status_change(id, task_status)
                else:
                    print("status in pending or completed, not other values.")
            else:
                print("ID not found")

        elif user_input == 6:
            if tasks:
                sort_tasks()
            else:
                print("No task present")

        elif user_input == 7:
            id = int(input("Enter task ID: "))
            id_value = present_task_id(id)
            if id_value == True:
                search_task(id)
            else:
                print("ID not found")

        elif user_input == 8:
            break

        else:
            print("Not match the choice")
    except ValueError:
        print("Please enter a valid number")
