# from functions import get_todos, write_todos
from modules import functions
import time

# print(older_version)
# input(help(get_todos))

FILENAME = "todos.txt"

now = time.strftime("%b %d - %Y %H:%m:%S")
print("It's", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        # todos.sort()

        todos = functions.get_todos(FILENAME)

        for i, item in enumerate(todos):
            print(f'{i + 1}-->  {item.title()}')

    elif user_action.startswith('edit'):
        try:
            item = int(user_action[5:])
            item -= 1

            todos = functions.get_todos()

            todos[item] = input('Enter: ') + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            item = int(user_action[9:])

            todos = functions.get_todos()
            i = item - 1
            todo_to_remove = todos[i].strip("\n")
            todos.pop(i)

            functions.write_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed successfully.")
        except IndexError:
            print('theres no item with that number!')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Enter a valid command.")

print('good luck !')
