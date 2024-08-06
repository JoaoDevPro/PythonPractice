tarefas = {
    "Construir casa": {
        "Preparação do terreno": {
            "limpeza do terreno": None,
            "Escavação": None,
        },
        "fundação": {
            "desenho da fundação": None,
            "Escavação da fundação": None,
            "Concretagem da fundação": None,
        },
        "Estrutura": {
            "Paredes externas": None,
            "Paredes internas": None,
            "Telhado": None,
        },
        "Encanamento": {
            "Instalação de encanamento": None,
            "Teste de pressão da tubulação": None,
        },
        "Instalações elétricas": {
            "Fiação elétrica": None,
            "Painel de distribuição": None,
        },
        "Acabamento": {
            "Pintura": None,
            "Revestimentos de pisos": None,
            "Instalação de portas e janelas": None,
        },
        "Inspeções e testes": {
            "Inspeção final": None,
            "Teste de Qualidade de água": None,
        },
        "Limpeza e preparação para mudança": {
            "Limpeza geral": None,
            "Paisagismo": None,
        }
    }
}

def adicionar_tarefa(arvore, tarefa_pai, nova_tarefa, sub_tarefas=None):
    if sub_tarefas is None:
        sub_tarefas = {}
    if tarefa_pai in arvore:
        arvore[tarefa_pai][nova_tarefa] = sub_tarefas
    else:
        print(f"A tarefa '{tarefa_pai}' não existe na árvore de tarefas.")
        return

def atribuir_responsavel(arvore, tarefa_pai, tarefa, responsavel):
    if tarefa_pai in arvore and tarefa in arvore[tarefa_pai]:
        if "responsavel" in arvore[tarefa_pai][tarefa]:
            arvore[tarefa_pai][tarefa]["responsavel"].append(responsavel)
        else:
            arvore[tarefa_pai][tarefa]["responsavel"] = [responsavel]
    else:
        print(f"A tarefa '{tarefa}' não existe na árvore de tarefas de '{tarefa_pai}'.")

def definir_prazo(arvore, tarefa_pai, tarefa, prazo):
    if tarefa_pai in arvore and tarefa in arvore[tarefa_pai]:
        arvore[tarefa_pai][tarefa]["prazo"] = prazo
    else:
        print(f"A tarefa '{tarefa}' não existe na árvore de tarefas de '{tarefa_pai}'.")

def listar_tarefas(arvore, tarefa_pai, nivel=0):
    if tarefa_pai in arvore:
        for tarefa, info in arvore[tarefa_pai].items():
            if isinstance(info, dict):
                responsavel = info.get("responsavel", "N/A")
                prazo = info.get("prazo", "N/A")
                concluida = info.get("Concluida", False)
                status = "concluida" if concluida else "pendente"
                print(tarefa)
                print("  " * nivel + f"Responsável: {responsavel}")
                print("  " * nivel + f"Prazo: {prazo}")
                print("  " * nivel + f"Status: {status}")
                print('')
                listar_tarefas(arvore[tarefa_pai], tarefa, nivel + 1)

# Exemplo de uso
adicionar_tarefa(tarefas, "Construir casa", "Preparação do terreno")
adicionar_tarefa(tarefas, "Construir casa", "fundação")
adicionar_tarefa(tarefas, "Construir casa", "Estrutura")
adicionar_tarefa(tarefas, "Construir casa", "Encanamento")
adicionar_tarefa(tarefas, "Construir casa", "Instalações elétricas")
adicionar_tarefa(tarefas, "Construir casa", "Acabamento")
adicionar_tarefa(tarefas, "Construir casa", "Inspeções e testes")
adicionar_tarefa(tarefas, "Construir casa", "Limpeza e preparação para mudança")

atribuir_responsavel(tarefas, "Construir casa", "Preparação do terreno", "Murilo")
atribuir_responsavel(tarefas, "Construir casa", "fundação", "Julio")
atribuir_responsavel(tarefas, "Construir casa", "Estrutura", "Davi")
atribuir_responsavel(tarefas, "Construir casa", "Encanamento", "Bernardo")
atribuir_responsavel(tarefas, "Construir casa", "Instalações elétricas", "Gustavo")
atribuir_responsavel(tarefas, "Construir casa", "Acabamento", "Matias")
atribuir_responsavel(tarefas, "Construir casa", "Inspeções e testes", "Natasha")
atribuir_responsavel(tarefas, "Construir casa", "Limpeza e preparação para mudança", "João")

definir_prazo(tarefas, "Construir casa", "Preparação do terreno", "2023-10-29")
definir_prazo(tarefas, "Construir casa", "fundação", "2023-11-05")
definir_prazo(tarefas, "Construir casa", "Estrutura", "2023-11-10")
definir_prazo(tarefas, "Construir casa", "Encanamento", "2024-01-10")
definir_prazo(tarefas, "Construir casa", "Instalações elétricas", "2024-01-17")
definir_prazo(tarefas, "Construir casa", "Acabamento", "2024-01-27")
definir_prazo(tarefas, "Construir casa", "Inspeções e testes", "2024-01-30")
definir_prazo(tarefas, "Construir casa", "Limpeza e preparação para mudança", "2024-02-02")


listar_tarefas(subtarefas, "Construir casa")




    




























