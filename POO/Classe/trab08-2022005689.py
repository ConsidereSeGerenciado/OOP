# Nome: Gabriel Maia Alves Araújo - 2022005689 #

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

class TipoErrado(Exception):
    pass

class IdadeBaixa(Exception):
    pass

class CPFJaExistente(Exception):
    pass

if __name__ == "__main__":
    listaDePessoas = [
        ("Jane", "6776", "Moc", 53, "Doutor"), # codinção correta
        ("Wellington", "3289", "Itajuba", 30, "Doutor"), # codinção correta
        ("Karla", "6842", "Itajuba", 49, "Mestrado"), # titulação errada
        ("Tiago", "1795", "Moc", 27, "Doutor"), # idade errada
        ("Heloi", "8493", "Moc", 23, "Graduado"), # titulação e idade erradas
        ("Warley", "3289", "Itajuba", 47, "Doutor"), # CPF igual
        ("Pedro", "0000", "Itajuba", 18, "CCO"), # codinção correta
        ("Lucca", "1274", "Moc", 22, "SIN"), # codinção correta
        ("Luiza", "7219", "Moc", 16, "CCO"), # idade errada
        ("Laura", "0916", "Itajuba", 19, "BCO"), # curso correto
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
            print(f"O CPF {cpf} de {nome} já existe.")
            print()

    for alguem in cadastro:
        alguem.printDescricao()
        print()