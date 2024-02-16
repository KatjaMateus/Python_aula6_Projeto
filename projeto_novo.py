listtasks = [
    {
    "tarefa" : "passear com Kiko", 
    "descrição" : "levar o cachorro para praia", 
    "prioridade" : "média", 
    "categoria" : "semanal",
    "concluído" : False
    },
    {"tarefa" : "lavar louça", 
    "descrição" : "lavar louça após cada refeição", 
    "prioridade" : "alta", 
    "categoria" : "diária",
    "concluído" : False
    },
    {"tarefa" : "louça", 
    "descrição" : "lavar louça após cada refeição", 
    "prioridade" : "alta", 
    "categoria" : "diária",
    "concluído" : False
    }
]
def adicionar_tarefas():    
    new_task = str(input("Digite o nome da tarefa: "))
    desc = str(input("Digite a descrição da tarefa: "))
    prioridade = str(input("Digite o nível de prioridade: "))
    categoria = str(input("Digite a letra de categoria: "))

    dictionary = {
        "tarefa" : new_task, 
        "descrição" : desc, 
        "prioridade" : prioridade, 
        "categoria" : categoria,
        "concluído" : False
    }
    return listtasks.append(dictionary)

def listar_tarefas():
    for item in listtasks:
        print(item)

def marcar_concluida():
    nameTask = str(input("Digite o nome da tarefa procurada: "))
    for item in listtasks:
        if item["tarefa"] == nameTask:
            item["concluído"]=True
            return item

def procurar_tarefas():
    while True:
        escolha = int(input("""Escolha uma opção: 
                1 - Procurar pela prioridade 
                2 - Procurar pela categoria (DIÁRIA | SEMANAL)
                0 - Sair
                
        """))
        if escolha == 1:
            prioridade = input("Digite o nível de prioridade ((ALTA | MÉDIA | BAIXA): ")
            for item in listtasks:  
                if item["prioridade"]==prioridade.lower():  
                    print(f"Tarefas de prioridade {prioridade} são {item}")
        elif escolha == 2:
            categoria = input("Digite a categoria (DIÁRIA | SEMANAL): ")
            for item in listtasks:
                if item["categoria"] == categoria.lower():
                    print(f"Tarefas de categoria {categoria} são {item}")
        elif escolha == 0:
            break

while True:
    escolha = int(input("""Escolha uma opção:
            1 - Adicionar tarefa
            2 - Listar tarefas
            3 - Marcar como concluída
            4 - Visualizar por prioridade ou categoria
            0 - Sair
    """))
    if escolha == 1:
        adicionar_tarefas()
    elif escolha == 2:
        listar_tarefas()
    elif escolha == 3:
        print(marcar_concluida())
    elif escolha == 4:
        procurar_tarefas()
    elif escolha == 0:
        print("Programa encerrado")
        break

