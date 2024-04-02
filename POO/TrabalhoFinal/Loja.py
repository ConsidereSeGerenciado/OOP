import tkinter as tk
from tkinter import messagebox
import random


class Produto:
    def __init__(self, codigo, descricao, precoCompra, valorVenda, quantidade, vendas):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__precoCompra = precoCompra
        self.__valorVenda = valorVenda
        self.__quantidade = quantidade
        self.__vendas = vendas

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def precoCompra(self):
        return self.__precoCompra

    @property
    def valorVenda(self):
        return self.__valorVenda

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, qtd):
        self.__quantidade += qtd

    @property
    def vendas(self):
        return self.__vendas

    @vendas.setter
    def vendas(self, qtd):
        self.__vendas += qtd


class Cliente:
    def __init__(self, nome, endereco, email, CPF):
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email
        self.__CPF = CPF

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def email(self):
        return self.__email

    @property
    def CPF(self):
        return self.__CPF


class NotaFiscalCliente:
    def __init__(self, CPF, codigo, valorGasto, quantidade, dataEmissao, valorUnico):
        self.__CPF = CPF
        self.__codigo = codigo
        self.__valorGasto = valorGasto
        self.__quantidade = quantidade
        self.__dataEmissao = dataEmissao
        self.__valorUnico = valorUnico

    @property
    def CPF(self):
        return self.__CPF

    @property
    def codigo(self):
        return self.__codigo

    @property
    def valorGasto(self):
        return self.__valorGasto

    @valorGasto.setter
    def valorGasto(self, valorGasto):
        self.__valorGasto = valorGasto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, qtd):
        self.__quantidade += qtd

    @property
    def dataEmissao(self):
        return self.__dataEmissao

    @dataEmissao.setter
    def dataEmissao(self, data):
        self.__dataEmissao = data

    @property
    def valorUnico(self):
        return self.__valorUnico


class Vendas:
    def __init__(self, CPF, codigo, quantidade, valorTotal):
        self.__CPF = CPF
        self.__codigo = codigo
        self.__quantidade = quantidade
        self.__valorTotal = valorTotal

    @property
    def CPF(self):
        return self.__CPF

    @property
    def codigo(self):
        return self.__codigo

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def valorTotal(self):
        return self.__valorTotal


class LucroLiquido:
    def __init__(self, valorGasto, valorGanho, dataEmissao):
        self.__valorGasto = valorGasto
        self.__valorGanho = valorGanho
        self.__dataEmissao = dataEmissao

    @property
    def valorGasto(self):
        return self.__valorGasto

    @valorGasto.setter
    def valorGasto(self, valorGasto):
        self.__valorGasto += valorGasto

    @property
    def valorGanho(self):
        return self.__valorGanho

    @valorGanho.setter
    def valorGanho(self, ganho):
        self.__valorGanho += ganho

    @property
    def dataEmissao(self):
        return self.__dataEmissao

    @dataEmissao.setter
    def dataEmissao(self, dia):
        self.__dataEmissao = dia


class InsereProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('350x250')
        self.title("Adicionar Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framePrecoCompra = tk.Frame(self)
        self.frameValorVenda = tk.Frame(self)
        self.frameQuantidade = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.framePrecoCompra.pack()
        self.frameValorVenda.pack()
        self.frameQuantidade.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelDescricao = tk.Label(self.frameDescricao, text="Descrição: ")
        self.labelPrecoCompra = tk.Label(self.framePrecoCompra, text="Preço de compra: ")
        self.labelValorVenda = tk.Label(self.frameValorVenda, text="Valor de venda: ")
        self.labelQuantidade = tk.Label(self.frameQuantidade, text="Quantidade: ")
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelPrecoCompra.pack(side="left")
        self.labelValorVenda.pack(side="left")
        self.labelQuantidade.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputDescricao = tk.Entry(self.frameDescricao, width=10)
        self.inputPrecoCompra = tk.Entry(self.framePrecoCompra, width=10)
        self.inputValorVenda = tk.Entry(self.frameValorVenda, width=10)
        self.inputQuantidade = tk.Entry(self.frameQuantidade, width=10)
        self.inputCodigo.pack(side="left")
        self.inputDescricao.pack(side="left")
        self.inputPrecoCompra.pack(side="left")
        self.inputValorVenda.pack(side="left")
        self.inputQuantidade.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Adicionar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.adicionar)

        self.buttonClear = tk.Button(self.frameButton, text="Limpar")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.limparProduto)

        self.buttonFecha = tk.Button(self.frameButton, text="Finalizar")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.finalizarProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ConsultarProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle

        self.framenroCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.framenroCodigo, text="Codigo: ")
        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.framenroCodigo, width=10)
        self.inputCodigo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.pesquisarProduto)

        self.buttonSubmit = tk.Button(self.frameButton, text="Todos")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.todasConsultas)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparConsulta)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarConsulta)

        self.frameProduto = tk.Frame(self)
        self.frameProduto.pack()
        self.textProduto = tk.Text(self.frameProduto, height=50, width=50)
        self.textProduto.pack()
        self.textProduto.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CadastrarCleinte(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('350x250')
        self.title("Cadastrar Cliente")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameEndereco = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameCPF = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameNome.pack()
        self.frameEndereco.pack()
        self.frameEmail.pack()
        self.frameCPF.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelEndereco = tk.Label(self.frameEndereco, text="Endereço: ")
        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelCPF = tk.Label(self.frameCPF, text="CPF: ")
        self.labelNome.pack(side="left")
        self.labelEndereco.pack(side="left")
        self.labelEmail.pack(side="left")
        self.labelCPF.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=10)
        self.inputEndereco = tk.Entry(self.frameEndereco, width=10)
        self.inputEmail = tk.Entry(self.frameEmail, width=10)
        self.inputCPF = tk.Entry(self.frameCPF, width=10)
        self.inputNome.pack(side="left")
        self.inputEndereco.pack(side="left")
        self.inputEmail.pack(side="left")
        self.inputCPF.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.adicionarcliente)

        self.buttonClear = tk.Button(self.frameButton, text="Limpar")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.limparclientecad)

        self.buttonFecha = tk.Button(self.frameButton, text="Finalizar")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.finalizarclientecad)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ConsultarCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle

        self.framenroCPF = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroCPF.pack()
        self.frameButton.pack()

        self.labelCPF = tk.Label(self.framenroCPF, text="CPF: ")
        self.labelCPF.pack(side="left")

        self.inputCPF = tk.Entry(self.framenroCPF, width=10)
        self.inputCPF.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultarcliente)

        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastrarCliente)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparcliente)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarcliente)

        self.frameCliente = tk.Frame(self)
        self.frameCliente.pack()
        self.textCliente = tk.Text(self.frameCliente, height=50, width=50)
        self.textCliente.pack()
        self.textCliente.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class FaturamentoProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle

        self.framenroCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.framenroCodigo, text="Codigo: ")
        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.framenroCodigo, width=10)
        self.inputCodigo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultarfaturamentoproduto)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparfaturamentoproduto)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarfaturamentoproduto)

        self.frameProduto = tk.Frame(self)
        self.frameProduto.pack()
        self.textProduto = tk.Text(self.frameProduto, height=50, width=50)
        self.textProduto.pack()
        self.textProduto.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class FaturamentoCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle

        self.framenroCPF = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroCPF.pack()
        self.frameButton.pack()

        self.labelCPF = tk.Label(self.framenroCPF, text="CPF: ")
        self.labelCPF.pack(side="left")

        self.inputCPF = tk.Entry(self.framenroCPF, width=10)
        self.inputCPF.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultarfaturamentocliente)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparfaturamentocliente)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarfaturamentocliente)

        self.frameCliente = tk.Frame(self)
        self.frameCliente.pack()
        self.textCliente = tk.Text(self.frameCliente, height=50, width=50)
        self.textCliente.pack()
        self.textCliente.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class FaturamentoPeriodo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle

        self.framenroDiaInicial = tk.Frame(self)
        self.framenroMesInicial = tk.Frame(self)
        self.framenroAnoInicial = tk.Frame(self)
        self.framenroDiaFinal = tk.Frame(self)
        self.framenroMesFinal = tk.Frame(self)
        self.framenroAnoFinal = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroDiaInicial.pack()
        self.framenroMesInicial.pack()
        self.framenroAnoInicial.pack()
        self.framenroDiaFinal.pack()
        self.framenroMesFinal.pack()
        self.framenroAnoFinal.pack()
        self.frameButton.pack()

        self.labelDiaInicial = tk.Label(self.framenroDiaInicial, text="Dia Inicial: ")
        self.labelMesInicial = tk.Label(self.framenroMesInicial, text="Mes Inicial: ")
        self.labelAnoInicial = tk.Label(self.framenroAnoInicial, text="Ano Inicial: ")
        self.labelDiaFinal = tk.Label(self.framenroDiaFinal, text="Dia Final: ")
        self.labelMesFinal = tk.Label(self.framenroMesFinal, text="Mes Final: ")
        self.labelAnoFinal = tk.Label(self.framenroAnoFinal, text="Ano Final: ")
        self.labelDiaInicial.pack(side="left")
        self.labelMesInicial.pack(side="left")
        self.labelAnoInicial.pack(side="left")
        self.labelDiaFinal.pack(side="left")
        self.labelMesFinal.pack(side="left")
        self.labelAnoFinal.pack(side="left")

        self.inputDiaInicial = tk.Entry(self.framenroDiaInicial, width=10)
        self.inputMesInicial = tk.Entry(self.framenroMesInicial, width=10)
        self.inputAnoInicial = tk.Entry(self.framenroAnoInicial, width=10)
        self.inputDiaFinal = tk.Entry(self.framenroDiaFinal, width=10)
        self.inputMesFinal = tk.Entry(self.framenroMesFinal, width=10)
        self.inputAnoFinal = tk.Entry(self.framenroAnoFinal, width=10)
        self.inputDiaInicial.pack(side="left")
        self.inputMesInicial.pack(side="left")
        self.inputAnoInicial.pack(side="left")
        self.inputDiaFinal.pack(side="left")
        self.inputMesFinal.pack(side="left")
        self.inputAnoFinal.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Verificar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.verificafaturamentoperiodo)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparfaturamentoperiodo)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarfaturamentoperiodo)

        self.framePeriodo = tk.Frame(self)
        self.framePeriodo.pack()
        self.textPeriodo = tk.Text(self.framePeriodo, height=50, width=50)
        self.textPeriodo.pack()
        self.textPeriodo.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class PeriodLucroLiquido(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle

        self.framenroDiaInicial = tk.Frame(self)
        self.framenroMesInicial = tk.Frame(self)
        self.framenroAnoInicial = tk.Frame(self)
        self.framenroDiaFinal = tk.Frame(self)
        self.framenroMesFinal = tk.Frame(self)
        self.framenroAnoFinal = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroDiaInicial.pack()
        self.framenroMesInicial.pack()
        self.framenroAnoInicial.pack()
        self.framenroDiaFinal.pack()
        self.framenroMesFinal.pack()
        self.framenroAnoFinal.pack()
        self.frameButton.pack()

        self.labelDiaInicial = tk.Label(self.framenroDiaInicial, text="Dia Inicial: ")
        self.labelMesInicial = tk.Label(self.framenroMesInicial, text="Mes Inicial: ")
        self.labelAnoInicial = tk.Label(self.framenroAnoInicial, text="Ano Inicial: ")
        self.labelDiaFinal = tk.Label(self.framenroDiaFinal, text="Dia Final: ")
        self.labelMesFinal = tk.Label(self.framenroMesFinal, text="Mes Final: ")
        self.labelAnoFinal = tk.Label(self.framenroAnoFinal, text="Ano Final: ")
        self.labelDiaInicial.pack(side="left")
        self.labelMesInicial.pack(side="left")
        self.labelAnoInicial.pack(side="left")
        self.labelDiaFinal.pack(side="left")
        self.labelMesFinal.pack(side="left")
        self.labelAnoFinal.pack(side="left")

        self.inputDiaInicial = tk.Entry(self.framenroDiaInicial, width=10)
        self.inputMesInicial = tk.Entry(self.framenroMesInicial, width=10)
        self.inputAnoInicial = tk.Entry(self.framenroAnoInicial, width=10)
        self.inputDiaFinal = tk.Entry(self.framenroDiaFinal, width=10)
        self.inputMesFinal = tk.Entry(self.framenroMesFinal, width=10)
        self.inputAnoFinal = tk.Entry(self.framenroAnoFinal, width=10)
        self.inputDiaInicial.pack(side="left")
        self.inputMesInicial.pack(side="left")
        self.inputAnoInicial.pack(side="left")
        self.inputDiaFinal.pack(side="left")
        self.inputMesFinal.pack(side="left")
        self.inputAnoFinal.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Verificar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.verificalucroliquido)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparlucroliquido)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarlucroliquido)

        self.framePeriodo = tk.Frame(self)
        self.framePeriodo.pack()
        self.textPeriodo = tk.Text(self.framePeriodo, height=50, width=50)
        self.textPeriodo.pack()
        self.textPeriodo.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ClientePeriodo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle

        self.framenroCPF = tk.Frame(self)
        self.framenroDiaInicial = tk.Frame(self)
        self.framenroMesInicial = tk.Frame(self)
        self.framenroAnoInicial = tk.Frame(self)
        self.framenroDiaFinal = tk.Frame(self)
        self.framenroMesFinal = tk.Frame(self)
        self.framenroAnoFinal = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroCPF.pack()
        self.framenroDiaInicial.pack()
        self.framenroMesInicial.pack()
        self.framenroAnoInicial.pack()
        self.framenroDiaFinal.pack()
        self.framenroMesFinal.pack()
        self.framenroAnoFinal.pack()
        self.frameButton.pack()

        self.labelCPF = tk.Label(self.framenroCPF, text="CPF: ")
        self.labelDiaInicial = tk.Label(self.framenroDiaInicial, text="Dia Inicial: ")
        self.labelMesInicial = tk.Label(self.framenroMesInicial, text="Mes Inicial: ")
        self.labelAnoInicial = tk.Label(self.framenroAnoInicial, text="Ano Inicial: ")
        self.labelDiaFinal = tk.Label(self.framenroDiaFinal, text="Dia Final: ")
        self.labelMesFinal = tk.Label(self.framenroMesFinal, text="Mes Final: ")
        self.labelAnoFinal = tk.Label(self.framenroAnoFinal, text="Ano Final: ")
        self.labelCPF.pack(side="left")
        self.labelDiaInicial.pack(side="left")
        self.labelMesInicial.pack(side="left")
        self.labelAnoInicial.pack(side="left")
        self.labelDiaFinal.pack(side="left")
        self.labelMesFinal.pack(side="left")
        self.labelAnoFinal.pack(side="left")

        self.inputCPF = tk.Entry(self.framenroCPF, width=10)
        self.inputDiaInicial = tk.Entry(self.framenroDiaInicial, width=10)
        self.inputMesInicial = tk.Entry(self.framenroMesInicial, width=10)
        self.inputAnoInicial = tk.Entry(self.framenroAnoInicial, width=10)
        self.inputDiaFinal = tk.Entry(self.framenroDiaFinal, width=10)
        self.inputMesFinal = tk.Entry(self.framenroMesFinal, width=10)
        self.inputAnoFinal = tk.Entry(self.framenroAnoFinal, width=10)
        self.inputCPF.pack(side="left")
        self.inputDiaInicial.pack(side="left")
        self.inputMesInicial.pack(side="left")
        self.inputAnoInicial.pack(side="left")
        self.inputDiaFinal.pack(side="left")
        self.inputMesFinal.pack(side="left")
        self.inputAnoFinal.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Verificar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.verificaclienteperiodo)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparclienteperiodo)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarclienteperiodo)

        self.frameClientePeriodo = tk.Frame(self)
        self.frameClientePeriodo.pack()
        self.textClientePeriodo = tk.Text(self.frameClientePeriodo, height=50, width=50)
        self.textClientePeriodo.pack()
        self.textClientePeriodo.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class NotaFiscal(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('350x100')
        self.title("Consulta")
        self.controle = controle

        self.framenroCPF = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroCPF.pack()
        self.frameButton.pack()

        self.labelCPF = tk.Label(self.framenroCPF, text="CPF: ")
        self.labelCPF.pack(side="left")

        self.inputCPF = tk.Entry(self.framenroCPF, width=10)
        self.inputCPF.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultarCPFnotaFiscal)

        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastrarCliente)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparCPFnotaFiscal)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarCPFnotaFiscal)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ProdutosNotaFiscal(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle

        self.framenroCodigo = tk.Frame(self)
        self.framenroQuantidade = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroCodigo.pack()
        self.framenroQuantidade.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.framenroCodigo, text="Codigo: ")
        self.labelQuantidade = tk.Label(self.framenroQuantidade, text="Quantidade: ")
        self.labelCodigo.pack(side="left")
        self.labelQuantidade.pack(side="left")

        self.inputCodigo = tk.Entry(self.framenroCodigo, width=10)
        self.inputQuantidade = tk.Entry(self.framenroQuantidade, width=10)
        self.inputCodigo.pack(side="left")
        self.inputQuantidade.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Adicionar ao carrinho")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.adicionaraocarrinho)

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.pesquisarprodutonotafiscal)

        self.buttonSubmit = tk.Button(self.frameButton, text="Cancelar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cancelarnotafiscal)

        self.buttonSubmit = tk.Button(self.frameButton, text="Emitir nota fiscal")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.emitirnotafiscal)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class mostrarCarrinho(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Carinho de Compras")
        self.controle = controle
        self.frameCarrinho = tk.Frame(self)
        self.frameCarrinho.pack()
        self.textCarrinho = tk.Text(self.frameCarrinho, height=50, width=50)
        self.textCarrinho.pack()
        self.textCarrinho.config(state=tk.DISABLED)


class ConsultarProdunoNotaFiscal(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('350x100')
        self.title("Consulta")
        self.controle = controle

        self.framenroCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.framenroCodigo, text="Codigo: ")
        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.framenroCodigo, width=10)
        self.inputCodigo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultarprodutonotafiscal)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limparprodutonotafiscal)

        self.buttonSubmit = tk.Button(self.frameButton, text="Finalizar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.finalizarprodutonotafiscal)

        self.frameProdutos = tk.Frame(self)
        self.frameProdutos.pack()
        self.textProdutos = tk.Text(self.frameProdutos, height=50, width=50)
        self.textProdutos.pack()
        self.textProdutos.config(state=tk.DISABLED)


class EmitirNotaFiscal(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('350x100')
        self.title("Consulta")
        self.controle = controle

        self.framenroDia = tk.Frame(self)
        self.framenroMes = tk.Frame(self)
        self.framenroAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroDia.pack()
        self.framenroMes.pack()
        self.framenroAno.pack()
        self.frameButton.pack()

        self.labelDia = tk.Label(self.framenroDia, text="Dia: ")
        self.labelMes = tk.Label(self.framenroMes, text="Mes: ")
        self.labelAno = tk.Label(self.framenroAno, text="Ano: ")
        self.labelDia.pack(side="left")
        self.labelMes.pack(side="left")
        self.labelAno.pack(side="left")

        self.inputDia = tk.Entry(self.framenroDia, width=10)
        self.inputMes = tk.Entry(self.framenroMes, width=10)
        self.inputAno = tk.Entry(self.framenroAno, width=10)
        self.inputDia.pack(side="left")
        self.inputMes.pack(side="left")
        self.inputAno.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Adicionar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.adicionardatanotafiscal)

        self.buttonSubmit = tk.Button(self.frameButton, text="Limpar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.limpardatanotafiscal)

        self.buttonSubmit = tk.Button(self.frameButton, text="Emitir nota fiscal")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.concluirnotafiscal)


class EmissaoNotaFiscal(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Nota Fiscal")
        self.controle = controle

        self.framenroDia = tk.Frame(self)
        self.framenroMes = tk.Frame(self)
        self.framenroAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framenroDia.pack()
        self.framenroMes.pack()
        self.framenroAno.pack()
        self.frameButton.pack()

        self.labelDia = tk.Label(self.framenroDia, text="Dia: ")
        self.labelMes = tk.Label(self.framenroMes, text="Mes: ")
        self.labelAno = tk.Label(self.framenroAno, text="Ano: ")
        self.labelDia.pack(side="left")
        self.labelMes.pack(side="left")
        self.labelAno.pack(side="left")

        self.inputDia = tk.Entry(self.framenroDia, width=10)
        self.inputMes = tk.Entry(self.framenroMes, width=10)
        self.inputAno = tk.Entry(self.framenroAno, width=10)
        self.inputDia.pack(side="left")
        self.inputMes.pack(side="left")
        self.inputAno.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Adicionar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.adicionardatanotafiscal)

        self.frameNotaFiscal = tk.Frame(self)
        self.frameNotaFiscal.pack()
        self.textNotaFiscal = tk.Text(self.frameNotaFiscal, height=50, width=50)
        self.textNotaFiscal.pack()
        self.textNotaFiscal.config(state=tk.DISABLED)


class MaisVendidos(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('450x250')
        self.title("Consulta")
        self.controle = controle
        self.frameMaisVendidos = tk.Frame(self)
        self.frameMaisVendidos.pack()
        self.textMaisVendidos = tk.Text(self.frameMaisVendidos, height=50, width=50)
        self.textMaisVendidos.pack()
        self.textMaisVendidos.config(state=tk.DISABLED)


class Controle:
    def __init__(self, controlador):
        self.consultaCliente = None
        self.cadastrarcliente = None
        self.maisvendidos = None
        self.consultaProduto = None
        self.mercadoria = None
        self.controlador = controlador
        self.listaProduto = []
        self.listaCliente = []
        self.listaNotaFiscal = []
        self.listaLucroLiquido = []
        self.listaVendas = []

    def adicionarProduto(self):
        self.mercadoria = InsereProduto(self)

    def adicionar(self, event):
        codigo = self.mercadoria.inputCodigo.get()
        descricao = self.mercadoria.inputDescricao.get()
        compra = self.mercadoria.inputPrecoCompra.get()
        venda = self.mercadoria.inputValorVenda.get()
        quantidade = self.mercadoria.inputQuantidade.get()

        info = 0
        for mercadorias in self.listaProduto:
            if mercadorias.codigo == codigo:
                mercadorias.quantidade = int(quantidade)
                for lucro in self.listaLucroLiquido:
                    lucro.valorGanho = mercadorias.quantidade * mercadorias.precoCompra
                info = 1
        if info == 0:
            mercadoria = Produto(codigo, descricao, int(compra), int(venda), int(quantidade), 0)
            self.listaProduto.append(mercadoria)

        self.mercadoria.mostraJanela('Sucesso', 'Produto Adicionada')
        self.limparProduto(event)

    def limparProduto(self, event):
        self.mercadoria.inputCodigo.delete(0, len(self.mercadoria.inputCodigo.get()))
        self.mercadoria.inputDescricao.delete(0, len(self.mercadoria.inputDescricao.get()))
        self.mercadoria.inputPrecoCompra.delete(0, len(self.mercadoria.inputPrecoCompra.get()))
        self.mercadoria.inputValorVenda.delete(0, len(self.mercadoria.inputValorVenda.get()))
        self.mercadoria.inputQuantidade.delete(0, len(self.mercadoria.inputQuantidade.get()))

    def finalizarProduto(self, event):
        self.mercadoria.destroy()

    def consultarProduto(self):
        self.consultaProduto = ConsultarProduto(self)

    def pesquisarProduto(self, event):
        codigo = self.consultaProduto.inputCodigo.get()
        achou = 0
        for mercadorias in self.listaProduto:
            if mercadorias.codigo == codigo:
                self.consultaProduto.textProduto.config(state=tk.NORMAL)
                self.consultaProduto.textProduto.delete(1.0, tk.END)
                self.consultaProduto.textProduto.insert(tk.END, f"Código: {mercadorias.codigo}. "
                                                                f"Descrição: {mercadorias.descricao}. "
                                                                f"Valor de venda: R${mercadorias.valorVenda},00. "
                                                                f"Quantidade: {mercadorias.quantidade}")
                self.consultaProduto.textProduto.config(state=tk.DISABLED)
                achou = 1
        if achou == 0:
            messagebox.showerror("Error", "Código errado ou produto não cadaastrado na loja")

    def todasConsultas(self, event):
        self.consultaProduto.textProduto.config(state=tk.NORMAL)
        self.consultaProduto.textProduto.delete(1.0, tk.END)
        for mercadorias in self.listaProduto:
            self.consultaProduto.textProduto.insert(tk.END,
                                                    f"Código: {mercadorias.codigo}, "
                                                    f"Descrição: {mercadorias.descricao}, "
                                                    f"Valor de venda: R${mercadorias.valorVenda}.00\n")
        self.consultaProduto.textProduto.config(state=tk.DISABLED)

    def limparConsulta(self, event):
        self.consultaProduto.inputCodigo.delete(0, len(self.consultaProduto.inputCodigo.get()))

    def finalizarConsulta(self, event):
        self.consultaProduto.destroy()

    def cadastrarCliente(self, event):
        self.cadastrarcliente = CadastrarCleinte(self)

    def adicionarcliente(self, event):
        nome = self.cadastrarcliente.inputNome.get()
        endereco = self.cadastrarcliente.inputEndereco.get()
        email = self.cadastrarcliente.inputEmail.get()
        CPF = self.cadastrarcliente.inputCPF.get()

        achou = 0
        for clientes in self.listaCliente:
            if CPF in clientes.CPF:
                messagebox.showerror("Erro", "CPF já existente")
                achou = 1
        if achou == 0:
            cliente = Cliente(nome, endereco, email, CPF)
            self.listaCliente.append(cliente)

        self.cadastrarcliente.mostraJanela('Sucesso', 'Cliente Cadastrado')
        self.limparclientecad(event)

    def limparclientecad(self, event):
        self.cadastrarcliente.inputNome.delete(0, len(self.cadastrarcliente.inputNome.get()))
        self.cadastrarcliente.inputEndereco.delete(0, len(self.cadastrarcliente.inputEndereco.get()))
        self.cadastrarcliente.inputEmail.delete(0, len(self.cadastrarcliente.inputEmail.get()))
        self.cadastrarcliente.inputCPF.delete(0, len(self.cadastrarcliente.inputCPF.get()))

    def finalizarclientecad(self, event):
        self.cadastrarcliente.destroy()

    def consultarCliente(self):
        self.consultaCliente = ConsultarCliente(self)

    def consultarcliente(self, event):
        CPF = self.consultaCliente.inputCPF.get()

        achou = 0
        for cliente in self.listaCliente:
            if cliente.CPF == CPF:
                self.consultaCliente.textCliente.config(state=tk.NORMAL)
                self.consultaCliente.textCliente.delete(1.0, tk.END)
                self.consultaCliente.textCliente.insert(tk.END, f"Nome: {cliente.nome}. "
                                                                f"Endereço: {cliente.endereco}. "
                                                                f"Email: {cliente.email}")
                self.consultaCliente.textCliente.config(state=tk.DISABLED)
                achou = 1

        if achou == 0:
            messagebox.showerror("Error", "Cliente não cadastrado. Necessário cadastrar para realizar consulta.")

    def limparcliente(self, event):
        self.consultaCliente.inputCPF.delete(0, len(self.consultaCliente.inputCPF.get()))

    def finalizarcliente(self, event):
        self.consultaCliente.destroy()

    def faturamentoProduto(self):
        self.faturamentoproduto = FaturamentoProduto(self)

    def consultarfaturamentoproduto(self, event):
        codigo = self.faturamentoproduto.inputCodigo.get()

        achou = 0
        faturamento = 0
        for produto in self.listaProduto:
            if produto.codigo == codigo:
                print(produto.codigo, produto.valorVenda, produto.vendas)
                faturamento = produto.valorVenda * produto.vendas
                achou = 1

        if achou == 1:
            if faturamento > 0:
                self.faturamentoproduto.textProduto.config(state=tk.NORMAL)
                self.faturamentoproduto.textProduto.delete(1.0, tk.END)
                self.faturamentoproduto.textProduto.insert(tk.END,
                                                           f"O produto {codigo} teve faturamento de R${faturamento},00")
                self.faturamentoproduto.textProduto.config(state=tk.DISABLED)
            else:
                messagebox.showinfo("Sem Venda", "O produto não teve nenhuma venda")
        else:
            messagebox.showerror("Erro", "Produto não cadastrado")

    def limparfaturamentoproduto(self, event):
        self.faturamentoproduto.inputCodigo.delete(0, len(self.faturamentoproduto.inputCodigo.get()))

    def finalizarfaturamentoproduto(self, event):
        self.faturamentoproduto.destroy()

    def faturamentoCliente(self):
        self.faturamentocliente = FaturamentoCliente(self)

    def consultarfaturamentocliente(self, event):
        CPF = self.faturamentocliente.inputCPF.get()

        achou = 0
        faturamento = 0
        for cliente in self.listaNotaFiscal:
            if cliente.CPF == CPF:
                faturamento += cliente.valorGasto
                achou = 1

        if achou == 1:
            self.faturamentocliente.textCliente.config(state=tk.NORMAL)
            self.faturamentocliente.textCliente.delete(1.0, tk.END)
            self.faturamentocliente.textCliente.insert(tk.END,
                                                       f"O cliente {CPF} teve faturamento de R${faturamento},00")
            self.faturamentocliente.textCliente.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Erro", "Cliente não encontrado ou não teve nenhum faturamento")

    def limparfaturamentocliente(self, event):
        self.faturamentocliente.inputCPF.delete(0, len(self.faturamentocliente.inputCPF.get()))

    def finalizarfaturamentocliente(self, event):
        self.faturamentocliente.destroy()

    def faturamentoPeriodo(self):
        self.faturamentoperiodo = FaturamentoPeriodo(self)

    def verificafaturamentoperiodo(self, event):
        diaInicial = self.faturamentoperiodo.inputDiaInicial.get()
        mesInicial = self.faturamentoperiodo.inputMesInicial.get()
        anoInicial = self.faturamentoperiodo.inputAnoInicial.get()
        diaFinal = self.faturamentoperiodo.inputDiaFinal.get()
        mesFinal = self.faturamentoperiodo.inputMesFinal.get()
        anoFinal = self.faturamentoperiodo.inputAnoFinal.get()

        inicial = f"{anoInicial}{mesInicial}{diaInicial}"
        fim = f"{anoFinal}{mesFinal}{diaFinal}"

        achou = 0
        faturamento = 0
        for clientes in self.listaNotaFiscal:
            if int(inicial) <= clientes.dataEmissao <= int(fim):
                faturamento += clientes.valorGasto
                achou = 1

        if achou == 1:
            self.faturamentoperiodo.textPeriodo.config(state=tk.NORMAL)
            self.faturamentoperiodo.textPeriodo.delete(1.0, tk.END)
            self.faturamentoperiodo.textPeriodo.insert(tk.END,
                                                       f"O faturamento entre os dias {diaInicial}/{mesInicial}/{anoInicial} e {diaFinal}/{mesFinal}/{anoFinal} teve faturamento de R${faturamento},00")
            self.faturamentoperiodo.textPeriodo.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Erro", "Periodo sem faturamento")

    def limparfaturamentoperiodo(self, event):
        self.faturamentoperiodo.inputDiaInicial.delete(0, len(self.faturamentoperiodo.inputDiaInicial.get()))
        self.faturamentoperiodo.inputDiaFinal.delete(0, len(self.faturamentoperiodo.inputDiaFinal.get()))

    def finalizarfaturamentoperiodo(self, event):
        self.faturamentoperiodo.destroy()

    def lucroLiquido(self):
        self.lucroliquido = PeriodLucroLiquido(self)

    def verificalucroliquido(self, event):
        diaInicial = self.lucroliquido.inputDiaInicial.get()
        mesInicial = self.lucroliquido.inputMesInicial.get()
        anoInicial = self.lucroliquido.inputAnoInicial.get()
        diaFinal = self.lucroliquido.inputDiaFinal.get()
        mesFinal = self.lucroliquido.inputMesFinal.get()
        anoFinal = self.lucroliquido.inputAnoFinal.get()

        inicial = f"{anoInicial}{mesInicial}{diaInicial}"
        fim = f"{anoFinal}{mesFinal}{diaFinal}"

        achou = 0
        lucroliquido = 0
        for lucro in self.listaLucroLiquido:
            if int(inicial) <= lucro.dataEmissao <= int(fim):
                lucroliquido = lucro.valorGanho
                achou = 1

        if achou == 1:
            self.lucroliquido.textPeriodo.config(state=tk.NORMAL)
            self.lucroliquido.textPeriodo.delete(1.0, tk.END)
            self.lucroliquido.textPeriodo.insert(tk.END,
                                                 f"O lucro líquido entre os dias {diaInicial}/{mesInicial}/{anoInicial} e {diaFinal}/{mesFinal}/{anoFinal} foi de R${lucroliquido},00")
            self.lucroliquido.textPeriodo.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Erro", "Periodo sem lucro líquido")

    def limparlucroliquido(self, event):
        self.lucroliquido.inputDiaInicial.delete(0, len(self.lucroliquido.inputDiaInicial.get()))
        self.lucroliquido.inputDiaFinal.delete(0, len(self.lucroliquido.inputDiaFinal.get()))

    def finalizarlucroliquido(self, event):
        self.lucroliquido.destroy()

    def clientePeriodo(self):
        self.clienteperiodo = ClientePeriodo(self)

    def verificaclienteperiodo(self, event):
        CPF = self.clienteperiodo.inputCPF.get()
        diaInicial = self.clienteperiodo.inputDiaInicial.get()
        mesInicial = self.clienteperiodo.inputMesInicial.get()
        anoInicial = self.clienteperiodo.inputAnoInicial.get()
        diaFinal = self.clienteperiodo.inputDiaFinal.get()
        mesFinal = self.clienteperiodo.inputMesFinal.get()
        anoFinal = self.clienteperiodo.inputAnoFinal.get()

        inicial = f"{anoInicial}{mesInicial}{diaInicial}"
        fim = f"{anoFinal}{mesFinal}{diaFinal}"

        achou = 0
        self.clienteperiodo.textClientePeriodo.config(state=tk.NORMAL)
        self.clienteperiodo.textClientePeriodo.delete(1.0, tk.END)
        for clientes in self.listaNotaFiscal:
            if int(inicial) <= clientes.dataEmissao <= int(fim) and clientes.CPF == CPF:
                self.clienteperiodo.textClientePeriodo.insert(tk.END,
                                                              f"Nota fiscal {clientes.valorUnico} com faturamento de R${clientes.valorGasto},00\n")
                achou = 1
        self.clienteperiodo.textClientePeriodo.config(state=tk.DISABLED)
        if achou == 0:
            messagebox.showerror("Erro", "Periodo sem nota fiscal")

    def limparclienteperiodo(self, event):
        self.clienteperiodo.inputCPF.delete(0, len(self.clienteperiodo.inputCPF.get()))
        self.clienteperiodo.inputDiaInicial.delete(0, len(self.clienteperiodo.inputDiaInicial.get()))
        self.clienteperiodo.inputDiaFinal.delete(0, len(self.clienteperiodo.inputDiaFinal.get()))

    def finalizarclienteperiodo(self, event):
        self.clienteperiodo.destroy()

    def noteFiscal(self):
        self.notafiscal = NotaFiscal(self)

    def consultarCPFnotaFiscal(self, event):
        CPF = self.notafiscal.inputCPF.get()

        achou = 0
        for cliente in self.listaCliente:
            if cliente.CPF == CPF:
                messagebox.showinfo("Bem-Vindo!", f"Bom ter você de volta aqui {cliente.nome}")
                self.ProdutosDiferentesNotaFiscal = 0
                self.produtosnotafiscal = ProdutosNotaFiscal(self)
                achou = 1
        if achou == 0:
            messagebox.showerror("Error", "Cliente não cadastrado. Necessário cadastrar para emitir nota fiscal.")

    def adicionaraocarrinho(self, event):
        if self.ProdutosDiferentesNotaFiscal < 10:
            CPF = self.notafiscal.inputCPF.get()
            codigo = self.produtosnotafiscal.inputCodigo.get()
            quantidade = self.produtosnotafiscal.inputQuantidade.get()
            maior = 0
            achou = 0
            info = 0
            if self.ProdutosDiferentesNotaFiscal > 0:
                for produto in self.listaProduto:
                    for fiscalcliente in self.listaNotaFiscal:
                        if fiscalcliente.CPF == CPF and produto.codigo == codigo:
                            if produto.quantidade - int(quantidade) >= 0:
                                totalpagar = produto.valorVenda * int(quantidade)
                                achou = 1
                                fiscalcliente.quantidade = int(quantidade)
                                fiscalcliente.valorGasto += totalpagar
                                info = 1
                                messagebox.showinfo("Sucesso", "Adicionado ao carrinho")
                                self.listaVendas.insert(0, Vendas(CPF, codigo, quantidade, totalpagar))
                                break
                            else:
                                achou = 1
                                messagebox.showerror("Erro",
                                                     "Quantidade solicitada de produto maior do que tem no estoque")
                        if fiscalcliente.codigo == codigo:
                            info = 1
                    if produto.codigo == codigo:
                        achou = 1
            else:
                if info == 0:
                    for produto in self.listaProduto:
                        if produto.codigo == codigo and produto.quantidade - int(quantidade) >= 0:
                            totalpagar = produto.valorVenda * int(quantidade)
                            valores_gerados = []
                            while True:
                                valor = random.randint(100000, 999999)
                                if valor not in valores_gerados:
                                    valores_gerados.append(valor)
                                    notafiscal = NotaFiscalCliente(CPF, codigo, totalpagar, 0, 0, valor)
                                    self.idUnico = valor
                                    break
                            self.listaNotaFiscal.insert(0, notafiscal)
                            self.listaVendas.insert(0, Vendas(CPF, codigo, quantidade, totalpagar))
                            messagebox.showinfo("Sucesso", "Adicionado ao carrinho")
                            maior = 1
                            achou = 1
                            break
                    if maior == 0:
                        achou = 1
                        messagebox.showerror("Erro", "Quantidade solicitada de produto maior do que tem no estoque")
                if achou == 0:
                    messagebox.showerror("Erro", "Não existe nenhum produto com esse código")

            self.carrinho = mostrarCarrinho(self)
            codigo = self.produtosnotafiscal.inputCodigo.get()

            self.carrinho.textCarrinho.config(state=tk.NORMAL)
            self.carrinho.textCarrinho.delete(1.0, tk.END)
            for produto in self.listaProduto:
                if produto.codigo == codigo:
                    self.carrinho.textCarrinho.insert(tk.END,
                                                      f"Descrição: {produto.descricao}. "
                                                      f"Valor de venda: R${produto.valorVenda}.00.\n")
            self.carrinho.textCarrinho.config(state=tk.DISABLED)

            self.ProdutosDiferentesNotaFiscal += 1
        else:
            messagebox.showerror("Erro", "Taxa total de produtos por nota fiscal exercida")

    def pesquisarprodutonotafiscal(self, event):
        self.pesquisarprodutofiscal = ConsultarProdunoNotaFiscal(self)

    def consultarprodutonotafiscal(self, event):
        codigo = self.pesquisarprodutofiscal.inputCodigo.get()

        self.pesquisarprodutofiscal.textProdutos.config(state=tk.NORMAL)
        self.pesquisarprodutofiscal.textProdutos.delete(1.0, tk.END)
        for mercadorias in self.listaProduto:
            if mercadorias.codigo == codigo:
                self.pesquisarprodutofiscal.textProdutos.insert(tk.END, f"Código: {mercadorias.codigo}, "
                                                                        f"Descrição: {mercadorias.descricao}, "
                                                                        f"Valor de venda: R${mercadorias.valorVenda}.00\n")
        self.pesquisarprodutofiscal.textProdutos.config(state=tk.DISABLED)

    def limparprodutonotafiscal(self, event):
        self.pesquisarprodutofiscal.inputCodigo.delete(0, len(self.pesquisarprodutofiscal.inputCodigo.get()))

    def finalizarprodutonotafiscal(self, cevent):
        self.pesquisarprodutofiscal.destroy()

    def cancelarnotafiscal(self, event):
        while self.ProdutosDiferentesNotaFiscal > 0:
            self.ProdutosDiferentesNotaFiscal -= 1
            self.listaVendas.pop(self.ProdutosDiferentesNotaFiscal)
        for notafiscal in self.listaNotaFiscal:
            if notafiscal.valorUnico == self.idUnico:
                self.listaNotaFiscal.remove(notafiscal)
        messagebox.showinfo("Sucesso", "Produtos removidos do carrinho")

    def emitirnotafiscal(self, event):
        self.emissao = EmissaoNotaFiscal(self)
        CPF = self.notafiscal.inputCPF.get()
        codigo = self.produtosnotafiscal.inputCodigo.get()

        self.emissao.textNotaFiscal.config(state=tk.NORMAL)
        self.emissao.textNotaFiscal.delete(1.0, tk.END)

        for vendas in self.listaVendas:
            for produto in self.listaProduto:
                for cliente in self.listaNotaFiscal:
                    if cliente.CPF == CPF and (
                            vendas.codigo == codigo) and produto.codigo == vendas.codigo and produto.quantidade - int(
                            vendas.quantidade) >= 0:
                        produto.quantidade = -int(vendas.quantidade)
                        produto.vendas = int(vendas.quantidade)
                        break

        for produto in self.listaProduto:
            for cliente in self.listaNotaFiscal:
                if cliente.CPF == CPF and codigo == produto.codigo:
                    self.emissao.textNotaFiscal.insert(tk.END, f""
                                                               f"Valor total ------------ R${cliente.valorGasto},00\n")
                    self.listaLucroLiquido.append(LucroLiquido(0, cliente.valorGasto, cliente.dataEmissao))
                    self.ProdutosDiferentesNotaFiscal = 0
                    break
        self.emissao.textNotaFiscal.config(state=tk.DISABLED)

        self.produtosnotafiscal.destroy()

    def adicionardatanotafiscal(self, event):
        dia = self.emissao.inputDia.get()
        mes = self.emissao.inputMes.get()
        ano = self.emissao.inputAno.get()
        CPF = self.notafiscal.inputCPF.get()

        data = f"{ano}{mes}{dia}"

        for cliente in self.listaNotaFiscal:
            if cliente.dataEmissao == 0 and cliente.CPF == CPF:
                cliente.dataEmissao = int(data)
                break

        messagebox.showinfo("Sucesso", "Data adicionada a nota fiscal")
        self.emissao.destroy()

    def limpardatanotafiscal(self, event):
        self.emitirfiscal.inputData.delete(0, len(self.emitirfiscal.inputData.get()))

    def concluirnotafiscal(self, event):
        self.emissao = EmissaoNotaFiscal(self)
        CPF = self.notafiscal.inputCPF.get()
        codigo = self.produtosnotafiscal.inputCodigo.get()

        self.emissao.textNotaFiscal.config(state=tk.NORMAL)
        self.emissao.textNotaFiscal.delete(1.0, tk.END)

        for produto in self.listaProduto:
            for cliente in self.listaNotaFiscal:
                if cliente.CPF == CPF and codigo == produto.codigo:
                    self.emissao.textNotaFiscal.insert(tk.END, f""
                                                               f"Valor total ------------ R${cliente.valorGasto},00\n")
                    self.listaLucroLiquido.append(LucroLiquido(0, cliente.valorGasto, cliente.dataEmissao))
                    self.ProdutosDiferentesNotaFiscal = 0
                    break
        self.emissao.textNotaFiscal.config(state=tk.DISABLED)

        self.emitirfiscal.destroy()
        self.produtosnotafiscal.destroy()

    def limparCPFnotaFiscal(self, event):
        self.notafiscal.inputCPF.delete(0, len(self.notafiscal.inputCPF.get()))

    def finalizarCPFnotaFiscal(self, evnet):
        self.notafiscal.destroy()

    def maisVendidos(self):
        self.maisvendidos = MaisVendidos(self)

        listaAux = []
        for mercadorias in self.listaVendas:
            listaAux.append(mercadorias)

        listaAux.sort(key=lambda x: x.valorTotal, reverse=True)
        listaMaisVendidos = listaAux[:10]
        self.maisvendidos.textMaisVendidos.config(state=tk.NORMAL)
        self.maisvendidos.textMaisVendidos.delete(1.0, tk.END)
        if len(listaMaisVendidos) == 0:
            self.maisvendidos.textMaisVendidos.insert(tk.END, "Não houve nenhuma venda\n")
        for mercadorias in listaMaisVendidos:
            self.maisvendidos.textMaisVendidos.insert(tk.END,
                                                      f"Código: {mercadorias.codigo}, Descrição: {mercadorias.quantidade}, Valor de venda: R${mercadorias.valorTotal}.00\n")
        self.maisvendidos.textMaisVendidos.config(state=tk.DISABLED)

    def carregarDadosClientes(self):
        with open("clientes.txt", 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(', ')

                nome = dados[0]
                endereco = dados[1]
                email = dados[2]
                cpf = dados[3]

                cliente = Cliente(nome, endereco, email, cpf)
                self.listaCliente.append(cliente)

    def carregarDadosProdutos(self):
        with open("produtos.txt", 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(', ')

                codigo = dados[0]
                descricao = dados[1]
                precoCompra = dados[2]
                valorVenda = dados[3]
                quantidade = dados[4]
                vendas = dados[5]

                produto = Produto(codigo, descricao, int(precoCompra), int(valorVenda), int(quantidade), int(vendas))
                self.listaProduto.append(produto)

    def carregarDadosVendas(self):
        with open("vendas.txt", 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(', ')

                CPF = dados[0]
                codigo = dados[1]
                quantidade = dados[2]
                valorTotal = dados[3]

                vendas = Vendas(CPF, codigo, int(quantidade), int(valorTotal))
                self.listaVendas.append(vendas)