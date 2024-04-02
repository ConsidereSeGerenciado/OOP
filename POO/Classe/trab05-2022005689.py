# Nome: Gabriel Maia Alves Araújo - 2022005689 #

from abc import ABC, abstractmethod

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []

    @property
    def getCodigo(self):
        return self.__codigo

    @property
    def getNome(self):
        return self.__nome

    @abstractmethod
    def adicionaVenda(self, codImovel, mes, ano, valor):
        pass

    @abstractmethod
    def getDados(self):
        pass

    @abstractmethod
    def calculaRenda(self, mes, ano):
        pass

class Venda:
    def __init__(self, codImovel, mesVenda, anoVenda, valorRenda):
        self.__codImovel = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valorRenda = valorRenda
        self.__vendas = []

    @property
    def getCodImovel(self):
        return self.__codImovel

    @property
    def getMesVenda(self):
        return self.__mesVenda

    @property
    def getAnoVenda(self):
        return self.__anoVenda

    @property
    def getValorRenda(self):
        return self.__valorRenda

class Contratado(Vendedor):
    def __init__(self, codigo, nome, salario, nroCartTrabalho):
        super().__init__(codigo, nome)
        self.__nroCartTrabalho = nroCartTrabalho
        self.__salario = salario
        self.__vendas = []

    def getNroCartTrabalho(self):
        return self.__nroCartTrabalho

    def getSalarioFixo(self):
        return self.__salario

    def adicionaVenda(self, codImovel, mes, ano, valor):
        return self.__vendas.append(Venda(codImovel, mes, ano, valor))

    def getDados(self):
        return f"Nome: {self.getNome} - Nro Carteira: {self.getNroCartTrabalho()}"

    def calculaRenda(self, mes, ano):
        valorComissao = 0
        for venda in self.__vendas:
            if mes == venda.getMesVenda and ano == venda.getAnoVenda:
                valorComissao += venda.getValorRenda * 0.01
        return self.__salario + valorComissao


class Comissionado(Vendedor):
    def __init__(self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self.__nroCPF = nroCPF
        self.__comissao = comissao
        self.__vendas = []

    def getNroCPF(self):
        return self.__nroCPF

    def getComissao(self):
        return self.__comissao

    def adicionaVenda(self, codImovel, mes, ano, valor):
        return self.__vendas.append(Venda(codImovel, mes, ano, valor))

    def getDados(self):
        return f"Nome: {self.getNome} - Nro CPF: {self.getNroCPF()}"

    def calculaRenda(self, mes, ano):
        valorComissao = 0
        for venda in self.__vendas:
            if mes == venda.getMesVenda and ano == venda.getAnoVenda:
                valorComissao += venda.getValorRenda * (self.__comissao/100)
        return valorComissao

if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)

    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)

    listaFunc = [funcContratado, funcComissionado]

    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))
