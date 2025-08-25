# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


def add_todo_task(todo_task, todo=None):
    if todo is None:
        todo = []
    todo.append(todo_task)
    return todo


def get_todo(todo=None):
    if todo is None:
        todo = []
    return todo


def show_todo(todo=None):
    print("LISTA DE TAREFAS \n")
    if todo is None:
        todo = []
    for item in todo:
        print(item)
    print()


def app():
    commands = ("fazer", "listar", "refazer")
    is_running = True
    result = []
    done = []
    while is_running:
        todo = get_todo(result)
        print("comandos:", *commands)
        command = input("digite uma tarefa ou comando: ")
        command = command.split()
        if command[0] == "listar":
            show_todo(todo)
        if command[0] == "fazer":
            print("Tarefa concluída")
            todo_task = " ".join(command[1:])
            if todo_task in todo:
                done.append(todo_task)
                todo.remove(todo_task)
        if command[0] == "refazer":
            todo_task = " ".join(command[1:])
            if todo_task in done:
                print(f"Refazendo {todo_task}")
                done.remove(todo_task)
                todo.append(todo_task)
        if command[0] not in commands:
            print("Tarefa adicionada")
            command = " ".join(command)
            result = add_todo_task(command, todo)
        if command[0] == "quit":
            is_running = False


if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        print("Operação encerrada manualmente.")
    except EOFError:
        print("Operação encerrada manualmente.")
