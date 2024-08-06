import tkinter as tk
from tkinter import simpledialog

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
    info_text = f"Subatividade: {subatividade}\n" \
                f"Responsável: [João]\n" \
                f"Prazo: {prazo}\n" \
                f"Status: {status}"
    resultado_label.config(text=info_text)

# Função para lidar com a seleção de atividade
def selecionar_atividade():
    subatividade = simpledialog.askstring("Atividade", "Digite a subatividade que deseja ver:")
    if subatividade in tarefas["Construir casa"]:
        resultado_label.config(text="Informações da subatividade:")
        mostrar_informacoes(subatividade)
    else:
        resultado_label.config(text="Subatividade não encontrada no grafo de tarefas da atividade principal 'Construir casa'.")

tarefas = {
    # ... (seu dicionário de tarefas)
}

# Criar a janela
tela_interativa = tk.Tk()
tela_interativa.geometry("400x300")
tela_interativa.title("Aplicativo de Tarefas")

# Criar um rótulo de boas-vindas
boas_vindas_label = tk.Label(tela_interativa, text="Bem-vindo ao Aplicativo de Tarefas", font=("Helvetica", 16))
boas_vindas_label.pack(pady=20)

# Botão para selecionar a atividade
atividade_button = tk.Button(tela_interativa, text="Selecionar Atividade", command=selecionar_atividade)
atividade_button.pack(pady=20)

# Rótulo para mostrar informações da atividade selecionada
resultado_label = tk.Label(tela_interativa, text="", font=("Helvetica", 14))
resultado_label.pack()

tela_interativa.mainloop()

