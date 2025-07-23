import tkinter as tk
import random
import string
import pyperclip

def gerarSenha():
    tamanho_senha = int(tamanho.get());
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho_senha))
    saida.delete(0, tk.END);
    saida.insert(0, senha);

def copiar():
    senha_gerada = saida.get();
    pyperclip.copy(senha_gerada); 

janela = tk.Tk();
janela.title("Gerador de Senhas");
janela.geometry("500x250");
janela.config(bg="#346085");

#Entrada
tk.Label(janela, text="Gerador de Senhas", font=("Tahoma Bold", 25), bg="#346085", fg="white").pack(pady=10);
tk.Label(janela, text="Comprimento da Senha:", font=("Tahoma", 12), bg="#346085", fg="white").pack(pady=5);
tamanho = tk.Entry(janela);
tamanho.pack(pady=5);
tk.Button(janela, text="Gerar Senha", bg="#c9c9c9", fg="black", command=gerarSenha).pack(pady=10);

#Saída
saida = tk.Entry(janela);
saida.pack(pady=5);
tk.Button(janela, text="Copiar Senha", bg="#c9c9c9", fg="black", command=copiar).pack(pady=10);

janela.mainloop();