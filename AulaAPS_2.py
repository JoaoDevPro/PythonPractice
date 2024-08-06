from datetime import datetime

# Função para calcular o status com base na data de prazo
def calcular_status(prazo):
    hoje = datetime.today()
    if prazo is None:
        return "Pendente"
    elif prazo < hoje:
        return "Atrasado"
    else:
        return "Realizado"

# Função para mostrar informações de uma atividade
def mostrar_informacoes(subatividade):
    prazo = tarefas.get(subatividade)
    status = calcular_status(prazo)
    print(f"Subatividade: {subatividade}")
    print(f"Responsável: [João]")
    print(f"Prazo: {prazo}")
    print(f"Status: {status}")
    print("")


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

subatividade = input("Digite a atividade: ").lower()

if subatividade in tarefas["Construir casa"]:
    print(f"Informações da subatividade: {subatividade}")
    mostrar_informacoes(subatividade)
else:
    print("Subatividade não encontrada no grafo de tarefas da atividade principal 'Construir casa'.")

import tkinter as tk
tela_interativa = tk.Tk()
tela_interativa.geometry("250x300")
rotulo = tk.Label(tela_interativa, text= "Selecione a atividade que deseja para ver mais  informações", font=("Helvetica", 16))
rotulo.pack(pady=20)

atividade = tk.Button(text= "Buscar informações")
atividade.pack(pady=200)




rotulo.pack(pady=20)


tela_interativa.mainloop()
