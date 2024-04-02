from abc import ABC, abstractmethod


class Trabalhador(ABC):
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome
        self.__listaDependentes = []

    @property
    def getCPF(self):
        return self.__cpf

    @property
    def getNome(self):
        return self.__nome

    @property
    def listaDependentes(self):
        return self.__listaDependentes

    def insereDependente(self, nome, idade):
        return self.__listaDependentes.append(Depende(nome, idade))

    @abstractmethod
    def calculaPagto(self, mes):
        pass

    @abstractmethod
    def imprimeRecibo(self, mes):
        pass

class Depende:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

class Diarista(Trabalhador):
    def __init__(self, cpf, nome, valorDiaria):
        super().__init__(cpf, nome)
        self.__valorDiaria = valorDiaria
        self.__listaDiarista = []

    def listaDiarista(self):
        return self.__listaDiarista

    def adicionaDiaria(self, dia, mes, ano, almoco, atraso):
        return self.__listaDiarista.append(Diaria(dia, mes, ano, almoco, atraso))

    def obtemValorAuxilio(self):
        pass

    def calculaPagto(self, mes):
        pagar = 0
        total = 0
        for diarista in self.__listaDiarista:
            if total > 0:
                if diarista.atraso > 0:
                    if diarista.atraso >= 30:
                        return pagar * total
                    pagar = self.__valorDiaria - (self.__valorDiaria*0.01)
                    if diarista.almoco:
                        pagar -= 10
                    return pagar * total
                    # else:
                    #     return pagar * total
                else:
                    pagar = self.__valorDiaria
                if diarista.almoco:
                    pagar -= 10
                return pagar * total
                # else:
                #     return pagar * total
            else:
                return pagar



    def imprimeRecibo(self, mes):
        pass

class Diaria:
    def __init__(self, dia, mes, ano, almoco, atraso):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__almoco = almoco
        self.__atraso = atraso

    @property
    def getDia(self):
        return self.__dia

    @property
    def getMes(self):
        return self.__mes

    @property
    def getAno(self):
        return self.__ano

    @property
    def getAlmoco(self):
        return self.__almoco

    @property
    def getAtraso(self):
        return self.__atraso

class Empreiteiro(Trabalhador):
    def __init__(self, cpf, nome):
        super().__init__(cpf, nome)
        self.__listaEmpreito = []

    def adicionaEmpreito(self, mes, ano, descricao, valor, atrasoEntrega):
        return self.__listaEmpreito.append(Empreito(mes, ano, descricao, valor, atrasoEntrega))

    def calculaPagto(self, mes):
        pass

    def imprimeRecibo(self, mes):
        pass

class Empreito:
    def __init__(self, mes, ano, descricao, valor, atrasoEntrega):
        self.__mes = mes
        self.__ano = ano
        self.__descricao = descricao
        self.__valor = valor
        self.__atrasoEntrega = atrasoEntrega

    @property
    def getMes(self):
        return self.__mes

    @property
    def getAno(self):
        return self.__ano

    @property
    def getDescricao(self):
        return self.__descricao

    @property
    def getValor(self):
        return self.__valor

    @property
    def isAtrasoEntrega(self):
        return self.__atrasoEntrega

if __name__ == "__main__":
    listaTrab = []
    d1 = Diarista("111222", "Joao Silva", 100)
    d1.insereDependente("Pedro Silva", 4)
    d1.insereDependente("Ana Silva", 2)
    d1.adicionaDiaria(10, 3, 2022, False, False)
    d1.adicionaDiaria(12, 4, 2022, False, True)
    d2 = Diarista("222333", "Jose Cruz", 120)
    d2.insereDependente("Paula Cruz", 3)
    d2.insereDependente("Mario Cruz", 10)
    d2.adicionaDiaria(5, 4, 2022, False, False)
    d2.adicionaDiaria(6, 4, 2022, True, False)
    d2.adicionaDiaria(7, 4, 2022, True, True)
    e1 = Empreiteiro("333444", "Marcio Souza")
    e1.adicionaEmpreito(3, 2022, "Fundações", 6000, False)
    e1.adicionaEmpreito(4, 2022, "Construção muros", 4000, False)
    e1.adicionaEmpreito(4, 2022, "Instalação dos pisos", 7000, True)
    listaTrab.append(d1)
    listaTrab.append(d2)
    listaTrab.append(e1)
    for trab in listaTrab:
        trab.imprimeRecibo(4, 2022)
