from tasks import (
    add_task,
    view_task,
    complete_task,
    edit_task,
    delete_task,
    filter_task
)

from storage import save_json, load_json


def main():
    tasks = load_json()

    while True:
        title = "📝 THINGS TO DO"
        print(f"\n*** {title} ***")
        print("-" * 20)
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Edit task")
        print("5. Delete task")
        print("6. Filter tasks")
        print("7. Exit")
        print()

        try:
            choice = int(input("What do you want to do? "))
        except ValueError:
            print("Your choice must be in digit!")
            continue

        if choice == 1:
            add_task(tasks)
            save_json(tasks)
        elif choice == 2:
            view_task(tasks)
        elif choice == 3:
            complete_task(tasks)
            save_json(tasks)
        elif choice == 4:
            edit_task(tasks)
            save_json(tasks)
        elif choice == 5:
            delete_task(tasks)
            save_json(tasks)
        elif choice == 6:
            filter_task(tasks)
        elif choice == 7:
            print("Thanks for using this application!")
            break
        else:
            print("Invalid choice! Try again.")


main()
