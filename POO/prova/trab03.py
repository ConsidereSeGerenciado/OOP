from abc import ABC, abstractmethod

class EmpDomestica (ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas

    @property
    def valorPorHora(self):
        return self.__valorPorHora

    def getSalario(self):
        return self.horasTrabalhadas * self.valorPorHora


class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados

    @property
    def valorPorDia(self):
        return self.__valorPorDia

    def getSalario(self):
        return self.valorPorDia * self.diasTrabalhados


class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    @property
    def valorMensal(self):
        return self.__valorMensal

    def getSalario(self):
        return self.valorMensal

if __name__ == "__main__":
    listaDeEmpregadas = []

    horista = Horista("Fernanda", 3599999999, 160, 12)
    diarista = Diarista("Lena", 35988888888, 20, 65)
    mensalista = Mensalista("Nazare", 35977777777, 1200)

    listaDeEmpregadas.append(horista)
    listaDeEmpregadas.append(diarista)
    listaDeEmpregadas.append(mensalista)

    # listaDeEmpregadas = {["Fernanda", 3599999999, 160, 12], ["Lena", 35988888888, 20, 65], ["Nazare", 35977777777, 1200]}

    for empregadas in listaDeEmpregadas:
        print(f"Nome: {empregadas.nome}")
        print(f"Valor mensal: {empregadas.getSalario()}")
        print()

    if horista.getSalario() < diarista.getSalario() and horista.getSalario() < mensalista.getSalario():
        print(f"Nome: {horista.nome}")
        print(f"Telefone: {horista.telefone}")
        print(f"Salario: {horista.getSalario()}")
        print()

    if diarista.getSalario() < horista.getSalario() and diarista.getSalario() < mensalista.getSalario():
        print(f"Nome: {diarista.nome}")
        print(f"Telefone: {diarista.telefone}")
        print(f"Salario: {diarista.getSalario()}")
        print()

    if mensalista.getSalario() < diarista.getSalario() and mensalista.getSalario() < horista.getSalario():
        print(f"Nome: {mensalista.nome}")
        print(f"Telefone: {mensalista.telefone}")
        print(f"Salario: {mensalista.getSalario()}")
        print()
