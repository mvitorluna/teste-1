"""
Sistema de Estoque — BR Brasil
"""

import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
import os

DB_FILE = "estoque.db"
VALIDADE_ALERT_DIAS = 10

# -----------------------
# Banco
# -----------------------
def conectar_banco(path=DB_FILE):
    conn = sqlite3.connect(path)
    # tabelas de estoques
    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )""")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos_epis (
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )""")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos_rotulos (
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL
        )""")
    # cria a tabela produtos_quimicos com colunas mínimas — as colunas completas
    # serão garantidas pela função de correção automática (sem popup).
    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos_quimicos (
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )""")
    conn.commit()
    return conn

# -----------------------
# Corrigir colunas ausentes 
# -----------------------
def corrigir_tabela_quimicos_silencioso(conn):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produtos_quimicos';")
    if not cur.fetchone():
        return
    colunas_necessarias = {
        "densidade_kg_l": "REAL",
        "unidade_origem": "TEXT",
        "litros": "REAL",
        "kilos": "REAL",
        "local_armazenamento": "TEXT",
        "lote": "TEXT",
        "validade": "TEXT"
    }
    cur.execute("PRAGMA table_info(produtos_quimicos);")
    existentes = [r[1] for r in cur.fetchall()]
    adicionadas = []
    for nome_col, tipo_col in colunas_necessarias.items():
        if nome_col not in existentes:
            cur.execute(f"ALTER TABLE produtos_quimicos ADD COLUMN {nome_col} {tipo_col};")
            adicionadas.append(nome_col)
    conn.commit()
    if adicionadas:
        # sem messagebox — apenas log no terminal
        print("Banco atualizado automaticamente. Colunas adicionadas:", ", ".join(adicionadas))

# -----------------------
# Helpers estoques
# -----------------------
def inserir_produto(conn, tabela, codigo, nome, quantidade):
    try:
        with conn:
            conn.execute(f"INSERT INTO {tabela} (codigo, nome, quantidade) VALUES (?, ?, ?)",
                         (codigo, nome, quantidade))
        return True
    except sqlite3.IntegrityError:
        return False

def listar_produtos(conn, tabela, filtro=None):
    cur = conn.cursor()
    if filtro:
        chave = f"%{filtro}%"
        cur.execute(f"SELECT codigo, nome, quantidade FROM {tabela} WHERE codigo LIKE ? OR nome LIKE ? ORDER BY nome",
                    (chave, chave))
    else:
        cur.execute(f"SELECT codigo, nome, quantidade FROM {tabela} ORDER BY nome")
    return cur.fetchall()

def buscar_produto(conn, tabela, codigo):
    cur = conn.cursor()
    cur.execute(f"SELECT codigo, nome, quantidade FROM {tabela} WHERE codigo = ?", (codigo,))
    return cur.fetchone()

def atualizar_produto(conn, tabela, codigo, nome=None, quantidade=None):
    with conn:
        if nome is not None and quantidade is not None:
            conn.execute(f"UPDATE {tabela} SET nome=?, quantidade=? WHERE codigo=?", (nome, quantidade, codigo))
        elif nome is not None:
            conn.execute(f"UPDATE {tabela} SET nome=? WHERE codigo=?", (nome, codigo))
        elif quantidade is not None:
            conn.execute(f"UPDATE {tabela} SET quantidade=? WHERE codigo=?", (quantidade, codigo))

def remover_produto(conn, tabela, codigo):
    with conn:
        conn.execute(f"DELETE FROM {tabela} WHERE codigo=?", (codigo,))

# -----------------------
# Helpers formulação (químicos)
# -----------------------
def converter_para_kg_por_l(dens_val, unidade):
    # conversões simples; internamente armazenamos kg/L
    if unidade == "kg/L": return dens_val
    if unidade == "g/cm³": return dens_val
    if unidade == "kg/m³": return dens_val * 0.001
    return dens_val

