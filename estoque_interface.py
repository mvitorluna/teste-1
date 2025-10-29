import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

ARQUIVO = "estoque.json"

# ===== Funções de arquivo =====
def carregar_estoque():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def salvar_estoque(estoque):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

# ===== Funções principais =====
def atualizar_tabela(filtro=""):
    for item in tabela.get_children():
        tabela.delete(item)
    for p in estoque:
        if filtro.lower() in p["nome"].lower() or filtro.lower() in p["codigo"].lower():
            tabela.insert("", tk.END, values=(p["codigo"], p["nome"], p["quantidade"], f"R$ {p['preco']:.2f}"))

def cadastrar_produto():
    codigo = entrada_codigo.get().strip()
    nome = entrada_nome.get().strip()
    quantidade = entrada_quantidade.get().strip()
    preco = entrada_preco.get().strip()

    if not codigo or not nome or not quantidade or not preco:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    for p in estoque:
        if p["codigo"] == codigo:
            messagebox.showerror("Erro", "Código já cadastrado!")
            return

    try:
        quantidade = int(quantidade)
        preco = float(preco)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade e preço devem ser números!")
        return

    produto = {"codigo": codigo, "nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(produto)
    salvar_estoque(estoque)
    atualizar_tabela()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

def entrada_produto():
    codigo = entrada_codigo.get().strip()
    qtd = entrada_quantidade.get().strip()

    if not codigo or not qtd:
        messagebox.showwarning("Aviso", "Informe o código e a quantidade!")
        return

    try:
        qtd = int(qtd)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade inválida!")
        return

    for p in estoque:
        if p["codigo"] == codigo:
            p["quantidade"] += qtd
            salvar_estoque(estoque)
            atualizar_tabela()
            messagebox.showinfo("Sucesso", "Entrada registrada!")
            return

    messagebox.showerror("Erro", "Produto não encontrado!")

def saida_produto():
    codigo = entrada_codigo.get().strip()
    qtd = entrada_quantidade.get().strip()

    if not codigo or not qtd:
        messagebox.showwarning("Aviso", "Informe o código e a quantidade!")
        return

    try:
        qtd = int(qtd)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade inválida!")
        return

    for p in estoque:
        if p["codigo"] == codigo:
            if p["quantidade"] >= qtd:
                p["quantidade"] -= qtd
                salvar_estoque(estoque)
                atualizar_tabela()
                messagebox.showinfo("Sucesso", "Saída registrada!")
            else:
                messagebox.showwarning("Aviso", "Quantidade insuficiente no estoque!")
            return

    messagebox.showerror("Erro", "Produto não encontrado!")

def relatorio_baixo_estoque():
    baixo = [p for p in estoque if p["quantidade"] < 5]
    if not baixo:
        messagebox.showinfo("Estoque OK", "Nenhum produto com baixo estoque!")
    else:
        msg = "\n".join([f"{p['nome']} — {p['quantidade']} unidades" for p in baixo])
        messagebox.showwarning("Baixo Estoque", msg)

def limpar_campos():
    entrada_codigo.delete(0, tk.END)
    entrada_nome.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)

def buscar_produto(event=None):
    termo = entrada_busca.get().strip()
    atualizar_tabela(termo)

# ===== Interface gráfica =====
estoque = carregar_estoque()

janela = tk.Tk()
janela.title("📦 Sistema de Controle de Estoque")
janela.geometry("750x550")
janela.resizable(False, False)

# ===== Campo de busca =====
frame_busca = tk.Frame(janela)
frame_busca.pack(pady=8)

tk.Label(frame_busca, text="🔎 Buscar produto:").pack(side=tk.LEFT, padx=5)
entrada_busca = tk.Entry(frame_busca, width=40)
entrada_busca.pack(side=tk.LEFT)
entrada_busca.bind("<KeyRelease>", buscar_produto)

# ===== Campos de entrada =====
frame_inputs = tk.Frame(janela)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Código:").grid(row=0, column=0, padx=5)
entrada_codigo = tk.Entry(frame_inputs, width=10)
entrada_codigo.grid(row=0, column=1)

tk.Label(frame_inputs, text="Nome:").grid(row=0, column=2, padx=5)
entrada_nome = tk.Entry(frame_inputs, width=25)
entrada_nome.grid(row=0, column=3)

tk.Label(frame_inputs, text="Qtd:").grid(row=1, column=0, padx=5)
entrada_quantidade = tk.Entry(frame_inputs, width=10)
entrada_quantidade.grid(row=1, column=1)

tk.Label(frame_inputs, text="Preço:").grid(row=1, column=2, padx=5)
entrada_preco = tk.Entry(frame_inputs, width=10)
entrada_preco.grid(row=1, column=3)

# ===== Botões =====
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Cadastrar Produto", command=cadastrar_produto, bg="#4CAF50", fg="white", width=18).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Entrada de Produto", command=entrada_produto, bg="#2196F3", fg="white", width=18).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="Saída de Produto", command=saida_produto, bg="#FF9800", fg="white", width=18).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="Relatório Baixo Estoque", command=relatorio_baixo_estoque, bg="#F44336", fg="white", width=20).grid(row=0, column=3, padx=5)

# ===== Tabela =====
colunas = ("codigo", "nome", "quantidade", "preco")
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=15)
for col in colunas:
    tabela.heading(col, text=col.capitalize())
    tabela.column(col, width=150 if col == "nome" else 100, anchor="center")
tabela.pack(pady=10)

# ===== Inicialização =====
atualizar_tabela()

janela.mainloop()
