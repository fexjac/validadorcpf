class Cpf():

    def __init__(self, registro):
        self.__registro = registro
        self.__numero = None
        self.__calculado = False
        self.__dv_cpf_validado = False
        self.__cpf_invalido = False

    def numero(self):
        return self.__numero

    def set_numero(self, numero):
        cpf_invalidos = ['00000000000', '11111111111', '22222222222',
        '33333333333', '44444444444', '55555555555', '66666666666',
        '77777777777', '88888888888', '99999999999']

        if len(str(numero)) == 11:
            if numero in cpf_invalidos:
                self.__numero = 0
            else:
                self.__numero = numero
        else:
            self.__numero = 0

    def verifica_igualdade_digitos(self, numero):
        numero = str(numero)
        cpf_invalidos = ['00000000000', '11111111111', '22222222222',
        '33333333333', '44444444444', '55555555555', '66666666666',
        '77777777777', '88888888888', '99999999999']
        if numero in cpf_invalidos:
            self.__cpf_invalido = False
        else:
            self.__cpf_invalido = True

        return self.__cpf_invalido

    def calcula_digitos_validade_cpf(self):
        dv1 = False
        dv2 = False

        totalizador = 0
        digito = 0

        for i in range(10, 1, -1):
          totalizador += (int(self.__numero[digito]))*i
          digito += 1

        digito10 = int(self.__numero[9])
        validar = (totalizador*10)%11

        if validar == digito10:
            dv1 = True

        totalizador = 0
        digito = 0

        for i in range(11, 1, -1):
          totalizador += (int(self.__numero[digito]))*i
          digito += 1

        digito11 = int(self.__numero[10])
        validar = (totalizador*10)%11

        if validar == digito11:
            dv2 = True

        if dv1 == True and dv2 ==True:
            self.__dv_cpf_validado = True

        self.__calculado = True

    def calculado(self):
        return self.__calculado

    def validado(self):
        return self.__dv_cpf_validado
