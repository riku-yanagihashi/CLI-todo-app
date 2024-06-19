import json
import os
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

DB_FILE = "todos.json"
CONFIG_FILE = "config.json"
LANG_DIR = "languages"
LANG_FILE = "lang_en.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {"language": "en"}

def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def load_language():
    global LANG_FILE
    config = load_config()
    if config["language"] == "ja":
        LANG_FILE = "lang_ja.json"
    else:
        LANG_FILE = "lang_en.json"
    with open(os.path.join(LANG_DIR, LANG_FILE), "r") as file:
        return json.load(file)

LANG = load_language()

def load_todos():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(DB_FILE, "w") as file:
        json.dump(todos, file, indent=4)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print(Fore.GREEN + "\n" + "=" * 40)
    print(Fore.GREEN + " " + LANG["menu"]["title"])
    print("=" * 40)
    for option in LANG["menu"]["options"]:
        print(Fore.YELLOW + option)
    print(Fore.GREEN + "=" * 40 + "\n")

def add_todo():
    clear_screen()
    title = input(Fore.CYAN + LANG["messages"]["enter_title"]).strip()
    if not title:
        print(Fore.RED + LANG["messages"]["empty_title"])
        return
    content = input(Fore.CYAN + LANG["messages"]["enter_content"]).strip()
    priority = input(Fore.CYAN + LANG["messages"]["enter_priority"]).strip().lower()
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    deadline = input(Fore.CYAN + LANG["messages"]["enter_deadline"]).strip()
    todos = load_todos()
    todos.append(
        {
            "title": title,
            "content": content,
            "priority": priority,
            "date_time": date_time,
            "deadline": deadline,
            "done": False,
        }
    )
    save_todos(todos)
    print(Fore.GREEN + "\n" + LANG["messages"]["todo_added"] + "\n")

def view_todos():
    clear_screen()
    todos = load_todos()
    if not todos:
        print(Fore.YELLOW + "\n" + LANG["messages"]["no_todos"] + "\n")
        return
    print(Fore.GREEN + "\n" + LANG["messages"]["your_todos"])
    print(Fore.GREEN + "-" * 40)
    for index, todo in enumerate(todos, start=1):
        status = (
            Fore.RED + LANG["status"]["not_done"]
            if not todo.get("done", False)
            else Fore.GREEN + LANG["status"]["done"]
        )
        priority = todo.get("priority", "low")
        priority_marker = (
            Fore.GREEN + "●"
            if priority == "low" or priority == "l"
            else (
                Fore.YELLOW + "●"
                if priority == "medium" or priority == "mid" or priority == "m"
                else Fore.RED + "●" if priority == "high" or priority == "h" else "-"
            )
        )
        title = Fore.WHITE + todo.get("title", "No Title")
        date_time = Fore.WHITE + todo.get("date_time", "No Date")
        deadline = Fore.WHITE + todo.get("deadline", "No Deadline")
        print(Fore.CYAN + f"{index}. {status} {title} ({date_time}) {priority_marker} {deadline}")
    print(Fore.GREEN + "-" * 40 + "\n")

