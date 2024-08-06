#Fazer rodar um audio aqui no python usando uma biblioteca para a criação de jogos 
#import pygame
#pygame.init()
#pygame.mixer.music.load(nome do arquivo copiado da ares de trabalho e colado neste projeto) loading da musica
#pygame.mixer.music.play() pra musica rolar
#ygame.event.wait() pra musica parar quando ela terminar
import tkinter as tk
def abrir_tela_loguin_vendedor():
    #Fecha a tela de boas vindas
    janela_boas_vindas.destroy()
def abrir_tela_acompanhamento_vendedor():
    pass

    #Criando a tela de loguin vendedor
janela_loguin_vendedor = tk.Tk()
janela_loguin_vendedor.title("CashAPP - Loguin vendedor")

    #Rotulo de boas vindas
    #tk.Label(Label é usar para criar rotulos ou melhor, passar uma informação)
rotulo_loguin_vendedor = tk.Label(janela_loguin_vendedor, text= "Faça seu loguin",font= ("Helvetica", 16))
rotulo_loguin_vendedor.pack(pady= 20)

    #Capo de entrada para o email do vandedor
    # width controla a largura do campo e show = "*" oculta uma informação que o usuário colocar 
entrada_email_vendedor = tk.Entry(janela_loguin_vendedor, width= 30)
entrada_email_vendedor.pack()

    #Campo de entrada para a senha do vendedor
entrada_senha_vendedor = tk.Entry(janela_loguin_vendedor, show= "*", width= 30)
entrada_senha_vendedor.pack()

    #Botão para fazer loguin como vendedor
botao_loguin_vendedor = tk.Button(janela_loguin_vendedor, text= "Loguin", command= lambda: janela_loguin_vendedor(entrada_email_vendedor.get(), entrada_senha_vendedor.get()))
botao_loguin_vendedor.pack()

    #Botão para cadastro vendedor
botao_cadastro_vendedor = tk.Button(janela_loguin_vendedor,text= "Cadastro (exbotão azul)" )
botao_cadastro_vendedor.pack()
janela_loguin_vendedor.mainloop