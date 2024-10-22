import tkinter as tk
from tkinter import messagebox
import mysql.connector
import uuid
from datetime import datetime

# Função para conectar ao banco de dados
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="22072004",
        database="pim_vi"
    )

# Função para criar as tabelas (se ainda não existirem)
def criar_tabelas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            codigo_venda VARCHAR(36),
            nome_cliente VARCHAR(100),
            cpf_cliente VARCHAR(20),
            codigo_prod VARCHAR(20),
            nome_produto VARCHAR(100),
            quantidade INT,
            data_venda DATETIME,
            valor_venda DECIMAL(10, 2),
            opcao_pagamento VARCHAR(50)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Criando os rótulos e campos de entrada
        tk.Label(root, text="Usuário:").grid(row=0, column=0, sticky="e")
        self.usuario_entry = tk.Entry(root)
        self.usuario_entry.grid(row=0, column=1)

        tk.Label(root, text="Senha:").grid(row=1, column=0, sticky="e")
        self.senha_entry = tk.Entry(root, show="*")
        self.senha_entry.grid(row=1, column=1)

        # Botão para login
        tk.Button(root, text="Login", command=self.login).grid(row=2, columnspan=2)

    def login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if usuario == "admin" and senha == "123":
            messagebox.showinfo("Sucesso", "Login bem-sucedido como administrador!")
            self.root.destroy()  # Fecha a janela de login
            self.abrir_app("admin")  # Abre a tela de registro de vendas para o administrador
        elif usuario == "funcionario" and senha == "1234":
            messagebox.showinfo("Sucesso", "Login bem-sucedido como funcionário!")
            self.root.destroy()  # Fecha a janela de login
            self.abrir_app("funcionario")  # Abre a tela de registro de vendas para o funcionário
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def abrir_app(self, tipo_usuario):
        root = tk.Tk()
        if tipo_usuario == "admin":
            app = RegistroVendasApp(root)
        elif tipo_usuario == "funcionario":
            app = RegistroVendasAppFuncionario(root)
        root.mainloop()

class RegistroVendasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vendas")

        # Criando os rótulos e campos de entrada para o registro de vendas
        tk.Label(root, text="Nome do Cliente:").grid(row=0, column=0, sticky="e")
        self.nome_cliente_entry = tk.Entry(root)
        self.nome_cliente_entry.grid(row=0, column=1)

        tk.Label(root, text="CPF do Cliente:").grid(row=1, column=0, sticky="e")
        self.cpf_cliente_entry = tk.Entry(root)
        self.cpf_cliente_entry.grid(row=1, column=1)

        tk.Label(root, text="Código do Produto:").grid(row=2, column=0, sticky="e")
        self.codigo_produto_entry = tk.Entry(root)
        self.codigo_produto_entry.grid(row=2, column=1)

        tk.Label(root, text="Nome do Produto:").grid(row=3, column=0, sticky="e")
        self.nome_produto_entry = tk.Entry(root)
        self.nome_produto_entry.grid(row=3, column=1)

        tk.Label(root, text="Quantidade:").grid(row=4, column=0, sticky="e")
        self.quantidade_entry = tk.Entry(root)
        self.quantidade_entry.grid(row=4, column=1)

        tk.Label(root, text="Valor da Venda:").grid(row=5, column=0, sticky="e")
        self.valor_venda_entry = tk.Entry(root)
        self.valor_venda_entry.grid(row=5, column=1)

        tk.Label(root, text="Opção de Pagamento:").grid(row=6, column=0, sticky="e")
        self.opcao_pagamento_entry = tk.Entry(root)
        self.opcao_pagamento_entry.grid(row=6, column=1)

        # Botão para registrar venda
        tk.Button(root, text="Registrar Venda", command=self.registrar_venda).grid(row=7, columnspan=2)

    def registrar_venda(self):
        nome_cliente = self.nome_cliente_entry.get()
        cpf_cliente = self.cpf_cliente_entry.get()
        codigo_produto = self.codigo_produto_entry.get()
        nome_produto = self.nome_produto_entry.get()
        quantidade = self.quantidade_entry.get()
        valor_venda = self.valor_venda_entry.get()
        opcao_pagamento = self.opcao_pagamento_entry.get()
        data_venda = datetime.now()
        codigo_venda = str(uuid.uuid4())

        # Conectando ao banco de dados e inserindo os dados da venda
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO vendas (codigo_venda, nome_cliente, cpf_cliente, codigo_prod, nome_produto, quantidade, data_venda, valor_venda, opcao_pagamento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (codigo_venda, nome_cliente, cpf_cliente, codigo_produto, nome_produto, quantidade, data_venda, valor_venda, opcao_pagamento))
            conn.commit()
            messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao registrar venda: {err}")
        finally:
            cursor.close()
            conn.close()

