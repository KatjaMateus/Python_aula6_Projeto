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
    }
]
def adicionar_tarefas(new_task, desc, prioridade, categoria):    
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

def listar_tarefas(items):
    for item in listtasks:
        return items

def marcar_concluida(item):
    for item in listtasks:
        if item["tarefa"] == str(input("Digite o nome da tarefa procurada: ")):
            item["concluído"]=True
        return item

def procurar_tarefas(item):
    while True:
        escolha = int(input("""Escolha uma opção: 
                1 - Procurar pela prioridade 
                2 - Procurar pela categoria (DIÁRIA | SEMANAL)
                0 - Sair
                
        """))
        if escolha == 1:
            prioridade = input("Digite o nível de prioridade ((ALTA | MÉDIA | BAIXA): ")
            for item in listtasks:  
                if item["prioridade"]=="ALTA":  
                    return "Tarefas de prioridade ALTA são {item}"
                elif item["prioridade"]=="MÉDIA":
                    return "Tarefas de prioridade MÉDIA são {item}"
                elif item["prioridade"]=="BAIXA":
                    return "Tarefas de prioridade BAIXA são {item}"
                else:
                    "Opção inválida"
        elif escolha == 2:
            for item in listtasks:
                if item["categoria"] == "DIÁRIA":
                    return "Tarefas de categoria DIÁRIA são {item}"
                if item["categoria"] == "SEMANAL":
                    return "Tarefas de categoria SEMANAL são {item}"
                else:
                    "Opção inválida"
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
        print(adicionar_tarefas(new_task="tarefa", desc="descrição", prioridade="prioridade", categoria="categoria"))
    elif escolha == 2:
        print(listar_tarefas(listtasks))
    elif escolha == 3:
        print(marcar_concluida(listtasks))
    elif escolha == 4:
        print(procurar_tarefas(listtasks))
    elif escolha == 0:
        print("Programa encerrado")
        break



