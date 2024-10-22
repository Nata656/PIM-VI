import tkinter as tk
from tkinter import messagebox
import mysql.connector


def conectar_bd():
    return mysql.connector.connect(
        host="localhost",   
        user="root",        
        password="22072004",
        database="pim_vi"  
    )


def criar_tabelas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            rg VARCHAR(20),
            cpf VARCHAR(20),
            nome VARCHAR(100),
            data_cadastro DATE,
            endereco VARCHAR(200),
            telefone VARCHAR(20),
            email VARCHAR(100)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        
        tk.Label(root, text="Usuário:").grid(row=0, column=0, sticky="e")
        self.usuario_entry = tk.Entry(root)
        self.usuario_entry.grid(row=0, column=1)

        tk.Label(root, text="Senha:").grid(row=1, column=0, sticky="e")
        self.senha_entry = tk.Entry(root, show="*")
        self.senha_entry.grid(row=1, column=1)

        
        tk.Button(root, text="Login", command=self.login).grid(row=2, columnspan=2)

    def login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if usuario == "admin" and senha == "123":
            messagebox.showinfo("Sucesso", "Login bem-sucedido como administrador!")
            self.root.destroy()  
            self.abrir_app("admin")  
        elif usuario == "funcionario" and senha == "1234":
            messagebox.showinfo("Sucesso", "Login bem-sucedido como funcionário!")
            self.root.destroy()  
            self.abrir_app("funcionario")  
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def abrir_app(self, tipo_usuario):
        root = tk.Tk()
        if tipo_usuario == "admin":
            app = CadastroClientesApp(root)
        elif tipo_usuario == "funcionario":
            app = CadastroClientesAppFuncionario(root)
        root.mainloop()

class CadastroClientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")

        
        tk.Label(root, text="RG:").grid(row=0, column=0, sticky="e")
        self.rg_entry = tk.Entry(root)
        self.rg_entry.grid(row=0, column=1)

        tk.Label(root, text="CPF:").grid(row=1, column=0, sticky="e")
        self.cpf_entry = tk.Entry(root)
        self.cpf_entry.grid(row=1, column=1)

        tk.Label(root, text="Nome:").grid(row=2, column=0, sticky="e")
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=2, column=1)

        tk.Label(root, text="Data de Cadastro:").grid(row=3, column=0, sticky="e")
        self.data_cadastro_entry = tk.Entry(root)
        self.data_cadastro_entry.grid(row=3, column=1)

        tk.Label(root, text="Endereço:").grid(row=4, column=0, sticky="e")
        self.endereco_entry = tk.Entry(root)
        self.endereco_entry.grid(row=4, column=1)

        tk.Label(root, text="Telefone:").grid(row=5, column=0, sticky="e")
        self.telefone_entry = tk.Entry(root)
        self.telefone_entry.grid(row=5, column=1)

        tk.Label(root, text="E-mail:").grid(row=6, column=0, sticky="e")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=6, column=1)

        
        tk.Button(root, text="Cadastrar Cliente", command=self.cadastrar_cliente).grid(row=7, columnspan=2)

    def cadastrar_cliente(self):
        rg = self.rg_entry.get()
        cpf = self.cpf_entry.get()
        nome = self.nome_entry.get()
        data_cadastro = self.data_cadastro_entry.get()
        endereco = self.endereco_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()

        
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO clientes (rg, cpf, nome, data_cadastro, endereco, telefone, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (rg, cpf, nome, data_cadastro, endereco, telefone, email))
            conn.commit()
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {err}")
        finally:
            cursor.close()
            conn.close()

class CadastroClientesAppFuncionario:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes (Funcionário)")

        
        tk.Label(root, text="RG:").grid(row=0, column=0, sticky="e")
        self.rg_entry = tk.Entry(root)
        self.rg_entry.grid(row=0, column=1)

        tk.Label(root, text="CPF:").grid(row=1, column=0, sticky="e")
        self.cpf_entry = tk.Entry(root)
        self.cpf_entry.grid(row=1, column=1)

        tk.Label(root, text="Nome:").grid(row=2, column=0, sticky="e")
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=2, column=1)

        tk.Label(root, text="Data de Cadastro:").grid(row=3, column=0, sticky="e")
        self.data_cadastro_entry = tk.Entry(root)
        self.data_cadastro_entry.grid(row=3, column=1)

        tk.Label(root, text="Endereço:").grid(row=4, column=0, sticky="e")
        self.endereco_entry = tk.Entry(root)
        self.endereco_entry.grid(row=4, column=1)

        tk.Label(root, text="Telefone:").grid(row=5, column=0, sticky="e")
        self.telefone_entry = tk.Entry(root)
        self.telefone_entry.grid(row=5, column=1)

        tk.Label(root, text="E-mail:").grid(row=6, column=0, sticky="e")
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=6, column=1)

        
        tk.Button(root, text="Cadastrar Cliente", command=self.cadastrar_cliente).grid(row=7, columnspan=2)

    def cadastrar_cliente(self):
        rg = self.rg_entry.get()
        cpf = self.cpf_entry.get()
        nome = self.nome_entry.get()
        data_cadastro = self.data_cadastro_entry.get()
        endereco = self.endereco_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()

        
        conn = conectar_bd()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO clientes (rg, cpf, nome, data_cadastro, endereco, telefone, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (rg, cpf, nome, data_cadastro, endereco, telefone, email))
            conn.commit()
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {err}")
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    criar_tabelas() 
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()