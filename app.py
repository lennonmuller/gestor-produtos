from tkinter import ttk
from tkinter import *
import sqlite3

class Produto:
    # Caminho da base de dados SQLite
    db = 'database/produtos.db'

    def __init__(self, root):
        # Configuração da janela principal
        self.janela = root
        self.janela.title("App Gestor de Produtos")
        self.janela.resizable(1, 1)
        self.janela.wm_iconbitmap('recursos/icon.ico')
        root.geometry("400x550")

        # Estilo global para botões e widgets
        style = ttk.Style()
        style.configure('my.TButton', font=('Calibri', 14, 'bold'))
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

        # Frame principal do formulário
        frame = LabelFrame(self.janela, text="Registar um novo Produto", font=('Calibri', 16, 'bold'))
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Campo Nome
        Label(frame, text="Nome: ", font=('Calibri', 13)).grid(row=1, column=0)
        self.nome = Entry(frame, font=('Calibri', 13))
        self.nome.grid(row=1, column=1)
        self.nome.focus()

        # Campo Preço
        Label(frame, text="Preço: ", font=('Calibri', 13)).grid(row=2, column=0)
        self.preco = Entry(frame, font=('Calibri', 13))
        self.preco.grid(row=2, column=1)

        # Botão Guardar Produto
        self.botao_adicionar = ttk.Button(frame, text="Guardar Produto", style='my.TButton', command=self.add_produto)
        self.botao_adicionar.grid(row=3, columnspan=2, sticky=W + E)

        # Mensagem de feedback para o utilizador
        self.mensagem = Label(text='', fg='red', font=('Calibri', 12))
        self.mensagem.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Tabela de produtos
        self.tabela = ttk.Treeview(height=15, columns=2, style="mystyle.Treeview")
        self.tabela.grid(row=4, column=0, columnspan=2)
        self.tabela.heading('#0', text='Nome', anchor=CENTER)
        self.tabela.heading('#1', text='Preço', anchor=CENTER)

        # Botões Editar e Eliminar
        ttk.Button(text='ELIMINAR', style='my.TButton', command=self.del_produto).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='EDITAR', style='my.TButton', command=self.edit_produto).grid(row=5, column=1, sticky=W + E)

        # Carregar dados ao iniciar
        self.get_produtos()

    # Conexão com o banco de dados
    def db_consulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(consulta, parametros)
            con.commit()
        return resultado

    # Listar os produtos na tabela
    def get_produtos(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        query = 'SELECT * FROM produto ORDER BY nome DESC'
        registos = self.db_consulta(query)
        for linha in registos:
            self.tabela.insert('', 0, text=linha[1], values=linha[2])

    # Verificação se o campo Nome está preenchido
    def validacao_nome(self):
        return len(self.nome.get().strip()) != 0

    # Verificação se o campo Preço está preenchido
    def validacao_preco(self):
        return len(self.preco.get().strip()) != 0

    # Adicionar novo produto ao banco de dados
    def add_produto(self):
        if self.validacao_nome() and self.validacao_preco():
            query = 'INSERT INTO produto VALUES (NULL, ?, ?)'
            parametros = (self.nome.get(), self.preco.get())
            self.db_consulta(query, parametros)
            self.mensagem['text'] = f'Produto {self.nome.get()} adicionado com êxito'
            self.nome.delete(0, END)
            self.preco.delete(0, END)
        elif self.validacao_nome() and not self.validacao_preco():
            self.mensagem['text'] = 'O preço é obrigatório'
        elif not self.validacao_nome() and self.validacao_preco():
            self.mensagem['text'] = 'O nome é obrigatório'
        else:
            self.mensagem['text'] = 'O nome e o preço são obrigatórios'
        self.get_produtos()

    # Eliminar produto selecionado
    def del_produto(self):
        self.mensagem['text'] = ''
        try:
            nome = self.tabela.item(self.tabela.selection())['text']
        except IndexError:
            self.mensagem['text'] = 'Por favor, selecione um produto'
            return
        query = 'DELETE FROM produto WHERE nome = ?'
        self.db_consulta(query, (nome,))
        self.mensagem['text'] = f'Produto {nome} eliminado com êxito'
        self.get_produtos()

    # Abrir janela para editar produto
    def edit_produto(self):
        self.mensagem['text'] = ''
        try:
            nome = self.tabela.item(self.tabela.selection())['text']
            old_preco = self.tabela.item(self.tabela.selection())['values'][0]
        except IndexError:
            self.mensagem['text'] = 'Por favor, selecione um produto'
            return

        self.janela_editar = Toplevel()
        self.janela_editar.title('Editar Produto')
        self.janela_editar.resizable(1, 1)
        self.janela_editar.wm_iconbitmap('recursos/icon.ico')

        Label(self.janela_editar, text='Edição de Produtos', font=('Calibri', 20, 'bold')).grid(column=0, row=0)

        frame_ep = LabelFrame(self.janela_editar, text="Editar Produto", font=('Calibri', 14, 'bold'))
        frame_ep.grid(row=1, column=0, columnspan=20, pady=20)

        # Nome antigo (readonly)
        Label(frame_ep, text="Nome antigo: ", font=('Calibri', 12)).grid(row=2, column=0)
        self.input_nome_antigo = Entry(frame_ep, textvariable=StringVar(self.janela_editar, value=nome), state='readonly', font=('Calibri', 12))
        self.input_nome_antigo.grid(row=2, column=1)

        # Nome novo
        Label(frame_ep, text="Nome novo: ", font=('Calibri', 12)).grid(row=3, column=0)
        self.input_nome_novo = Entry(frame_ep, font=('Calibri', 12))
        self.input_nome_novo.grid(row=3, column=1)
        self.input_nome_novo.focus()

        # Preço antigo (readonly)
        Label(frame_ep, text="Preço antigo: ", font=('Calibri', 12)).grid(row=4, column=0)
        self.input_preco_antigo = Entry(frame_ep, textvariable=StringVar(self.janela_editar, value=old_preco), state='readonly', font=('Calibri', 12))
        self.input_preco_antigo.grid(row=4, column=1)

        # Preço novo
        Label(frame_ep, text="Preço novo: ", font=('Calibri', 12)).grid(row=5, column=0)
        self.input_preco_novo = Entry(frame_ep, font=('Calibri', 12))
        self.input_preco_novo.grid(row=5, column=1)

        # Botão de atualizar
        ttk.Button(frame_ep, text="Atualizar Produto", style='my.TButton',
                   command=lambda: self.atualizar_produtos(
                       self.input_nome_novo.get(),
                       self.input_nome_antigo.get(),
                       self.input_preco_novo.get(),
                       self.input_preco_antigo.get())
                   ).grid(row=6, columnspan=2, sticky=W + E)

    # Atualizar produto no banco
    def atualizar_produtos(self, novo_nome, antigo_nome, novo_preco, antigo_preco):
        produto_modificado = False
        query = 'UPDATE produto SET nome = ?, preco = ? WHERE nome = ? AND preco = ?'
        if novo_nome and novo_preco:
            parametros = (novo_nome, novo_preco, antigo_nome, antigo_preco)
            produto_modificado = True
        elif novo_nome and not novo_preco:
            parametros = (novo_nome, antigo_preco, antigo_nome, antigo_preco)
            produto_modificado = True
        elif not novo_nome and novo_preco:
            parametros = (antigo_nome, novo_preco, antigo_nome, antigo_preco)
            produto_modificado = True

        if produto_modificado:
            self.db_consulta(query, parametros)
            self.janela_editar.destroy()
            self.mensagem['text'] = f'O produto {antigo_nome} foi atualizado com êxito'
            self.get_produtos()
        else:
            self.janela_editar.destroy()
            self.mensagem['text'] = f'O produto {antigo_nome} NÃO foi atualizado'


# Execução da aplicação
if __name__ == '__main__':
    root = Tk()
    app = Produto(root)
    root.mainloop()
