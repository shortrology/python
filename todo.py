# === Todo_List_App ===

todo_list = [{"name": "example1", "completed": False},
             {"name": "example2", "completed": True}
]

def display_task(any_list):
    count = 1
    for task in any_list:
        print(f"{count}) {task["name"]}: {task["completed"]}")
        count += 1

type(bool(int(0))), bool(int('1'))

def add_task(any_list):
    name = input("Enter task name:")
    task = {"name": name, "completed": False}
    any_list.append(task)

    return any_list


def complete_task(any_list):
    print("Look your list and enter task number to complete it")
    display_task(any_list)
    task_number = int(input("Enter number here:"))
    task = any_list[task_number-1]
    task["completed"] = True

    return any_list


def delete_task(any_list):
    print("select task to delete:")
    display_task(any_list)
    task_number = int(input("Enter number here:"))
    any_list.pop(task_number-1)

    return any_list


def run_todo():
    todo_list = []
    while True:
        print("Welcome to todo list")
        print("Option 1) Display Task")
        print("Option 2) Add Task")
        print("Option 3) Complete Task")
        print("Option 4) Delete Task")
        print("Option 5) Exit")
        
        option = input("\n Enetr any option \n")
        if option == "1":
            display_task(todo_list)
        elif option == "2":
            todo_list = add_task(todo_list)
        elif option == "3":
            todo_list = complete_task(todo_list)
        elif option == "4":
            todo_list = delete_task(todo_list)
        elif option == "5":    
            print("Thankyou")
            break
        else:
            print("Invalid Option: please enter correct option")

run_todo()
