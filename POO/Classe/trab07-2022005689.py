# Nome: Gabriel Maia Alves Araújo - 2022005689 #

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = []

    @property
    def getCodigo(self):
        return self.__codigo

    @property
    def getNome(self):
        return self.__nome

    @property
    def getPontoMensalFunc(self):
        return self.__pontoMensalFunc

    def adicionaPonto(self, mes, ano, faltas, atrasos):
        ponto = PontoFunc(mes, ano, faltas, atrasos)
        self.__pontoMensalFunc.append(ponto)

    def lancaFaltas(self, mes, ano, faltas):
        for ponto in self.__pontoMensalFunc:
            if ponto.getMes == mes and ponto.getAno == ano:
                ponto.lancaFaltas(faltas)

    def lancaAtrasos(self, mes, ano, atrasos):
        for ponto in self.__pontoMensalFunc:
            if ponto.getMes == mes and ponto.getAno == ano:
                ponto.lancaAtrasos(atrasos)

    def imprimeFolha(self, mes, ano):
        print(f"Codigo: {self.getCodigo}")
        print(f"Nome: {self.getNome}")
        print(f"Salário líquido: {self.calculaSalario(mes, ano):.2f}")
        print(f"Bonus: {self.calculaBonus(mes, ano):.2f}")

    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass



class PontoFunc:
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    @property
    def getMes(self):
        return self.__mes

    @property
    def getAno(self):
        return self.__ano

    @property
    def getNroFaltas(self):
        return self.__nroFaltas

    @property
    def getNroAtrasos(self):
        return self.__nroAtrasos

    def lancaFaltas(self, nroFaltas):
        self.__nroFaltas += nroFaltas

    def lancaAtrasos(self, nroAtrasos):
        self.__nroAtrasos += nroAtrasos

class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroHoras):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroHoras = nroHoras

    def getTitulacao(self):
        return self.__titulacao

    def getSalarioHora(self):
        return self.__salarioHora

    def getNroAulas(self):
        return self.__nroHoras

    def calculaSalario(self, mes, ano):
        salario = 0
        for ponto in self.getPontoMensalFunc:
            if ponto.getMes == mes and ponto.getAno == ano:
                salario = self.__salarioHora * self.__nroHoras - self.__salarioHora * ponto.getNroFaltas
        return salario

    def calculaBonus(self, mes, ano):
        bonus = 0
        for ponto in self.getPontoMensalFunc:
            if ponto.getMes == mes and ponto.getAno == ano:
                if ponto.getNroAtrasos < 10:
                    percBonus = 10 - ponto.getNroAtrasos
                    bonus = self.calculaSalario(mes, ano) * (percBonus/100)
        return bonus

class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    def getFuncao(self):
        return self.__funcao

    def getSalarioMensal(self):
        return self.__salarioMensal

    def calculaSalario(self, mes, ano):
        salario = 0
        for ponto in self.getPontoMensalFunc:
            if ponto.getMes == mes and ponto.getAno == ano:
                salario = self.__salarioMensal - (self.__salarioMensal/30) * ponto.getNroFaltas
        return salario

    def calculaBonus(self, mes, ano):
        bonus = 0
        for ponto in self.getPontoMensalFunc:
            if ponto.getMes == mes and ponto.getAno == ano:
                if ponto.getNroAtrasos < 8:
                    percBonus = 8 - ponto.getNroAtrasos
                    bonus = self.calculaSalario(mes, ano) * (percBonus/100)
        return bonus

if __name__ == "__main__":
     funcionarios = []
     prof = Professor(1, "Joao", "Doutor", 45.35, 32)
     prof.adicionaPonto(4, 2021, 0, 0)
     prof.lancaFaltas(4, 2021, 2)
     prof.lancaAtrasos(4, 2021, 3)
     funcionarios.append(prof)
     tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
     tec.adicionaPonto(4, 2021, 0, 0)
     tec.lancaFaltas(4, 2021, 3)
     tec.lancaAtrasos(4, 2021, 4)
     funcionarios.append(tec)

     for func in funcionarios:
         func.imprimeFolha(4, 2021)
         print()



class Pessoa:
    def __init__(self, nome, CPF, endereco, idade):
        self.__nome = nome
        self.__CPF = CPF
        self.__endereco = endereco
        self.__idade = idade

    @property
    def getNome(self):
        return self.__nome

    @property
    def getCPF(self):
        return self.__CPF

    @property
    def getEndereco(self):
        return self.__endereco

    @property
    def getIdade(self):
        return self.__idade

    def printDescricao(self):
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__CPF}")
        print(f"Endereço: {self.__endereco}")
        print(f"Idade: {self.__idade}")

class Professor(Pessoa):
    def __init__(self, nome, CPF, endereco, idade, titulacao):
        super().__init__(nome, CPF, endereco, idade)
        self.__titulacao = titulacao

    @property
    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        super().printDescricao()
        print(f"Titulação: {self.__titulacao}")

class Aluno(Pessoa):
    def __init__(self, nome, CPF, endereco, idade, curso):
        super().__init__(nome, CPF, endereco, idade)
        self.__curso = curso

    @property
    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        super().printDescricao()
        print(f"Curso: {self.__curso}")

# class TitulacaoErrada(Exception):
#     pass

