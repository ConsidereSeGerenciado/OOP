import tkinter as tk
import Loja as lj


class View:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('650x300')
        self.menubar = tk.Menu(self.root)
        self.Produto = tk.Menu(self.menubar)
        self.Consultar = tk.Menu(self.menubar)
        self.MaisVendidos = tk.Menu(self.menubar)
        self.Emitir = tk.Menu(self.menubar)

        self.menubar.add_cascade(label="Cadastrar", menu=self.Produto)
        self.Produto.add_command(label="Cliente", command=self.controle.adicionarCliente)
        self.Produto.add_command(label="Produto", command=self.controle.adicionarmercadoria)

        self.menubar.add_cascade(label="Consultar", menu=self.Consultar)
        self.Consultar.add_command(label="Produtos", command=self.controle.consultarmercadoria)
        self.Consultar.add_command(label="Clintes", command=self.controle.consultarcliente)
        self.Consultar.add_command(label="Faturamento por Produto", command=self.controle.consultarFaturamentoProduto)
        self.Consultar.add_command(label="Faturamento por Cliente", command=self.controle.consultarFaturamentoCliente)
        self.Consultar.add_command(label="Faturamento por Período", command=self.controle.consultarFaturamentoPeriodo)
        self.Consultar.add_command(label="Lucro líquido por Período", command=self.controle.consultarLucroLiquido)
        self.Consultar.add_command(label="Vendas realizadas em um Período", command=self.controle.consultarVendasRealizadas)

        self.menubar.add_cascade(label="Emitir Nota Fiscal", menu=self.Emitir)
        self.Emitir.add_command(label="Emitir", command=self.controle.emitirNotaFiscal)

        self.menubar.add_cascade(label="Mais Vendidos", menu=self.MaisVendidos)
        self.MaisVendidos.add_command(label="Consultar", command=self.controle.consultarMaisVendidos)

        self.root.config(menu=self.menubar)


class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.Controle = lj.Controle(self)

        self.limite = View(self.root, self)

        self.Controle.carregarDadosClientes()

        self.Controle.carregarDadosProdutos()

        self.Controle.carregarDadosVendas()

        self.root.protocol("WM_DELETE_WINDOW", self.fecharPrograma)

        self.root.title("Gerenciamento da Loja")
        self.root.mainloop()

    def adicionarCliente(self):
        self.Controle.cadastrarCliente(0)

    def adicionarmercadoria(self):
        self.Controle.adicionarProduto()

    def consultarmercadoria(self):
        self.Controle.consultarProduto()

    def consultarcliente(self):
        self.Controle.consultarCliente()

    def consultarFaturamentoProduto(self):
        self.Controle.faturamentoProduto()

    def consultarFaturamentoCliente(self):
        self.Controle.faturamentoCliente()

    def consultarFaturamentoPeriodo(self):
        self.Controle.faturamentoPeriodo()

    def consultarLucroLiquido(self):
        self.Controle.lucroLiquido()

    def consultarVendasRealizadas(self):
        self.Controle.clientePeriodo()

    def emitirNotaFiscal(self):
        self.Controle.noteFiscal()

    def consultarMaisVendidos(self):
        self.Controle.maisVendidos()

    def fecharPrograma(self):
        self.root.destroy()


if __name__ == '__main__':
    c = ControlePrincipal()
