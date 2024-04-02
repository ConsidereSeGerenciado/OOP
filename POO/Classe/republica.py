from abc import ABC, abstractmethod


class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @abstractmethod
    def salario(self):
        pass


class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

    def salario(self):
        return self.__valorPorHora * self.__horasTrabalhadas

class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    def salario(self):
        return self.__valorPorDia * self.__diasTrabalhados


class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    def salario(self):
        return self.__valorMensal


if __name__ == "__main__":
    horista = Horista("Creusa", "(38)97221-6892", 160, 12)
    diarista = Diarista("Pedro", "(38)99978-5998", 20, 65)
    mensalista = Mensalista("Jose", "(38)93569-9874", 1200)

    print(f"Salário da horista {horista.nome} é {horista.salario()}")
    print(f"Salário do diarista {diarista.nome} é {diarista.salario()}")
    print(f"Salário do mensalista {mensalista.nome} é {mensalista.salario()}")

    if(horista.salario()>diarista.salario()):
        if(diarista.salario()>mensalista.salario()):
            print(f"\nA opção mais barata é o mensalista {mensalista.nome}, {mensalista.telefone}, e com o salário de {mensalista.salario()}")
        else:
            print(f"\nA opção mais barata é o diarista {diarista.nome}, {diarista.telefone}, e com o salário de {diarista.salario()}")
    else:
        print(f"\nA opção mais barata é a horisto {horista.nome}, {horista.telefone}, e com o salário de {horista.salario()}")