class TipoErrado(Exception):
    pass

class IdadeBaixa(Exception):
    pass

# class CursoDiferente(Exception):
#     pass

class CPFJaExistente(Exception):
    pass

if __name__ == "__main__":
    listaDePessoas = [
        ("Jane", "6776", "Moc", 53, "Doutor"), # codinção correta
        ("Wellington", "3289", "Moc", 50, "Doutor"), # codinção correta
        ("Karla", "6842", "Moc", 49, "Mestrado"), # titulação errada
        ("Tiago", "1795", "Moc", 27, "Doutor"), # idade errada
        ("Heloi", "8493", "Moc", 23, "Graduado"), # titulação e idade erradas
        ("Warley", "3289", "Moc", 47, "Doutor"), # CPF igual
        ("Pedro", "0000", "Moc", 19, "CCO"), # codinção correta
        ("Lucca", "1274", "Moc", 22, "SIN"), # codinção correta
        ("Luiza", "7219", "Moc", 16, "CCO"), # idade errada
        ("Laura", "0916", "Moc", 19, "BCO"), # curso correto
        ("Renato", "2856", "Moc", 17, "EMC"), # curso e idade errada
        ("Jão", "0000", "Moc", 23, "CCO") # CPF igual
    ]

    cadastro = []
    for nome, cpf, endereco, idade, tipo in listaDePessoas:
        try:
            if tipo != "Doutor" and tipo != "CCO" and tipo != "SIN":
                raise TipoErrado
            if tipo == "Doutor" and idade < 30:
                raise IdadeBaixa
            if tipo == "CCO" and idade < 18:
                raise IdadeBaixa
            for CPF in cadastro:
                if cpf == CPF.getCPF:
                    raise CPFJaExistente

            if tipo == "Doutor" and idade >= 30:
                cadastro.append(Professor(nome, cpf, endereco, idade, tipo))
            if tipo == "CCO" or tipo == "SIN" and idade >= 18:
                cadastro.append(Aluno(nome, cpf, endereco, idade, tipo))

        except TipoErrado:
            print(f"O tipo de {nome}, {tipo}, não condiz com a que é requerido.")
            print()
        except IdadeBaixa:
            print(f"A idade de {nome} é baixa.")
            print()
        except CPFJaExistente:
            print(f"Já existe um cadastro com o CPF {cpf}.")
            print()

    for alguem in cadastro:
        alguem.printDescricao()
        print()

# if __name__ == "__main__":
#     professores = [
#         ("Jane", "6776", "Moc", 53, "Doutor"),
#         ("Wellington", "3289", "Moc", 50, "Doutor"),
#         ("Karla", "6842", "Moc", 49, "Mestrado"),
#         ("Tiago", "1795", "Moc", 27, "Doutor"),
#         ("Heloi", "8493", "Moc", 23, "Graduado"),
#         ("Warley", "3289", "Moc", 47, "Doutor")
#     ]
#     alunos = [
#         ("Pedro", "0000", "Moc", 19, "CCO"),
#         ("Lucca", "1274", "Moc", 22, "SIN"),
#         ("Luiza", "7219", "Moc", 16, "CCO"),
#         ("Laura", "0916", "Moc", 19, "BCO"),
#         ("Renato", "2856", "Moc", 17, "EMC"),
#         ("Jão", "0000", "Moc", 23, "CCO")
#     ]
#
#     cadastro = []
#     for nome, cpf, endereco, idade, titulacao in professores:
#         try:
#
#             if titulacao != "Doutor":
#                 raise TitulacaoErrada
#             if idade < 30:
#                 raise IdadeBaixa
#             for CPF in cadastro:
#                 if cpf == CPF.getCPF:
#                     raise CPFJaExistente
#
#             if titulacao == "Doutor" and idade >= 30:
#                 cadastro.append(Professor(nome, cpf, endereco, idade, titulacao))
#
#         except TitulacaoErrada:
#             print(f"A titulação do(a) professor(a) {nome}, {titulacao}, não condiz com a que é requerido, Doutor.")
#             print()
#         except IdadeBaixa:
#             print(f"A idade do(a) prfessor(a) {nome} é baixa.")
#             print()
#         except CPFJaExistente:
#             print(f"Já existe um cadastro com o CPF {cpf}.")
#             print()
#
#     for nome, cpf, endereco, idade, curso in alunos:
#         try:
#
#             if curso != "CCO" and curso != "SIN":
#                 raise CursoDiferente
#             if idade < 18:
#                 raise IdadeBaixa
#             for CPF in cadastro:
#                 if cpf == CPF.getCPF:
#                     raise CPFJaExistente
#
#             if curso == "CCO" or curso == "SIN" and idade >= 18:
#                 cadastro.append(Aluno(nome, cpf, endereco, idade, curso))
#
#         except CursoDiferente:
#             print(f"O curso do(a) aluno(a) {nome}, {curso}, é diferente da que é pedida, CCO ou SIN.")
#             print()
#         except IdadeBaixa:
#             print(f"A idade do(a) aluno(a) {nome} é baixa.")
#             print()
#         except CPFJaExistente:
#             print(f"Já existe um cadastro com o CPF {cpf}.")
#             print()
#
#     for alguem in cadastro:
#         alguem.printDescricao()
#         print()