from datetime import datetime


def select_task(tasks):
    while True:
        choice = input(
            "Enter task number or type (c) to cancel: "
        ).strip()

        if choice.lower() == "c":
            return None, None

        try:
            task_number = int(choice)
        except ValueError:
            print("Please enter a valid number!")
            continue

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number")
            continue

        return task_number - 1, tasks[task_number - 1]


def ask_yes_or_no(prompt):
    while True:
        answer = input(prompt).strip().upper()

        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("Invalid input! Enter Y or N.")


def add_task(tasks):
    while True:
        title = input("What is this task? ").strip().capitalize()
        if not title:
            print("Task title cannot be empty!")
            continue
        elif title.isdigit():
            print("Task title cannot be a number!")
            continue
        break

    while True:
        priority = input("How urgent is it? "
                         "(High, Medium or Low) ").strip().capitalize()
        if priority not in ("High", "Medium", "Low"):
            print("Please select urgency from given!")
            continue
        break

    new_task = {
        "task": title,
        "completed": False,
        "priority": priority,
        "due_date": datetime.now().strftime("%d-%m-%Y")
    }
    tasks.append(new_task)

    print("Task added successfully.")


def view_task(tasks):
    line = "-" * 72

    if not tasks:
        print("List is empty!")
        return

    print(
        f"{'Number':<10} {'Task':<25} {'Status':<12}"
        f"{'Priority':<12} {'Due_Date':<12}"
    )
    print(line)

    for number, item in enumerate(tasks, start=1):
        status = "✅" if item["completed"] else "⬜"
        print(
            f"{number:<10} {item['task']:<25} {status:<12} "
            f"{item['priority']:<7} {item['due_date']:>12}"
        )


def complete_task(tasks):
    if not tasks:
        print("There are no tasks to complete!")
        return

    view_task(tasks)

    _, selected = select_task(tasks)

    if selected is None:
        print("Returning to menu...")
        return

    print(
        f"You selected: {selected['task']} "
        f"due {selected['due_date']}"
    )

    if ask_yes_or_no("Are you sure you have completed this task? (Y/N): "):
        selected["completed"] = True
        print("Task marked as complete.")
    else:
        print("Task not completed.")


def delete_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    while True:
        view_task(tasks)

        index, selected = select_task(tasks)
        if selected is None:
            print("Returning to menu...")
            return

        print(
            f"You selected: {selected['task']}, "
            f"Completed: ({selected['completed']}) "
            f"Priority: ({selected['priority']})"
            )

        if ask_yes_or_no("Are you sure you want to delete this task? (Y/N): "):
            tasks.pop(index)
            print("Task deleted successfully!")
        else:
            print("Deletion cancelled!")

        if not tasks:
            print("No more tasks left.")
            break

        if ask_yes_or_no("Do you want to delete another task? (Y/N): "):
            continue
        else:
            break


def edit_task(tasks):
    if not tasks:
        print("No tasks found!")
        return

    view_task(tasks)

    _, selected = select_task(tasks)

    if selected is None:
        print("Returning to menu...")
        return

    while True:
        view_task([selected])

        print("What do you want to edit? ")
        print("1. Task title")
        print("2. Priority")
        print("3. Due date")
        print("4. Cancel")

        try:
            option = int(input())
        except ValueError:
            print("Enter edit option in digits!")
            continue

        if option == 1:
            while True:
                new_title = input(f"Task title [{selected['task']}]: "
                                  ).strip().capitalize()

                if not new_title:
                    print("New title cannot be empty")
                    continue

                if new_title.isdigit():
                    print("New title cannot be a number!")
                    continue
                selected["task"] = new_title
                print("Task title updated successfully!")
                break

        elif option == 2:
            while True:
                new_priority = input("How urgent is it? (High, Medium, Low: )"
                                     ).strip().capitalize()

                if new_priority not in ("High", "Medium", "Low"):
                    print("Select urgency from the options given")
                    continue

                selected["priority"] = new_priority
                print("Priority updated successfully!")
                break

        elif option == 3:
            while True:
                new_due_date = input("Enter due date (DD-MM-YYYY): ").strip()

                if not new_due_date:
                    print("Due Date cannot be empty")
                    continue

                try:
                    datetime.strptime(new_due_date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date! Use DD-MM-YYYY")
                    continue

                selected["due_date"] = new_due_date
                print("Due_date updated successfully!")
                break

        elif option == 4:
            print("Finished editing this task.")
            return

        else:
            print("Invalid option, choose between 1-4")


def show_matches(matches, no_match_message):
    if not matches:
        print(no_match_message)
    else:
        view_task(matches)


def filter_task(tasks):
    if not tasks:
        print("No tasks found!")
        return

    while True:
        print("Search by: ")
        print("1. Priority")
        print("2. Completion")
        print("3. Due date")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if choice == 1:
            target = input(
                "Which priority? (High, Medium, Low): "
            ).strip().capitalize()

            # matches = [item for item in tasks if item['priority'] == target]

            matches = []
            for item in tasks:
                if item['priority'] == target:
                    matches.append(item)

            show_matches(matches, f"No match found with {target} priority.")

        elif choice == 2:
            print("1. Completed tasks")
            print("2. Pending tasks")
            status_choice = input("Choose an option: ").strip()

            if status_choice == "1":
                target_status = True
            elif status_choice == "2":
                target_status = False
            else:
                print("Invalid input!")
                continue

            matches = []
            for item in tasks:
                if item['completed'] == target_status:
                    matches.append(item)

            show_matches(matches, "No matching tasks found.")

        elif choice == 3:
            print("1. Day")
            print("2. Month")
            print("3. Year")
            part_choice = input("Filter by which part? ").strip()

            if part_choice == "1":
                target_choice = input("Enter day (1-31): ").strip()
            elif part_choice == "2":
                target_choice = input("Enter month (1-12): ").strip()
            elif part_choice == "3":
                target_choice = input("Enter year: ").strip()
            else:
                print("Invalid option.")
                continue

            try:
                target = int(target_choice)
            except ValueError:
                print("Enter a valid number!")
                continue

            matches = []
            for item in tasks:
                try:
                    date = datetime.strptime(item["due_date"], "%d-%m-%Y")
                except ValueError:
                    continue

                if part_choice == "1" and date.day == target:
                    matches.append(item)
                elif part_choice == "2" and date.month == target:
                    matches.append(item)
                elif part_choice == "3" and date.year == target:
                    matches.append(item)

            show_matches(matches, "No matches found.")

        elif choice == 4:
            print("Returning to menu....")
            return

        else:
            print("Invalid option, choose between 1-4.")
