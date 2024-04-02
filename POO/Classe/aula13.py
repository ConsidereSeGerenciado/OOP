from datetime import date

class Conta:
    def __init__(self, nroConta, nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []

    @property
    def NroConta(self):
        return self.__nroConta

    @property
    def Nome(self):
        return self.__nome

    @property
    def Limite(self):
        return self.__limite

    @property
    def Senha(self):
        return self.__senha

    @property
    def Transacoes(self):
        return self.__transacoes

    def adicionaDeposito(self, valor, data, nomeDepositante):
        deposito = Deposito(valor, data, nomeDepositante)
        return self.__transacoes.append(deposito)

    def adicionaSaque(self, valor, data, senha):
        if senha != self.__senha or valor > self.calculaSaldo():
            return False
        self.__transacoes.append(Saque(valor, data, senha))
        return True

    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if senha != self.__senha or valor > self.calculaSaldo():
            return False
        tDebito = Transferencia(valor, data, senha, "D")
        self.__transacoes.append(tDebito)
        tCredito = Transferencia(valor, data, senha, "C")
        contaFavorecido.Transacoes.append(tCredito)
        return True

    def calculaSaldo(self):
        saldo = self.__limite
        for transacao in self.__transacoes:
            if type(transacao) is Saque:
                saldo -= transacao.getValor
            if type(transacao) is Deposito:
                saldo += transacao.getValor
            if type(transacao) is Transferencia and transacao.getTipoTransf == "D":
                saldo -= transacao.getValor
            if type(transacao) is Transferencia and transacao.getTipoTransf == "C":
                saldo += transacao.getValor
        return saldo

class Transacao:
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    @property
    def getValor(self):
        return self.__valor

    @property
    def getData(self):
        return self.__data

class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha

    @property
    def getSenha(self):
        return self.__senha

class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf

    @property
    def getSenha(self):
        return self.__senha

    @property
    def getTipoTransf(self):
        return self.__tipoTransf

class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante

    @property
    def getNomeDepositante(self):
        return self.__nomeDepositante

if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')

    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700