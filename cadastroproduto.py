import tkinter as tk
from tkinter import messagebox
import mysql.connector

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
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            codigo_barras VARCHAR(20),
            nome_produto VARCHAR(100),
            categoria VARCHAR(100),
            fabricante VARCHAR(100),
            quantidade INT,
            valor DECIMAL(10, 2)
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
            self.abrir_app("admin")  # Abre a tela de cadastro de produtos para o administrador
        elif usuario == "funcionario" and senha == "1234":
            messagebox.showinfo("Sucesso", "Login bem-sucedido como funcionário!")
            self.root.destroy()  # Fecha a janela de login
            self.abrir_app("funcionario")  # Abre a tela de cadastro de produtos para o funcionário
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def abrir_app(self, tipo_usuario):
        root = tk.Tk()
        if tipo_usuario == "admin":
            app = CadastroProdutosApp(root)
        elif tipo_usuario == "funcionario":
            app = CadastroProdutosAppFuncionario(root)
        root.mainloop()

class CadastroProdutosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")

        # Criando os rótulos e campos de entrada para o cadastro de produtos
        tk.Label(root, text="Código de Barras:").grid(row=0, column=0, sticky="e")
        self.codigo_barras_entry = tk.Entry(root)
        self.codigo_barras_entry.grid(row=0, column=1)

        tk.Label(root, text="Nome do Produto:").grid(row=1, column=0, sticky="e")
        self.nome_produto_entry = tk.Entry(root)
        self.nome_produto_entry.grid(row=1, column=1)

        tk.Label(root, text="Categoria:").grid(row=2, column=0, sticky="e")
        self.categoria_entry = tk.Entry(root)
        self.categoria_entry.grid(row=2, column=1)

        tk.Label(root, text="Fabricante:").grid(row=3, column=0, sticky="e")
        self.fabricante_entry = tk.Entry(root)
        self.fabricante_entry.grid(row=3, column=1)

        tk.Label(root, text="Quantidade:").grid(row=4, column=0, sticky="e")
        self.quantidade_entry = tk.Entry(root)
        self.quantidade_entry.grid(row=4, column=1)

        tk.Label(root, text="Valor:").grid(row=5, column=0, sticky="e")
        self.valor_entry = tk.Entry(root)
        self.valor_entry.grid(row=5, column=1)

        # Botão para cadastrar produto
        tk.Button(root, text="Cadastrar Produto", command=self.cadastrar_produto).grid(row=6, columnspan=2)

    def cadastrar_produto(self):
        codigo_barras = self.codigo_barras_entry.get()
        nome_produto = self.nome_produto_entry.get()
        categoria = self.categoria_entry.get()
        fabricante = self.fabricante_entry.get()
        quantidade = int(self.quantidade_entry.get())
        valor = float(self.valor_entry.get())

        # Conectando ao banco de dados e inserindo os dados do produto
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO produtos (codigo_barras, nome_produto, categoria, fabricante, quantidade, valor)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (codigo_barras, nome_produto, categoria, fabricante, quantidade, valor))
            conn.commit()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar produto: {err}")
        finally:
            cursor.close()
            conn.close()

class CadastroProdutosAppFuncionario:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos (Funcionário)")

        # Criando os rótulos e campos de entrada para o cadastro de produtos
        tk.Label(root, text="Código de Barras:").grid(row=0, column=0, sticky="e")
        self.codigo_barras_entry = tk.Entry(root)
        self.codigo_barras_entry.grid(row=0, column=1)

        tk.Label(root, text="Nome do Produto:").grid(row=1, column=0, sticky="e")
        self.nome_produto_entry = tk.Entry(root)
        self.nome_produto_entry.grid(row=1, column=1)

        tk.Label(root, text="Categoria:").grid(row=2, column=0, sticky="e")
        self.categoria_entry = tk.Entry(root)
        self.categoria_entry.grid(row=2, column=1)

        tk.Label(root, text="Fabricante:").grid(row=3, column=0, sticky="e")
        self.fabricante_entry = tk.Entry(root)
        self.fabricante_entry.grid(row=3, column=1)

        tk.Label(root, text="Quantidade:").grid(row=4, column=0, sticky="e")
        self.quantidade_entry = tk.Entry(root)
        self.quantidade_entry.grid(row=4, column=1)

        tk.Label(root, text="Valor:").grid(row=5, column=0, sticky="e")
        self.valor_entry = tk.Entry(root)
        self.valor_entry.grid(row=5, column=1)

        # Botão para cadastrar produto
        tk.Button(root, text="Cadastrar Produto", command=self.cadastrar_produto).grid(row=6, columnspan=2)

    def cadastrar_produto(self):
        codigo_barras = self.codigo_barras_entry.get()
        nome_produto = self.nome_produto_entry.get()
        categoria = self.categoria_entry.get()
        fabricante = self.fabricante_entry.get()
        quantidade = int(self.quantidade_entry.get())
        valor = float(self.valor_entry.get())

        # Conectando ao banco de dados e inserindo os dados do produto
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO produtos (codigo_barras, nome_produto, categoria, fabricante, quantidade, valor)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (codigo_barras, nome_produto, categoria, fabricante, quantidade, valor))
            conn.commit()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar produto: {err}")
        finally:
            cursor.close()
            conn.close()

# Inicializando a aplicação
if __name__ == "__main__":
    criar_tabelas()  # Criando as tabelas se ainda não existirem
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()