def update_todo():
    view_todos()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + LANG["messages"]["enter_number_update"])) - 1
        if 0 <= index < len(todos):
            title = input(Fore.CYAN + LANG["messages"]["enter_new_title"]).strip()
            content = input(Fore.CYAN + LANG["messages"]["enter_new_content"]).strip()
            priority = input(Fore.CYAN + LANG["messages"]["enter_new_priority"]).strip()
            deadline = input(Fore.CYAN + LANG["messages"]["enter_new_deadline"]).strip()
            status = input(Fore.CYAN + LANG["messages"]["is_done"]).strip().lower()

            if title:
                todos[index]["title"] = title
            if content:
                todos[index]["content"] = content
            if priority:
                todos[index]["priority"] = priority
            if deadline:
                todos[index]["deadline"] = deadline
            if status:
                todos[index]["done"] = status == "yes"

            todos[index]["date_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_todos(todos)
            print(Fore.GREEN + "\n" + LANG["messages"]["todo_updated"] + "\n")
        else:
            print(Fore.RED + "\n" + LANG["messages"]["invalid_number"] + "\n")
    except ValueError:
        print(Fore.RED + "\n" + LANG["messages"]["invalid_input"] + "\n")

def delete_todo():
    clear_screen()
    view_todos()
    todos = load_todos()
    if not todos:
        return
    try:
        index = int(input(Fore.CYAN + LANG["messages"]["enter_number_delete"])) - 1
        if 0 <= index < len(todos):
            todos.pop(index)
            save_todos(todos)
            print(Fore.GREEN + "\n" + LANG["messages"]["todo_deleted"] + "\n")
        else:
            print(Fore.RED + "\n" + LANG["messages"]["invalid_number"] + "\n")
    except ValueError:
        print(Fore.RED + "\n" + LANG["messages"]["invalid_input"] + "\n")

def export_todos():
    todos = load_todos()
    if not todos:
        print(Fore.YELLOW + "\n" + LANG["messages"]["no_todos"] + "\n")
        return

    with open("todos_export.md", "w") as file:
        file.write("# To-Do List\n\n")
        for todo in todos:
            file.write(f"## {todo['title']}\n")
            file.write(f"- Content: {todo['content']}\n")
            file.write(f"- Priority: {todo['priority']}\n")
            file.write(f"- Date: {todo['date_time']}\n")
            deadline = todo.get('deadline', 'No Deadline')
            file.write(f"- Deadline: {deadline}\n")
            file.write(f"- Status: {'Done' if todo['done'] else 'Not Done'}\n")
            file.write("\n")
    print(Fore.GREEN + "\n" + LANG["messages"]["todos_exported"] + "\n")

def search_todos():
    clear_screen()
    query = input(Fore.CYAN + LANG["messages"]["enter_search_query"]).strip().lower()
    todos = load_todos()
    if not query:
        print(Fore.RED + LANG["messages"]["empty_search_query"])
        return

    matching_todos = [
        todo for todo in todos
        if query in todo["title"].lower() or query in todo["content"].lower()
    ]

    if not matching_todos:
        print(Fore.YELLOW + "\n" + LANG["messages"]["no_matching_todos"] + "\n")
        return

    print(Fore.GREEN + "\n" + LANG["messages"]["matching_todos"])
    print(Fore.GREEN + "-" * 40)
    for index, todo in enumerate(matching_todos, start=1):
        status = (
            Fore.RED + LANG["status"]["not_done"]
            if not todo.get("done", False)
            else Fore.GREEN + LANG["status"]["done"]
        )
        priority = todo.get("priority", "low")
        priority_marker = (
            Fore.GREEN + "●"
            if priority == "low" or priority == "l"
            else (
                Fore.YELLOW + "●"
                if priority == "medium" or priority == "mid" or priority == "m"
                else Fore.RED + "●" if priority == "high" or priority == "h" else "-"
            )
        )
        title = Fore.WHITE + todo.get("title", "No Title")
        date_time = Fore.WHITE + todo.get("date_time", "No Date")
        deadline = Fore.WHITE + todo.get("deadline", "No Deadline")
        print(Fore.CYAN + f"{index}. {status} {title} ({date_time}) {priority_marker} {deadline}")
    print(Fore.GREEN + "-" * 40 + "\n")

def help():
    clear_screen()
    help_text = """
    コマンド一覧:
    1. add (a)      - タスクを追加します
    2. view (v)     - タスク一覧を表示します
    3. update (u)   - タスクを更新します
    4. delete (d)   - タスクを削除します
    5. export (e)   - タスクをエクスポートします
    6. search (s)   - タスクを検索します
    7. exit (x)     - プログラムを終了します
    ?, help         - このヘルプメッセージを表示します
    """
    print(Fore.YELLOW + help_text)

def main():
    while True:
        display_menu()
        choice = input(Fore.CYAN + LANG["menu"]["prompt"]).strip().lower()
        if choice in ["1", "add", "a"]:
            add_todo()
        elif choice in ["2", "view", "v"]:
            view_todos()
            input(Fore.CYAN + LANG["messages"]["press_enter_to_continue"])
        elif choice in ["3", "update", "u"]:
            update_todo()
        elif choice in ["4", "delete", "d"]:
            delete_todo()
        elif choice in ["5", "export", "e"]:
            export_todos()
        elif choice in ["6", "search", "s"]:
            search_todos()
            input(Fore.CYAN + LANG["messages"]["press_enter_to_continue"])
        elif choice in ["7", "exit", "x"]:
            print(Fore.GREEN + "\n" + LANG["messages"]["goodbye"] + "\n")
            break
        elif choice in ["?", "help"]:
            help()
        else:
            print(Fore.RED + "\n" + LANG["messages"]["invalid_choice"] + "\n")

if __name__ == "__main__":
    main()
