import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import winsound
import pyautogui
import time
import os
import socket
import webbrowser

# Configurações da tela do programa
window = tk.Tk()
window.title("AutoEncremente")
window.geometry("800x600")
window.resizable(False, False)

# Define o ícone da janela
icon_path = "config/AutoEncrement.ico"
window.iconbitmap(default=icon_path)

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

# Link para update do programa
def openBrowserUpdate():
    url = "https://github.com/Ernan21/AutoEncrement"
    webbrowser.open(url)

# Lista para armazenar o conteúdo do arquivo
conteudo = []
lista = []
timeInit = 5
separator = ";"
itensTime = 0.1
reapeat = 1
frasepadrao = ""

# Pegando nome de usuario
username = os.getlogin()
ip_local = socket.gethostbyname(socket.gethostname())

# Função para imprimir informações na tela de console
def log(msg):
    console.config(state="normal")
    console.insert(tk.END, msg + "\n")
    console.config(state="disabled")
    console.see(tk.END)

def openConfig():
    global timeInit, separator, itensTime, config, frasepadrao

    # Função para atualizar as configurações
    def update():
        # Objetos globais
        
        global timeInit, separator, itensTime, config, reapeat, frasepadrao

        # Atualizando valores dos objetos globais
        valueTimerInit = TimerInit.get()
        valueSeparator = separator_entry.get()
        timeInit = int(valueTimerInit)
        separator = valueSeparator
        valueReapeat = reapeatVezes.get()
        reapeat = int(valueReapeat)
        valueItensTime = timerItens.get()
        itensTime = float(valueItensTime)
        frasepadrao = valuefrasepadrao.get()
        
        log("Aplicando configurações")
        config.destroy()
        time.sleep(0.5)
        log("Configurações Atualizadas")


    # Configuração da tela de configurações
    config = tk.Toplevel(window)
    config.title("Configurações")
    config.geometry("830x400")
    config.resizable(False, False)

    # Estilização da tela de configurações
    config.configure(background=background_color)


    def validate_separator_input(*args):
        separator = separator_entry.get()
        if len(separator) > 1:
            separator_entry.set(separator[:1])

    tk.Label(config, text="Separador:", fg=text_color, bg=background_color).grid(row=0, column=0, padx=10, pady=10)
    separator_entry = tk.StringVar()
    separator_entry.trace('w', validate_separator_input)
    separator_entry.set(separator)
    separator_entry_widget = tk.Entry(config, width=10, textvariable=separator_entry)
    separator_entry_widget.grid(row=0, column=1, padx=10, pady=10)


    tk.Label(config, text="Tempo de Inicialização:", fg=text_color, bg=background_color).grid(row=1, column=0, padx=10, pady=10)
    TimerInit = tk.Spinbox(config, width=10)
    TimerInit.grid(row=1, column=1, padx=10, pady=10)
    TimerInit.delete(0, tk.END)
    TimerInit.insert(0, timeInit)
    
    tk.Label(config, text="Vezes", fg=text_color, bg=background_color).grid(row=2, column=0, padx=10, pady=10)
    reapeatVezes = tk.Spinbox(config, width=10)
    reapeatVezes.grid(row=2, column=1, padx=10, pady=10)
    reapeatVezes.delete(0, tk.END)
    reapeatVezes.insert(0, reapeat)
    
    tk.Label(config, text="Tempo Entre itens", fg=text_color, bg=background_color).grid(row=3, column=0, padx=10, pady=10)
    timerItens = tk.Spinbox(config, width=10)
    timerItens.grid(row=3, column=1, padx=10, pady=10)
    timerItens.delete(0, tk.END)
    timerItens.insert(0, itensTime)
    
    tk.Label(config, text="Texto padrão para ser adicionado entre os separadores", fg=text_color, bg=background_color).grid(row=4, column=0, padx=10, pady=10)
    valuefrasepadrao = tk.Entry(config, width=100)
    valuefrasepadrao.grid(row=5, column=0, padx=10, pady=10)
    valuefrasepadrao.delete(0, tk.END)
    valuefrasepadrao.insert(0 ,frasepadrao)
    
    # Botões das configurações
    Salvar = tk.Button(config, text="Salvar", width=10, height=2, command=update)
    Salvar.grid(row=10, column=1, padx=10, pady=10)
    Salvar.configure(bg=background_color, fg=text_color)

    Sair = tk.Button(config, text="Sair", width=10, height=2, command=config.destroy)
    Sair.grid(row=10, column=2, padx=10, pady=10)
    Sair.configure(bg=background_color, fg=text_color)
    
    def on_closing():
        if messagebox.askokcancel("Aviso", "Ao sair, as configurações feitas não serão aplicadas"):
            config.destroy()
    config.protocol("WM_DELETE_WINDOW", on_closing)

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
    # Quantas vezes o codigo ira se repetir
    for i in range(reapeat):
    # Repete a função enquanto tiver itens no array
        for item in lista:
            pyautogui.typewrite(frasepadrao)
            pyautogui.typewrite(item.strip())
            pyautogui.press("enter")
            time.sleep(itensTime)
    # Confirmação de termino do programa
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    log("A lista de itens " + str(lista) + " foi digitada corretamente")


# Campo de entrada do diretório do arquivo
filebydirectory = tk.Entry(window, width=95, borderwidth=2)
filebydirectory.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# Adicionando um help para o usuário
log("\ Cada item deve ser separado por '" + separator + "' para um perfeito funcionamento!! /")
log("\ ------------------------------------------------------------------- /")

# Lista de botões na tela do programa

searchFile = tk.Button(window, text="Buscar arquivo", width=20, command=FsearchFile)
searchFile.grid(row=0, column=2, padx=5, pady=5)

writeButton = tk.Button(window, text="Escrever conteúdo", width=20, command=to_write)
writeButton.grid(row=3, column=1, padx=3, pady=3)

exitButton = tk.Button(window, text="Configurações", width=20, command=openConfig)
exitButton.grid(row=3, column=2, padx=5, pady=5)

versionText = tk.Label(window, text="Version 4", width=20, fg=text_color, bg=background_color)
versionText.grid(row=4, column=0, padx=1, pady=5)

usernameText = tk.Label(window, text="User: " + username, width=20, fg=text_color, bg=background_color)
usernameText.grid(row=4, column=1, padx=1, pady=5)

updateButton = tk.Button(window, text="Code in GITHUB", fg=text_color, bg=background_color, command=openBrowserUpdate)
updateButton.grid(row=4, column=2, padx=1, pady=5)


# Estilização
window.configure(background=background_color)
console.configure(font=("Courier", 10), insertbackground=text_color)
searchFile.configure(bg=background_color, fg=text_color)
writeButton.configure(bg=background_color, fg=text_color)
exitButton.configure(bg=background_color, fg=text_color)
versionText.configure(bg=background_color)
usernameText.configure(bg=background_color)


def on_closing():
    if messagebox.askokcancel("AVISO", "Deseja realmente sair?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
