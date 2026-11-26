# To Do List v1
tasks = []
while True:
    print("--- TO-DO LIST ---")
    print("1. List Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    wish = input("Please enter the number of the transaction you wish to perform: ")
    if wish == "1":
        if len(tasks) == 0:
            print("There are no tasks added yet.")
        else:
            meter = 1
            for t in tasks:
                print(f"{meter}- {t}")
                meter += 1
    elif wish == "2":
        task = input("You can write your task: ")
        tasks.append(task)
        print("Successfully added")
    elif wish == "3":
        meter = 1
        for t in tasks:
            print(f"{meter}- {t}")
            meter += 1
        del_task = input("Which task would you like to delete?: ")
        del_task = int(del_task)
        tasks.pop(del_task - 1)
        print("It has been successfully deleted.")
    else:
        print("Thank you!")
        break