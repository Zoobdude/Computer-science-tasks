#Holiday check list

get_holiday_destintion = input("Where are you going on holiday? ")

check_list = {}


try:
    with open(f"{get_holiday_destintion}.txt", "r") as file:
        for line in file:
            line = line.strip()
            try:
                task, status = line.split(":")
            except ValueError:
                task = line
                status = "False"
            check_list[task] = True if status == "True" else False


except FileNotFoundError:
    with open(f"{get_holiday_destintion}.txt", "w") as file:
        file.write("")

print(f"Check list for {get_holiday_destintion}")
for task in check_list:
    print(f"{task} [{'/' if check_list[task] else 'x'}]")

while True:
    action_input = input("What would you like to do? (add, remove, mark, unmark, quit) ")
    if action_input == "add":
        new_task = input("What task would you like to add? ")
        check_list[new_task] = False
    elif action_input == "remove":
        remove_task = input("What task would you like to remove? ")
        del check_list[remove_task]
    elif action_input == "mark":
        mark_task = input("What task would you like to mark as complete? ")
        check_list[mark_task] = True
    elif action_input == "unmark":
        unmark_task = input("What task would you like to unmark? ")
        check_list[unmark_task] = False
    elif action_input == "quit":
        with open(f"{get_holiday_destintion}.txt", "w") as file:
            for task in check_list:
                file.write(f"{task}:{check_list[task]}\n")
            exit()