import functions as fnc
from random import randint

print("""
    [ 1 ] Adicionar task
    [ 2 ] Editar task
    [ 3 ] Editor membro
    [ 4 ] Editar prazo
    [ 5 ] Deletar task
""")
option = input()

if option == "1":
    task = input("Qual é a tarefa?: ")
    member = input('Essa tarefa é para qual membro da equipe?: ')
    fnc.addTask(task, member)
elif option == "2":
    oldTask = input("Qual tarefa editar?: ")
    newTask = input("Qual o nome da nova tarefa?: ")
    fnc.editTask(oldTask, newTask)
elif option == "3":
    task = input("Qual tarefa excluir?: ")
    fnc.delTask(task)
else:
    print("Digito inválido")

