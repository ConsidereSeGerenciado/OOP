from abc import ABC, abstractmethod


class Banco(ABC):
    def __init__(self, nroConta, nomeCorrentista, saldo):
        self.__nroConta = nroConta
        self.__nomeCorrentista = nomeCorrentista
        self.__saldo = saldo

    @property
    def nroConta(self):
        return  self.__nroConta

    @property
    def nomeCorrentista(self):
        return self.__nomeCorrentista

    @property
    def saldo(self):
        return self.__saldo


    def deposito(self):
        pass

    @abstractmethod
    def retirada(self):
        pass

    @abstractmethod
    def imprimeExtrato(self):
        pass

class ContaCorrenteComum(Banco):
    def __init__(self, nroConta, nomeCorrentista, saldo):
        super().__init__(nroConta, nomeCorrentista, saldo)
        self.__transacaoComum = []

    @property
    def transacaoComum(self):
        return self.__transacaoComum


class ContaCorrenteLimite(Banco):
    def __init__(self, nroConta, nomeCorrentista, saldo, aniversarioConta):
        super().__init__(nroConta, nomeCorrentista, saldo)
        self.__aniversarioConta = aniversarioConta
        self.__transacaoLimite = []

    @property
    def aniversarioConta(self):
        return self.__aniversarioConta

    @property
    def transacaoLimite(self):
        return self.__transacaoLimite

class ContaPoupanca(Banco):
    def __init__(self, nroConta, nomeCorrentista, saldo, limite):
        super().__init__(nroConta, nomeCorrentista, saldo)
        self.__limite = limite
        self.__transacaoPoupanca = []

    @property
    def limite(self):
        return self.__limite

    @property
    def transacaoPoupanca(self):
        return self.__transacaoPoupanca

class Trasacao():
    def __init__(self, data, valor, descricao):
        self.__data = data
        self.__valor = valor
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data

    @property
    def valor(self):
        return self.__valor

    @property
    def descricao(self):
        return self.__descricao