class RegistroVendasAppFuncionario:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vendas (Funcionário)")

        # Criando os rótulos e campos de entrada para o registro de vendas
        tk.Label(root, text="Nome do Cliente:").grid(row=0, column=0, sticky="e")
        self.nome_cliente_entry = tk.Entry(root)
        self.nome_cliente_entry.grid(row=0, column=1)

        tk.Label(root, text="CPF do Cliente:").grid(row=1, column=0, sticky="e")
        self.cpf_cliente_entry = tk.Entry(root)
        self.cpf_cliente_entry.grid(row=1, column=1)

        tk.Label(root, text="Código do Produto:").grid(row=2, column=0, sticky="e")
        self.codigo_produto_entry = tk.Entry(root)
        self.codigo_produto_entry.grid(row=2, column=1)

        tk.Label(root, text="Nome do Produto:").grid(row=3, column=0, sticky="e")
        self.nome_produto_entry = tk.Entry(root)
        self.nome_produto_entry.grid(row=3, column=1)

        tk.Label(root, text="Quantidade:").grid(row=4, column=0, sticky="e")
        self.quantidade_entry = tk.Entry(root)
        self.quantidade_entry.grid(row=4, column=1)

        tk.Label(root, text="Valor da Venda:").grid(row=5, column=0, sticky="e")
        self.valor_venda_entry = tk.Entry(root)
        self.valor_venda_entry.grid(row=5, column=1)

        tk.Label(root, text="Opção de Pagamento:").grid(row=6, column=0, sticky="e")
        self.opcao_pagamento_entry = tk.Entry(root)
        self.opcao_pagamento_entry.grid(row=6, column=1)

        # Botão para registrar venda
        tk.Button(root, text="Registrar Venda", command=self.registrar_venda).grid(row=7, columnspan=2)

    def registrar_venda(self):
        nome_cliente = self.nome_cliente_entry.get()
        cpf_cliente = self.cpf_cliente_entry.get()
        codigo_produto = self.codigo_produto_entry.get()
        nome_produto = self.nome_produto_entry.get()
        quantidade = self.quantidade_entry.get()
        valor_venda = self.valor_venda_entry.get()
        opcao_pagamento = self.opcao_pagamento_entry.get()
        data_venda = datetime.now()
        codigo_venda = str(uuid.uuid4())

        # Conectando ao banco de dados e inserindo os dados da venda
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO vendas (codigo_venda, nome_cliente, cpf_cliente, codigo_prod, nome_produto, quantidade, data_venda, valor_venda, opcao_pagamento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (codigo_venda, nome_cliente, cpf_cliente, codigo_produto, nome_produto, quantidade, data_venda, valor_venda, opcao_pagamento))
            conn.commit()
            messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao registrar venda: {err}")
        finally:
            cursor.close()
            conn.close()

# Inicializando a aplicação
if __name__ == "__main__":
    criar_tabelas()  # Criando as tabelas se ainda não existirem
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()