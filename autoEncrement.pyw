import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import pyautogui
import time
import os

# Configurações da tela do programa
window = tk.Tk()
window.title("AutoEncremente Version 4")
window.geometry("800x600")
window.resizable(False, False)

# Definindo cores
background_color = "black"
text_color = "#49DB40"

# Criando a tela de console
console = tk.Text(
    window,
    state="disabled",
    width=97,
    height=30,
    background=background_color,
    foreground=text_color,
)
console.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

# Lista para armazenar o conteúdo do arquivo
conteudo = []
lista = []
timeInit = 8
separator = ";"

# Função para imprimir informações na tela de console
def log(msg):
    console.config(state="normal")
    console.insert(tk.END, msg + "\n")
    console.config(state="disabled")
    console.see(tk.END)

def openConfig():
    global timeInit
    global separator
    global config  # Tornando config uma variável global

    # Função para atualizar as configurações
    def update():
        # Objetos globais
        global timeInit
        global separator

        # Atualizando valores dos objetos globais
        valueTimerInit = TimerInit.get()
        valueSeparator = separator_entry.get()
        timeInit = int(valueTimerInit)
        separator = valueSeparator
        log("Aplicando configurações")
        config.destroy()
        time.sleep(1.5)
        log("Configurações Atualizadas")


    # Configuração da tela de configurações
    config = tk.Toplevel(window)
    config.title("Configurações")
    config.geometry("400x200")
    config.resizable(False, False)

    # Labels e campos de entrada
    tk.Label(config, text="Separador:").grid(row=0, column=0, padx=10, pady=10)
    separator_entry = tk.Entry(config, width=10)
    separator_entry.grid(row=0, column=1, padx=10, pady=10)
    separator_entry.insert(0, separator)

    tk.Label(config, text="Tempo de Inicialização:").grid(row=1, column=0, padx=10, pady=10)
    TimerInit = tk.Spinbox(config, width=10)
    TimerInit.grid(row=1, column=1, padx=10, pady=10)
    TimerInit.delete(0, tk.END)
    TimerInit.insert(0, timeInit)

    # Botões das configurações
    aplica = tk.Button(config, text="Aplicar", width=10, height=2, command=update)
    aplica.grid(row=2, column=0, padx=10, pady=10)

    # Impedir que a janela principal seja usada enquanto a janela de configurações estiver aberta
    config.grab_set()

def FsearchFile():
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo com o nome dos arquivos",
        filetypes=(("Arquivos .txt", "*.txt"), ("Todos os arquivos", "*.*")),
    )
    filebydirectory.delete(0, tk.END)
    filebydirectory.insert(0, arquivo)
    log("Arquivo selecionado: " + arquivo)
    arquivo = filebydirectory.get()

    try:
        with open(arquivo, "r") as f:
            conteudo = f.read()
            log(arquivo)
            lista.extend(conteudo.split(separator))

    except Exception as e:
        log("Erro ao ler o arquivo " + str(e))
        messagebox.showerror("ERRO", "Não foi possível ler o arquivo!")


def to_write():
    # Timer de tempoInicial segundos para iniciar a função do array
    time.sleep(timeInit)

    # Repete a função enquanto tiver itens no array
    for item in lista:
        pyautogui.typewrite(item.strip())
        pyautogui.press("enter")
        time.sleep(0.1)

    # Confirmação de termino do programa
    log("A lista de itens " + str(lista) + " foi digitada corretamente")


# Campo de entrada do diretório do arquivo
filebydirectory = tk.Entry(window, width=95, borderwidth=2)
filebydirectory.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# Adicionando um help para o usuário
log("\ Cada item deve ser separado por ponto e vírgula para um perfeito funcionamento!! /")
log("\ ------------------------------------------------------------------------------- /")

# Lista de botões na tela do programa

searchFile = tk.Button(window, text="Buscar arquivo", width=20, command=FsearchFile)
searchFile.grid(row=0, column=2, padx=5, pady=5)

writeButton = tk.Button(window, text="Escrever conteúdo", width=20, command=to_write)
writeButton.grid(row=3, column=1, padx=3, pady=3)

exitButton = tk.Button(window, text="Configurações", width=20, command=openConfig)
exitButton.grid(row=3, column=2, padx=5, pady=5)

# Estilização
window.configure(background=background_color)
console.configure(font=("Courier", 10), insertbackground=text_color)
searchFile.configure(bg=background_color, fg=text_color)
writeButton.configure(bg=background_color, fg=text_color)
exitButton.configure(bg=background_color, fg=text_color)

# Botões de verificação do sistema
# verific = tk.Button(window, text="Verificar", command=lambda: print("Tempo de Inicialização: ", timeInit, " Separador utilizado é ", separator))
# verific.grid(row=3, column=0, padx=3, pady=5)
# verific.configure(bg=background_color, fg=text_color)

window.mainloop()
