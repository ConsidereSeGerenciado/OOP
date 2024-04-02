# Nome: Gabriel Maia Alves Araújo - 2022005689 #

from abc import ABC, abstractmethod

class Banco(ABC):
    def __init__(self, nome, numConta, saldo):
        self.__nome = nome
        self.__numConta = numConta
        self.__saldo = saldo

    @property
    def numConta(self):
        return self.__numConta

    @numConta.setter
    def numConta(self, numConta):
        self.__numConta = numConta

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @abstractmethod
    def deposito(self, data, valor, descricao):
        pass

    @abstractmethod
    def retirada(self, data, valor, descricao):
        pass

    @abstractmethod
    def imprimirExtrato(self):
        pass


class ContaCorrenteComum(Banco):
    def __init__(self, nome, numConta, saldo):
        super().__init__(nome, numConta, saldo)
        self.__listaTransacao = []

    def deposito(self, data, valor, descricao):
        self.saldo += valor
        return self.__listaTransacao.append(Transacoes(data, valor, descricao))

    def retirada(self, data, valor, descricao):
        if self.saldo - valor < 0:
            print("Saldo insuficiente para a retirada na conta corretne comum")
        else:
            self.saldo -= valor
            return self.__listaTransacao.append(Transacoes(data, valor, descricao))


    def imprimirExtrato(self):
        imprimir = f"Nome: {self.nome} \nNúmero da conta: {self.numConta} \nSaldo: {self.saldo}\n"
        for transicao in self.__listaTransacao:
            imprimir += f"Data: {transicao.data}, Valor: {transicao.valor}, Descrição: {transicao.descricao}\n"
        return imprimir

class ContaCorrenteLimite(Banco):
    def __init__(self, nome, numConta, saldo, valorLimite):
        super().__init__(nome, numConta, saldo)
        self.__valorLimite = valorLimite
        self.__listaTransacao = []

    def deposito(self, data, valor, descricao):
        self.saldo += valor
        return self.__listaTransacao.append(Transacoes(data, valor, descricao))

    def retirada(self, data, valor, descricao):
        if self.saldo - valor < self.__valorLimite:
            print("Limite insuficiente para realizada a retirada")
        else:
            self.saldo -= valor
            return self.__listaTransacao.append(Transacoes(data, valor, descricao))

    def imprimirExtrato(self):
        imprimir = f"Nome: {self.nome}\nNúmero da conta: {self.numConta}\nSaldo: {self.saldo}\nLimite: {self.__valorLimite}\n"
        for transicao in self.__listaTransacao:
            imprimir += f"Data: {transicao.data}, Valor: {transicao.valor}, Descrição: {transicao.descricao} \n"
        return imprimir

class ContaPoupanca(Banco):
    def __init__(self, nome, numConta, saldo, aniversarioConta):
        super().__init__(nome, numConta, saldo)
        self.__aniversarioConta = aniversarioConta
        self.__listaTransacao = []

    def deposito(self, data, valor, descricao):
        self.saldo += valor
        return self.__listaTransacao.append(Transacoes(data, valor, descricao))

    def retirada(self, data, valor, descricao):
        if self.saldo - valor < 0:
            print("Saldo insuficiente para a retirada na conta poupança")
        else:
            self.saldo -= valor
            return self.__listaTransacao.append(Transacoes(data, valor, descricao))

    def imprimirExtrato(self):
        imprimir = f"Nome: {self.nome}\nNúmero da conta: {self.numConta}\nSaldo: {self.saldo}\nAniversário da conta: {self.__aniversarioConta}\n"
        for transicao in self.__listaTransacao:
            imprimir += f"Data: {transicao.data}, Valor: {transicao.valor}, Descrição: {transicao.descricao} \n"
        return imprimir


class Transacoes:
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

if __name__ == "__main__":

    comum = ContaCorrenteComum("João", 3245, 1000)
    comum.deposito("10/05/2023", 500, "ganhando com jogos")
    comum.retirada("03/12/2023", 1273, "compras no shopping")

    limite = ContaCorrenteLimite("Maria", 7738, 2500, 800)
    limite.deposito("20/12/2033", 2300, "décimo terceiro")
    limite.retirada("24/12/2033", 800, "presentes")

    poupanca = ContaPoupanca("Zeca", 5930, 1800, "12/30")
    poupanca.deposito("02/04/2028", 1500, "pagamento")
    poupanca.retirada("09/04/2028", 500, "páscoa")

    listaContas = [comum, limite, poupanca]

    for conta in listaContas:
        print(conta.imprimirExtrato())