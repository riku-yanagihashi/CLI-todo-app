import json
import os
from colorama import init, Fore, Style

init(autoreset=True)

DB_FILE = 'todos.json'

def load_todos():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(DB_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def display_menu():
    print(Fore.GREEN + "\n" + "="*40)
    print(Fore.GREEN + " What would you like to do?")
    print("="*40)
    print(Fore.YELLOW + "1. Add Todo")
    print(Fore.YELLOW + "2. View Todos")
    print(Fore.YELLOW + "3. Update Todo")
    print(Fore.YELLOW + "4. Delete Todo")
    print(Fore.YELLOW + "5. Exit")
    print(Fore.GREEN + "="*40 + "\n")

def add_todo():
    task = input(Fore.CYAN + "Enter the task: ")
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(Fore.GREEN + "\nTodo added successfully!\n")

def view_todos():
    todos = load_todos()
    if not todos:
        print(Fore.YELLOW + "\nNo todos found!\n")
        return
    print(Fore.GREEN + "\nYour Todos:")
    print(Fore.GREEN + "-"*40)
    for index, todo in enumerate(todos, start=1):
        status = Fore.RED + "✘" if not todo["done"] else Fore.GREEN + "✔"
        print(Fore.CYAN + f"{index}. {status} {todo['task']}")
    print(Fore.GREEN + "-"*40 + "\n")

def update_todo():
    view_todos()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + "Enter the number of the todo to update: ")) - 1
        if 0 <= index < len(todos):
            todos[index]["task"] = input(Fore.CYAN + "Enter the new task: ")
            status = input(Fore.CYAN + "Is it done? (yes/no): ").strip().lower()
            todos[index]["done"] = status == "yes"
            save_todos(todos)
            print(Fore.GREEN + "\nTodo updated successfully!\n")
        else:
            print(Fore.RED + "\nInvalid number!\n")
    except ValueError:
        print(Fore.RED + "\nInvalid input!\n")

def delete_todo():
    view_todos()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + "Enter the number of the todo to delete: ")) - 1
        if 0 <= index < len(todos):
            todos.pop(index)
            save_todos(todos)
            print(Fore.GREEN + "\nTodo deleted successfully!\n")
        else:
            print(Fore.RED + "\nInvalid number!\n")
    except ValueError:
        print(Fore.RED + "\nInvalid input!\n")

def main():
    while True:
        display_menu()
        choice = input(Fore.CYAN + "Enter your choice: ").strip().lower()
        if choice in ['1', 'add', 'a']:
            add_todo()
        elif choice in ['2', 'view', 'v']:
            view_todos()
        elif choice in ['3', 'update', 'u']:
            update_todo()
        elif choice in ['4', 'delete', 'd']:
            delete_todo()
        elif choice in ['5', 'exit', 'e']:
            print(Fore.GREEN + "\nGoodbye!\n")
            break
        else:
            print(Fore.RED + "\nInvalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
