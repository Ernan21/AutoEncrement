import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import pyautogui
import time

# Configurações da tela do programa
window = tk.Tk()
window.configure(borderwidth=5, width=800, height=600)
window.resizable(False, False)
window.title("AutoEncremente Version 3")

# Criando a tela de console
console = tk.Text(window, state='disabled', width=96, height=20, background="black", foreground="white")
console.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

# Função para imprimir informações na tela de console
def log(msg):
    console.config(state='normal')
    console.insert(tk.END, msg + '\n')
    console.config(state='disabled')
    console.see(tk.END)

filebydirectory = tk.Entry(window, width=95, borderwidth=2)
filebydirectory.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# Variavel global para armazenar o conteudo do arquivo
conteudo = []
lista = []

def FsearchFile():
    arquivo = filedialog.askopenfilename()
    filebydirectory.delete(0, tk.END)
    filebydirectory.insert(0, arquivo)
    log("Arquivo selecionado: " + arquivo)
    arquivo = filebydirectory.get()

    try:
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            log(arquivo)
            lista.extend(conteudo.split(","))
    
    except Exception as e:
        log("Erro ao ler o arquivo " + str(e))
        messagebox.showerror("ERRO", "Não foi possivel ler o arquivo!")

    return arquivo

def to_write():
    # timer de 8 segundos para iniciar a função do arrey
    time.sleep(8)
    # Repete a função enquanto tiver itens no arrey
    for item in lista:
        pyautogui.typewrite(item.strip())
        pyautogui.press('enter')
    log("A lista de itens " + str(lista) + " foi digitada corretamente")

def exit_program():
    window.destroy()


# Lista de butões na tela no programa
searchFile = tk.Button(window, text="Buscar arquivo", width=20, command=FsearchFile)
searchFile.grid(row=0, column=2, padx=5, pady=5)

writeButton = tk.Button(window, text="Escrever conteudo", width=20, command=to_write)
writeButton.grid(row=2, column=1, padx=3, pady=3)

exitButton = tk.Button(window, text="Sair do programa", width=20, command=exit_program)
exitButton.grid(row=2, column=2, padx=5, pady=5)

window.mainloop()