import json

todos=[]

all_marked_flag = False

def add_todo(text):
    todo = {"text": text, "is_done": False, "number": len(todos) + 1}
    todos.append(todo)
    return todo

def update_todos_is_done(number):
    todo = todos[number]
    todo["is_done"] = not todo["is_done"]
    return todo

def strike(text):
    i = 0
    new_text = ''
    while i < len(text):
        new_text = new_text + (text[i] + u'\u0336')
        i = i + 1
    return(new_text)

def strike_todo(todo):
    return strike(todo["text"]) if todo["is_done"] else todo["text"]

def yes_no_todo_choice(number, todo, action):
    y = input(f' You want to add one more? (y/n) ')
    return y in ('Y', 'y')

def update_todo_text(number, text):
    todo = todos[number]
    todo["text"] = text
    return todo

def delete_todo(number):
    todo = todos.pop(number)
    return todo

def print_delete_todos():
    while len(todos):
        print_todos()
        number = input('print number of task you want to delete: ')
        number = int(number)
        todo = delete_todo(number - 1)
        if not yes_no_todo_choice(number, todo, 'delete'):
            break
    return True

def print_todos():
    i = 1
    print('list of tasks:')
    for todo in todos:
        print(f'{i}. {strike_todo(todo)}')
        i += 1
    return True

def print_add_todos():
    while True:
        print_todos()
        text = input('Enter new todo - ')
        todo = add_todo(text)
        if not yes_no_todo_choice(len(todos), todo, 'add'):
            break
    return True

def print_todos():
    # for i, todo in enumerate(todos):
    i = 1
    print('Todo list:')
    for todo in todos:
        print(f'{i}. {strike_todo(todo)}')
        i += 1
    return True

def print_update_todos_text():
    while True:
        print_todos()
        number = input('print number you want to change: ')
        number = int(number)
        text = input('print text of new todo: ')
        todo = update_todo_text(number - 1, text)
        if not yes_no_todo_choice(number, todo, 'delete'):
            break
    return True
    
def print_update_todos_is_done():
    while True:
        print_todos()
        number = input('print number of todo you want to mark: ')
        number = int(number)
        todo = update_todos_is_done(number - 1)
        if not yes_no_todo_choice(number, todo, 'mark'):
            break
    return True

def all_marked(is_done=True):
    global todos
    todos = list(map(lambda x: dict(x, **{"is_done": is_done}), todos))
    print('all marked todos', todos)
    return True

def print_all_marked():
    global all_marked_flag
    all_marked_flag = not all_marked_flag
    all_marked(all_marked_flag)
    print('print all marked', todos)
    return True

def filter(is_done=True):
    return list(filter(lambda x: x["is_done"] == is_done, todos))

def print_filter():
    text = input('Do you want to see done tasks? (y/n) - ')
    print_todos(filter(text.lower() in ('y', 'yes')))
    return True

def search(text):
    return list(filter(lambda x: text.lower() in x["text"].lower(), todos))

def print_search():
    text = input('Enter key for search - ')
    print_todos(search(text))
    return True

def read(file_name):
    file = open(file_name)
    data = json.loads(file.read())
    file.close()
    global todos

def read_file():
    file_name = input('enter file name: ')
    read(file_name)

def write(file_name):
    file = open(file_name, 'w')
    file.write(json.dumps(todos))
    file.close()

def write_file():
    file_name = input('enter file name: ')
    write(file_name)

def todos_exit():
    y = input('Are you sure you want to exit? (y/n) ')
    if y in ('y', 'Y'):
        exit()

choices = {
    "1": print_add_todos,
    "2": print_todos,
    "3": print_update_todos_text,
    "4": print_update_todos_is_done,
    "5": print_all_marked,
    "6": print_delete_todos,
    "7": print_filter,
    "8": read_file,
    "9": write_file,
    "10": print_search,
    "0": todos_exit
}

menu = """
1. add new todo
2. show todos
3. update todos
4. mark todo
5. mark all
6. delete todo
7. show marked tasks
8. read file
9. write file
10. search by text
0. exit
"""

while True:
    menu_number = input(menu)
    choice = choices.get(menu_number)
    if not choice:
        print('you enter invalid number, please try again')
        continue
    choice()
