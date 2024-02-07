from tkinter import *
import tkinter as tk
from tkinter import messagebox

def validar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if len(senha) > 6 and "@" in email:
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo!")
    else:
        messagebox.showerror("Erro no login", "Email ou senha inválidos. Verifique as restrições.")

janela = tk.Tk()
janela.title("Login")
janela.geometry("200x100")

label_email = tk.Label(janela, text="E-mail:")
label_senha = tk.Label(janela, text="Senha:")
entry_email = tk.Entry(janela)
entry_senha = tk.Entry(janela, show="*")

button_login = tk.Button(janela, text="Login", command=validar_login, bg= 'green')

label_email.grid(row=0, column=0, sticky=tk.E)
label_senha.grid(row=1, column=0, sticky=tk.E)
entry_email.grid(row=0, column=1, padx=5, pady=5)
entry_senha.grid(row=1, column=1, padx=5, pady=5)
button_login.grid(row=2, column=1, pady=10)

janela.mainloop()