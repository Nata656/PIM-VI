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
        CREATE TABLE IF NOT EXISTS vendas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            codigo_venda VARCHAR(36),
            nome_cliente VARCHAR(100),
            cpf_cliente VARCHAR(20),
            codigo_prod VARCHAR(20),
            nome_produto VARCHAR(100),
            quantidade INT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_cliente VARCHAR(100),
            cpf_cliente VARCHAR(20)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            codigo_prod VARCHAR(20),
            nome_produto VARCHAR(100)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

criar_tabelas()

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
            self.abrir_app() 
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    def abrir_app(self):
        root = tk.Tk()
        app = ConsultaApp(root)
        root.mainloop()

class ConsultaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consulta de Tabelas")

        
        tk.Button(root, text="Consultar Vendas", command=self.consultar_vendas).grid(row=0, column=0)
        tk.Button(root, text="Consultar Clientes", command=self.consultar_clientes).grid(row=1, column=0)
        tk.Button(root, text="Consultar Produtos", command=self.consultar_produtos).grid(row=2, column=0)

    def consultar_vendas(self):
        self.consultar_tabela("vendas")

    def consultar_clientes(self):
        self.consultar_tabela("clientes")

    def consultar_produtos(self):
        self.consultar_tabela("produtos")

    def consultar_tabela(self, tabela):
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tabela}")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()

       
        resultado_janela = tk.Toplevel(self.root)
        resultado_janela.title(f"Resultados - {tabela.capitalize()}")
        
        for i, linha in enumerate(resultados):
            for j, valor in enumerate(linha):
                tk.Label(resultado_janela, text=str(valor)).grid(row=i, column=j)


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()