def inserir_quimico(conn, codigo, nome, densidade_kg_l, unidade_origem, litros, kilos, local, lote, validade):
    try:
        with conn:
            conn.execute("""
                INSERT INTO produtos_quimicos
                (codigo, nome, densidade_kg_l, unidade_origem, litros, kilos, local_armazenamento, lote, validade)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (codigo, nome, densidade_kg_l, unidade_origem, litros, kilos, local, lote, validade))
        return True
    except sqlite3.IntegrityError:
        return False

def listar_quimicos(conn, filtro=None):
    cur = conn.cursor()
    base = """SELECT codigo, nome, densidade_kg_l, unidade_origem, litros, kilos, local_armazenamento, lote, validade
              FROM produtos_quimicos"""
    if filtro:
        chave = f"%{filtro}%"
        base += " WHERE codigo LIKE ? OR nome LIKE ? ORDER BY nome"
        cur.execute(base, (chave, chave))
    else:
        base += " ORDER BY nome"
        cur.execute(base)
    return cur.fetchall()

def atualizar_quimico(conn, codigo, nome=None, densidade=None, unidade=None, litros=None, kilos=None, local=None, lote=None, validade=None):
    with conn:
        if all(v is not None for v in (nome, densidade, unidade, litros, kilos)):
            conn.execute("""UPDATE produtos_quimicos SET
                            nome=?, densidade_kg_l=?, unidade_origem=?, litros=?, kilos=?, local_armazenamento=?, lote=?, validade=?
                            WHERE codigo=?""",
                         (nome, densidade, unidade, litros, kilos, local, lote, validade, codigo))
        else:
            if nome is not None:
                conn.execute("UPDATE produtos_quimicos SET nome=? WHERE codigo=?", (nome, codigo))
            if densidade is not None:
                conn.execute("UPDATE produtos_quimicos SET densidade_kg_l=? WHERE codigo=?", (densidade, codigo))
            if unidade is not None:
                conn.execute("UPDATE produtos_quimicos SET unidade_origem=? WHERE codigo=?", (unidade, codigo))
            if litros is not None:
                conn.execute("UPDATE produtos_quimicos SET litros=? WHERE codigo=?", (litros, codigo))
            if kilos is not None:
                conn.execute("UPDATE produtos_quimicos SET kilos=? WHERE codigo=?", (kilos, codigo))
            if local is not None:
                conn.execute("UPDATE produtos_quimicos SET local_armazenamento=? WHERE codigo=?", (local, codigo))
            if lote is not None:
                conn.execute("UPDATE produtos_quimicos SET lote=? WHERE codigo=?", (lote, codigo))
            if validade is not None:
                conn.execute("UPDATE produtos_quimicos SET validade=? WHERE codigo=?", (validade, codigo))

def remover_quimico(conn, codigo):
    with conn:
        conn.execute("DELETE FROM produtos_quimicos WHERE codigo = ?", (codigo,))

# -----------------------
# Validade (verificação)
# -----------------------
def verificar_validade_quimicos(conn):
    hoje = date.today()
    vencidos = []
    proximos = []
    cur = conn.cursor()
    cur.execute("SELECT codigo, nome, validade FROM produtos_quimicos WHERE validade IS NOT NULL AND validade != ''")
    for codigo, nome, validade in cur.fetchall():
        try:
            vdate = datetime.strptime(validade, "%Y-%m-%d").date()
            dias = (vdate - hoje).days
            if dias < 0:
                vencidos.append((nome, validade))
            elif dias <= VALIDADE_ALERT_DIAS:
                proximos.append((nome, validade, dias))
        except:
            continue
    return vencidos, proximos

# -----------------------
# Interface
# -----------------------
class SistemaEstoque:
    def __init__(self, root, conn):
        self.root = root
        self.conn = conn

        self.COR_BG = "#07153a"
        self.COR_CARD = "#0f2b5f"
        self.COR_PRIMARY = "#132b63"
        self.COR_ACCENT = "#ffd200"
        self.COR_TEXT = "#ffffff"

        root.title("BR Brasil — Sistema de Estoque")
        root.geometry("1120x760")
        root.configure(bg=self.COR_BG)

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("TNotebook", background=self.COR_BG)
        self.style.configure("TNotebook.Tab", background=self.COR_CARD, foreground=self.COR_TEXT, padding=[12,8])
        self.style.map("TNotebook.Tab", background=[("selected", self.COR_PRIMARY)])

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=12, pady=12)

        # abas: chave -> nome da tabela
        self.abas = [
            ("Estoque Principal", "produtos"),
            ("Estoque EPI'S", "produtos_epis"),
            ("Rótulos / Sleeve", "produtos_rotulos"),
            ("Formulação", "produtos_quimicos"),
            ("Relatórios", None)
        ]
        self.frames = {}
        for titulo, tabela in self.abas:
            f = tk.Frame(self.notebook, bg=self.COR_BG)
            self.notebook.add(f, text=titulo)
            if tabela:
                self.frames[tabela] = f
            else:
                self.frames["relatorios"] = f

        # montar abas
        for titulo, tabela in self.abas:
            if tabela is None:
                self._montar_aba_relatorios(self.frames["relatorios"])
            elif tabela == "produtos_quimicos":
                self._montar_aba_formulacao(self.frames[tabela])
            else:
                self._montar_aba_estoque_com_cadastro(self.frames[tabela], tabela, titulo)

        # bind troca de aba para alerta de validade (apenas Formulação)
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)

    # ---- Aba estoque com cadastro (reaproveitável) ----
    def _montar_aba_estoque_com_cadastro(self, frame, tabela, titulo):
        # Card de cadastro (Código, Nome, Quantidade)
        card = tk.LabelFrame(frame, text=f"{titulo} — Cadastro de Produto", bg=self.COR_BG, fg=self.COR_ACCENT, padx=12, pady=12)
        card.pack(fill="x", padx=12, pady=8)

        tk.Label(card, text="Código:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=0, column=0, sticky="w", padx=6, pady=6)
        entry_cod = tk.Entry(card, width=24); entry_cod.grid(row=0, column=1, padx=6, pady=6)

        tk.Label(card, text="Nome:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=1, column=0, sticky="w", padx=6, pady=6)
        entry_nome = tk.Entry(card, width=56); entry_nome.grid(row=1, column=1, columnspan=2, padx=6, pady=6)

        tk.Label(card, text="Quantidade:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=2, column=0, sticky="w", padx=6, pady=6)
        entry_qtd = tk.Entry(card, width=12); entry_qtd.grid(row=2, column=1, padx=6, pady=6, sticky="w")

        def salvar(event=None):
            cod = entry_cod.get().strip(); nome = entry_nome.get().strip(); qtd = entry_qtd.get().strip()
            if not cod or not nome or not qtd:
                messagebox.showwarning("Atenção", "Preencha todos os campos.")
                return
            try:
                qi = int(qtd)
                if qi < 0: raise ValueError
            except ValueError:
                messagebox.showerror("Erro", "Quantidade inválida.")
                return
            ok = inserir_produto(self.conn, tabela, cod, nome, qi)
            if not ok:
                messagebox.showerror("Erro", "Código já cadastrado.")
                return
            # limpa campos e atualiza tabela
            entry_cod.delete(0, tk.END); entry_nome.delete(0, tk.END); entry_qtd.delete(0, tk.END)
            atualizar()

        def limpar():
            entry_cod.delete(0, tk.END); entry_nome.delete(0, tk.END); entry_qtd.delete(0, tk.END)

        tk.Button(card, text="Salvar", bg=self.COR_ACCENT, fg="black", width=18, command=salvar).grid(row=3, column=0, padx=6, pady=8)
        tk.Button(card, text="Limpar Campos", bg="#555", fg="white", width=16, command=limpar).grid(row=3, column=1, padx=6, pady=8, sticky="w")

        # Bind Enter para salvar
        for e in (entry_cod, entry_nome, entry_qtd):
            e.bind("<Return>", salvar)

        # Barra de busca
        barra = tk.Frame(frame, bg=self.COR_BG); barra.pack(fill="x", padx=12, pady=(8,2))
        tk.Label(barra, text="Buscar:", bg=self.COR_BG, fg=self.COR_TEXT).pack(side="left", padx=6)
        entry_busca = tk.Entry(barra, width=44); entry_busca.pack(side="left", padx=4)
        def pesquisar(event=None):
            atualizar(entry_busca.get().strip())
        tk.Button(barra, text="Pesquisar", bg=self.COR_PRIMARY, fg="white", command=pesquisar).pack(side="left", padx=6)
        tk.Button(barra, text="Mostrar Todos", bg="#607D8B", fg="white", command=lambda: atualizar()).pack(side="left", padx=6)
        entry_busca.bind("<Return>", pesquisar)

        # Treeview
        tree = ttk.Treeview(frame, columns=("codigo","nome","quantidade"), show="headings", height=16)
        tree.heading("codigo", text="Código"); tree.heading("nome", text="Nome"); tree.heading("quantidade", text="Quantidade")
        tree.column("codigo", width=160); tree.column("nome", width=620); tree.column("quantidade", width=120, anchor="center")
        tree.pack(fill="both", expand=True, padx=12, pady=8)

        # ações: editar, baixar, remover, atualizar
        def atualizar(filtro=None):
            tree.delete(*tree.get_children())
            for cod, nome, qtd in listar_produtos(self.conn, tabela, filtro):
                tree.insert("", "end", values=(cod, nome, qtd))

        def editar():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Atenção", "Selecione um produto."); return
            codigo = tree.item(sel[0], "values")[0]
            self._abrir_janela_edicao_estoque(codigo, tabela, atualizar)

        def remover():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Atenção", "Selecione um produto."); return
            codigo, nome = tree.item(sel[0], "values")[:2]
            if messagebox.askyesno("Confirmar", f"Remover '{nome}' (código {codigo})?"):
                remover_produto(self.conn, tabela, codigo); atualizar()

        def baixar():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Atenção", "Selecione um produto."); return
            codigo = tree.item(sel[0], "values")[0]
            self._abrir_janela_baixa_estoque(codigo, tabela, atualizar)

        bar = tk.Frame(frame, bg=self.COR_BG); bar.pack(fill="x", padx=12, pady=6)
        tk.Button(bar, text="Editar", bg="#4CAF50", fg="white", command=editar).pack(side="left", padx=6)
        tk.Button(bar, text="Baixar Estoque", bg=self.COR_ACCENT, fg="black", command=baixar).pack(side="left", padx=6)
        tk.Button(bar, text="Remover", bg="#D32F2F", fg="white", command=remover).pack(side="left", padx=6)
        tk.Button(bar, text="Atualizar", bg="#607D8B", fg="white", command=lambda: atualizar()).pack(side="right", padx=6)

        atualizar()

    # ---- Janela editar / baixa para estoques ----
    def _abrir_janela_edicao_estoque(self, codigo, tabela, callback):
        prod = buscar_produto(self.conn, tabela, codigo)
        if not prod:
            messagebox.showerror("Erro", "Produto não encontrado."); return
        cod, nome, qtd = prod
        j = tk.Toplevel(self.root); j.title(f"Editar — {cod}"); j.geometry("420x240"); j.configure(bg=self.COR_BG)
        tk.Label(j, text="Código:", bg=self.COR_BG, fg=self.COR_ACCENT).pack(anchor="w", padx=12, pady=(12,4))
        tk.Label(j, text=cod, bg=self.COR_BG, fg=self.COR_TEXT).pack(anchor="w", padx=12)
        tk.Label(j, text="Nome:", bg=self.COR_BG, fg=self.COR_TEXT).pack(anchor="w", padx=12, pady=(8,4))
        entry_nome = tk.Entry(j, width=48); entry_nome.insert(0, nome); entry_nome.pack(padx=12)
        tk.Label(j, text="Quantidade:", bg=self.COR_BG, fg=self.COR_TEXT).pack(anchor="w", padx=12, pady=(8,4))
        entry_qtd = tk.Entry(j, width=12); entry_qtd.insert(0, str(qtd)); entry_qtd.pack(padx=12)
        def salvar(event=None):
            novo_nome = entry_nome.get().strip(); qtd_str = entry_qtd.get().strip()
            if not novo_nome or not qtd_str:
                messagebox.showwarning("Atenção", "Preencha todos os campos."); return
            try:
                nova_qtd = int(qtd_str)
                if nova_qtd < 0: raise ValueError
            except ValueError:
                messagebox.showerror("Erro", "Quantidade inválida."); return
            atualizar_produto(self.conn, tabela, cod, nome=novo_nome, quantidade=nova_qtd)
            messagebox.showinfo("Sucesso", "Produto atualizado."); j.destroy(); callback()
        tk.Button(j, text="Salvar", bg="#4CAF50", fg="white", command=salvar).pack(pady=10)
        entry_qtd.bind("<Return>", salvar)

    def _abrir_janela_baixa_estoque(self, codigo, tabela, callback):
        prod = buscar_produto(self.conn, tabela, codigo)
        if not prod:
            messagebox.showerror("Erro", "Produto não encontrado."); return
        cod, nome, qtd_atual = prod
        j = tk.Toplevel(self.root); j.title(f"Dar Baixa — {cod}"); j.geometry("360x200"); j.configure(bg=self.COR_BG)
        tk.Label(j, text=f"{nome} (Atual: {qtd_atual})", bg=self.COR_BG, fg=self.COR_ACCENT).pack(pady=10)
        entry_baixa = tk.Entry(j, width=12); entry_baixa.pack(pady=6)
        def confirmar(event=None):
            try:
                baixa = int(entry_baixa.get())
                if baixa <= 0 or baixa > qtd_atual: raise ValueError
            except ValueError:
                messagebox.showerror("Erro", "Quantidade inválida."); return
            atualizar_produto(self.conn, tabela, cod, quantidade=qtd_atual - baixa)
            messagebox.showinfo("Sucesso", f"Baixa aplicada. Novo estoque: {qtd_atual - baixa}"); j.destroy(); callback()
        tk.Button(j, text="Confirmar", bg=self.COR_ACCENT, fg="black", command=confirmar).pack(pady=8)
        entry_baixa.bind("<Return>", confirmar)

    # ---- Aba Formulação ----
    def _montar_aba_formulacao(self, frame):
        tk.Label(frame, text="Formulação", bg=self.COR_BG, fg=self.COR_ACCENT, font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=6)

        # topo: formulário de cadastro específico para formulação
        card = tk.LabelFrame(frame, text="Cadastro de Formulação", bg=self.COR_BG, fg=self.COR_ACCENT, padx=12, pady=12)
        card.pack(fill="x", padx=12, pady=8)

        tk.Label(card, text="Código:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=0, column=0, sticky="w", padx=6, pady=6)
        entry_cod = tk.Entry(card, width=18); entry_cod.grid(row=0, column=1, padx=6, pady=6)

        tk.Label(card, text="Nome:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=1, column=0, sticky="w", padx=6, pady=6)
        entry_nome = tk.Entry(card, width=44); entry_nome.grid(row=1, column=1, columnspan=2, padx=6, pady=6)

        tk.Label(card, text="Densidade:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=2, column=0, sticky="w", padx=6, pady=6)
        entry_dens = tk.Entry(card, width=12); entry_dens.grid(row=2, column=1, sticky="w", padx=6, pady=6)
        unit_combo = ttk.Combobox(card, values=("kg/L","g/cm³","kg/m³"), width=8, state="readonly"); unit_combo.current(0); unit_combo.grid(row=2, column=2, padx=6)

        tk.Label(card, text="Litros:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=3, column=0, sticky="w", padx=6, pady=6)
        entry_litros = tk.Entry(card, width=12); entry_litros.grid(row=3, column=1, sticky="w", padx=6, pady=6)

        tk.Label(card, text="Local:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=0, column=3, sticky="w", padx=8, pady=6)
        entry_local = tk.Entry(card, width=20); entry_local.grid(row=0, column=4, padx=6, pady=6)
        tk.Label(card, text="Lote:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=1, column=3, sticky="w", padx=8, pady=6)
        entry_lote = tk.Entry(card, width=20); entry_lote.grid(row=1, column=4, padx=6, pady=6)
        tk.Label(card, text="Validade (YYYY-MM-DD):", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=2, column=3, sticky="w", padx=8, pady=6)
        entry_validade = tk.Entry(card, width=16); entry_validade.grid(row=2, column=4, padx=6, pady=6)

        lbl_kilos = tk.Label(card, text="Peso (Kg): —", bg=self.COR_BG, fg=self.COR_ACCENT, font=("Arial", 11, "bold"))
        lbl_kilos.grid(row=4, column=0, columnspan=3, pady=(8,4), sticky="w")

        # cálculo em tempo real e bind Enter para salvar
        def calcular_local(event=None):
            try:
                dv = float(entry_dens.get()); u = unit_combo.get()
                lv = float(entry_litros.get()) if entry_litros.get().strip() != "" else 0.0
                dk = converter_para_kg_por_l(dv, u)
                lbl_kilos.config(text=f"Peso (Kg): {dk*lv:.3f}  (dens={dk:.4f} kg/L)")
            except:
                lbl_kilos.config(text="Peso (Kg): —")

        entry_dens.bind("<KeyRelease>", calcular_local)
        entry_litros.bind("<KeyRelease>", calcular_local)
        unit_combo.bind("<<ComboboxSelected>>", lambda e: calcular_local())

        def salvar_formulacao(event=None):
            codigo = entry_cod.get().strip(); nome = entry_nome.get().strip()
            local = entry_local.get().strip() or None; lote = entry_lote.get().strip() or None
            validade = entry_validade.get().strip() or None
            if validade:
                try:
                    datetime.strptime(validade, "%Y-%m-%d")
                except:
                    messagebox.showerror("Erro", "Validade deve estar no formato YYYY-MM-DD."); return
            try:
                dv = float(entry_dens.get()); u = unit_combo.get(); lv = float(entry_litros.get())
            except:
                messagebox.showerror("Erro", "Densidade e Litros inválidos."); return
            dk = converter_para_kg_por_l(dv, u); kilos = dk * lv
            if not codigo or not nome:
                messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios."); return
            ok = inserir_quimico(self.conn, codigo, nome, dk, u, lv, kilos, local, lote, validade)
            if not ok:
                messagebox.showerror("Erro", "Código já cadastrado."); return
            messagebox.showinfo("Sucesso", f"Formulação '{nome}' cadastrada.")
            # limpar
            entry_cod.delete(0, tk.END); entry_nome.delete(0, tk.END); entry_dens.delete(0, tk.END)
            entry_litros.delete(0, tk.END); entry_local.delete(0, tk.END); entry_lote.delete(0, tk.END); entry_validade.delete(0, tk.END)
            lbl_kilos.config(text="Peso (Kg): —")
            atualizar()

        tk.Button(card, text="Salvar", bg=self.COR_ACCENT, fg="black", command=salvar_formulacao).grid(row=5, column=0, pady=8)
        for e in (entry_cod, entry_nome, entry_dens, entry_litros, entry_local, entry_lote, entry_validade):
            e.bind("<Return>", salvar_formulacao)

        # busca e tabela
        barra = tk.Frame(frame, bg=self.COR_BG); barra.pack(fill="x", padx=12, pady=(8,2))
        tk.Label(barra, text="Buscar:", bg=self.COR_BG, fg=self.COR_TEXT).pack(side="left", padx=6)
        entry_busca = tk.Entry(barra, width=44); entry_busca.pack(side="left", padx=4)
        def pesquisar(event=None):
            atualizar(entry_busca.get().strip())
        tk.Button(barra, text="Pesquisar", bg=self.COR_PRIMARY, fg="white", command=pesquisar).pack(side="left", padx=6)
        tk.Button(barra, text="Mostrar Todos", bg="#607D8B", fg="white", command=lambda: atualizar()).pack(side="left", padx=6)
        entry_busca.bind("<Return>", pesquisar)

        tree = ttk.Treeview(frame, columns=("codigo","nome","densidade","litros","kilos","validade"), show="headings", height=14)
        for c, n in [("codigo","Código"),("nome","Nome"),("densidade","Dens (kg/L)"),("litros","Litros"),("kilos","Kilos"),("validade","Validade")]:
            tree.heading(c, text=n)
        tree.column("codigo", width=140); tree.column("nome", width=360); tree.column("densidade", width=120, anchor="center")
        tree.column("litros", width=100, anchor="center"); tree.column("kilos", width=100, anchor="center"); tree.column("validade", width=120, anchor="center")
        tree.pack(fill="both", expand=True, padx=12, pady=8)

        tree.tag_configure("vencido", background="#FFCDD2")
        tree.tag_configure("proximo", background="#FFF9C4")

        def atualizar(filtro=None):
            tree.delete(*tree.get_children())
            for cod, nome, dens, unidade, litros, kilos, local, lote, validade in listar_quimicos(self.conn, filtro):
                tag = ""
                if validade:
                    try:
                        dias = (datetime.strptime(validade, "%Y-%m-%d").date() - date.today()).days
                        if dias < 0:
                            tag = "vencido"
                        elif dias <= VALIDADE_ALERT_DIAS:
                            tag = "proximo"
                    except:
                        tag = ""
                tree.insert("", "end", values=(cod, nome, f"{dens:.4f}", f"{litros:.3f}", f"{kilos:.3f}", validade or ""), tags=(tag,))

        # ações editar/remover para formulação
        def editar_formulacao():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Atenção", "Selecione uma formulação."); return
            codigo = tree.item(sel[0], "values")[0]
            self._janela_editar_formulacao(codigo, atualizar)

        def remover_formulacao():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Atenção", "Selecione uma formulação."); return
            codigo, nome = tree.item(sel[0], "values")[0], tree.item(sel[0], "values")[1]
            if messagebox.askyesno("Confirmar", f"Remover '{nome}' (código {codigo})?"):
                remover_quimico(self.conn, codigo); atualizar()

        bar = tk.Frame(frame, bg=self.COR_BG); bar.pack(fill="x", padx=12, pady=6)
        tk.Button(bar, text="Editar", bg="#4CAF50", fg="white", command=editar_formulacao).pack(side="left", padx=6)
        tk.Button(bar, text="Remover", bg="#D32F2F", fg="white", command=remover_formulacao).pack(side="left", padx=6)
        tk.Button(bar, text="Atualizar", bg="#607D8B", fg="white", command=lambda: atualizar()).pack(side="right", padx=6)

        # salvar função atualizar para uso externo (quando abrir aba)
        self.atualizar_formulacao = atualizar
        atualizar()

    def _janela_editar_formulacao(self, codigo, callback):
        prod = None
        cur = self.conn.cursor()
        cur.execute("SELECT codigo, nome, densidade_kg_l, unidade_origem, litros, kilos, local_armazenamento, lote, validade FROM produtos_quimicos WHERE codigo = ?", (codigo,))
        row = cur.fetchone()
        if not row:
            messagebox.showerror("Erro", "Formulação não encontrada."); return
        cod, nome, dens, unidade, litros, kilos, local, lote, validade = row
        j = tk.Toplevel(self.root); j.title(f"Editar — {cod}"); j.geometry("640x360"); j.configure(bg=self.COR_BG)
        frame = tk.Frame(j, bg=self.COR_BG); frame.pack(fill="both", expand=True, padx=12, pady=12)

        tk.Label(frame, text="Código:", bg=self.COR_BG, fg=self.COR_ACCENT).grid(row=0, column=0, sticky="w")
        tk.Label(frame, text=cod, bg=self.COR_BG, fg=self.COR_TEXT).grid(row=0, column=1, sticky="w")
        tk.Label(frame, text="Nome:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=1, column=0, sticky="w", pady=4)
        entry_nome = tk.Entry(frame, width=40); entry_nome.grid(row=1, column=1, pady=4); entry_nome.insert(0, nome)

        tk.Label(frame, text="Densidade:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=2, column=0, sticky="w", pady=4)
        entry_dens = tk.Entry(frame, width=12); entry_dens.grid(row=2, column=1, sticky="w", pady=4); entry_dens.insert(0, f"{dens:.4f}")
        unit_combo = ttk.Combobox(frame, values=("kg/L","g/cm³","kg/m³"), width=8, state="readonly"); unit_combo.grid(row=2, column=2, padx=8, pady=4)
        # tentar setar unidade_origem do DB
        unit_combo.set(unidade if unidade else "kg/L")

        tk.Label(frame, text="Litros:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=3, column=0, sticky="w", pady=4)
        entry_litros = tk.Entry(frame, width=12); entry_litros.grid(row=3, column=1, sticky="w", pady=4); entry_litros.insert(0, f"{litros:.3f}")

        tk.Label(frame, text="Local:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=4, column=0, sticky="w", pady=4)
        entry_local = tk.Entry(frame, width=30); entry_local.grid(row=4, column=1, pady=4); entry_local.insert(0, local or "")

        tk.Label(frame, text="Lote:", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=5, column=0, sticky="w", pady=4)
        entry_lote = tk.Entry(frame, width=20); entry_lote.grid(row=5, column=1, pady=4); entry_lote.insert(0, lote or "")

        tk.Label(frame, text="Validade (YYYY-MM-DD):", bg=self.COR_BG, fg=self.COR_TEXT).grid(row=6, column=0, sticky="w", pady=4)
        entry_validade = tk.Entry(frame, width=16); entry_validade.grid(row=6, column=1, pady=4); entry_validade.insert(0, validade or "")

        lbl_kilos = tk.Label(frame, text=f"Peso (Kg): {kilos:.3f}", bg=self.COR_BG, fg=self.COR_ACCENT)
        lbl_kilos.grid(row=7, column=0, columnspan=3, pady=8, sticky="w")

        def calcular_local(event=None):
            try:
                dv = float(entry_dens.get()); u = unit_combo.get(); lv = float(entry_litros.get())
                dk = converter_para_kg_por_l(dv, u)
                lbl_kilos.config(text=f"Peso (Kg): {dk*lv:.3f} (dens={dk:.4f} kg/L)")
            except:
                lbl_kilos.config(text="Peso (Kg): —")

        entry_dens.bind("<KeyRelease>", calcular_local); entry_litros.bind("<KeyRelease>", calcular_local)
        unit_combo.bind("<<ComboboxSelected>>", lambda e: calcular_local())

        def salvar_edit(event=None):
            novo_nome = entry_nome.get().strip()
            try:
                dv = float(entry_dens.get()); u = unit_combo.get(); lv = float(entry_litros.get())
            except:
                messagebox.showerror("Erro", "Densidade e Litros inválidos."); return
            nk = converter_para_kg_por_l(dv, u) * lv
            localv = entry_local.get().strip() or None; lotev = entry_lote.get().strip() or None; validadev = entry_validade.get().strip() or None
            if validadev:
                try:
                    datetime.strptime(validadev, "%Y-%m-%d")
                except:
                    messagebox.showerror("Erro", "Validade deve estar no formato YYYY-MM-DD."); return
            atualizar_quimico(self.conn, cod, nome=novo_nome, densidade=converter_para_kg_por_l(dv, u), unidade=u, litros=lv, kilos=nk, local=localv, lote=lotev, validade=validadev)
            messagebox.showinfo("Sucesso", "Formulação atualizada."); j.destroy(); callback()

        tk.Button(frame, text="Salvar", bg="#4CAF50", fg="white", command=salvar_edit).grid(row=8, column=0, pady=10)

    # ---- aba Relatórios ----
    def _montar_aba_relatorios(self, frame):
        tk.Label(frame, text="Relatórios — Visualização", bg=self.COR_BG, fg=self.COR_ACCENT, font=("Arial", 12, "bold")).pack(anchor="w", padx=12, pady=(12,6))
        boxes = [
            ("produtos", "Estoque Principal"),
            ("produtos_epis", "Estoque EPI'S"),
            ("produtos_rotulos", "Rótulos / Sleeve"),
            ("produtos_quimicos", "Formulação")
        ]
        for tabela, nome in boxes:
            box = tk.LabelFrame(frame, text=nome, bg=self.COR_BG, fg=self.COR_TEXT, padx=8, pady=8); box.pack(fill="x", padx=12, pady=6)
            tk.Button(box, text="Visualizar Relatório", bg="#607D8B", fg="white", command=lambda t=tabela: self._abrir_relatorio(t)).pack(side="left", padx=8)

    def _abrir_relatorio(self, tabela):
        j = tk.Toplevel(self.root); j.title(f"Relatório — {tabela}"); j.geometry("920x520"); j.configure(bg=self.COR_BG)
        tk.Label(j, text=f"Relatório — {tabela}", bg=self.COR_BG, fg=self.COR_ACCENT, font=("Arial", 12, "bold")).pack(anchor="w", padx=12, pady=8)
        if tabela == "produtos_quimicos":
            cols = ("codigo","nome","densidade","unidade","litros","kilos","local","lote","validade")
            tree = ttk.Treeview(j, columns=cols, show="headings")
            for col, txt in [("codigo","Código"),("nome","Nome"),("densidade","Dens (kg/L)"),("unidade","Unid"),("litros","Litros"),("kilos","Kilos"),("local","Local"),("lote","Lote"),("validade","Validade")]:
                tree.heading(col, text=txt)
            tree.tag_configure('vencido', background='#FFCDD2'); tree.tag_configure('proximo', background='#FFF9C4')
            for codigo, nome, dens, unidade, litros, kilos, local, lote, validade in listar_quimicos(self.conn):
                tag = ""
                if validade:
                    try:
                        dias = (datetime.strptime(validade, "%Y-%m-%d").date() - date.today()).days
                        if dias < 0: tag = 'vencido'
                        elif dias <= VALIDADE_ALERT_DIAS: tag = 'proximo'
                    except:
                        tag = ""
                tree.insert("", "end", values=(codigo, nome, f"{dens:.4f}", unidade, f"{litros:.3f}", f"{kilos:.3f}", local or "", lote or "", validade or ""), tags=(tag,))
        else:
            cols = ("codigo","nome","quantidade"); tree = ttk.Treeview(j, columns=cols, show="headings")
            tree.heading("codigo", text="Código"); tree.heading("nome", text="Nome"); tree.heading("quantidade", text="Quantidade")
            for cod, nome, qtd in listar_produtos(self.conn, tabela=tabela):
                tree.insert("", "end", values=(cod, nome, qtd))
        tree.pack(fill="both", expand=True, padx=12, pady=8)
        tk.Button(j, text="Fechar", bg="#999", fg="white", command=j.destroy).pack(pady=8)

    # ---- Evento: troca de aba (alerta de validade apenas na aba Formulação) ----
    def _on_tab_changed(self, event):
        aba_text = self.notebook.tab(self.notebook.select(), "text")
        if aba_text == "Formulação":
            vencidos, proximos = verificar_validade_quimicos(self.conn)
            if vencidos or proximos:
                self._mostrar_alerta_validade(vencidos, proximos)
            # atualizar tabela de formulação caso exista
            if hasattr(self, "atualizar_formulacao"):
                self.atualizar_formulacao()

    def _mostrar_alerta_validade(self, vencidos, proximos):
        j = tk.Toplevel(self.root); j.title("Alerta de Validade — Formulação"); j.geometry("540x420"); j.configure(bg=self.COR_BG)
        tk.Label(j, text="⚠️ Alerta de Validade", bg=self.COR_PRIMARY, fg=self.COR_ACCENT, font=("Arial", 14, "bold")).pack(fill="x", pady=8)
        body = tk.Frame(j, bg=self.COR_BG); body.pack(fill="both", expand=True, padx=12, pady=6)
        if vencidos:
            box_v = tk.LabelFrame(body, text=f"Vencidos ({len(vencidos)})", bg="#FFEBEE", fg="#B71C1C", padx=8, pady=8)
            box_v.pack(fill="x", pady=6)
            for nome, validade in vencidos:
                tk.Label(box_v, text=f"{nome} — {validade}", anchor="w", bg="#FFEBEE").pack(fill="x")
        if proximos:
            box_p = tk.LabelFrame(body, text=f"A vencer (≤ {VALIDADE_ALERT_DIAS} dias) ({len(proximos)})", bg="#FFFDE7", fg="#F57F17", padx=8, pady=8)
            box_p.pack(fill="x", pady=6)
            for nome, validade, dias in proximos:
                tk.Label(box_p, text=f"{nome} — {validade} (em {dias} dias)", anchor="w", bg="#FFFDE7").pack(fill="x")
        tk.Button(j, text="Fechar", bg="#607D8B", fg="white", command=j.destroy).pack(pady=8)

# -----------------------
# main()
# -----------------------
def main():
    conn = conectar_banco()
    # corrige colunas ausentes sem popup
    corrigir_tabela_quimicos_silencioso(conn)
    root = tk.Tk()
    app = SistemaEstoque(root, conn)
    root.mainloop()
    conn.close()

if __name__ == "__main__":
    main()
