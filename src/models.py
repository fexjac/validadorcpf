class Cpf():

    def __init__(self, registro):
        self.__registro = registro
        self.__numero = None
        self.__calculado = False
        self.__cpf_validado = False


    def numero(self):
        return self.__numero

    def set_numero(self, numero):
        if len(str(numero)) == 11:
            self.__numero = numero
        else:
            self.__numero = 0

    def calcula_digitos_validade_cpf(self):
        dv1 = False
        dv2 = False

        digito1 = int(self.__numero[0])*10
        digito2 = int(self.__numero[1])*9
        digito3 = int(self.__numero[2])*8
        digito4 = int(self.__numero[3])*7
        digito5 = int(self.__numero[4])*6
        digito6 = int(self.__numero[5])*5
        digito7 = int(self.__numero[6])*4
        digito8 = int(self.__numero[7])*3
        digito9 = int(self.__numero[8])*2
        digito10 = int(self.__numero[9])
        totalizador = digito1+digito2+digito3+digito4+digito5+digito6+digito7+digito8+digito9
        validar = (totalizador*10)%11
        if validar == digito10:
            dv1 = True
        digito1 = int(self.__numero[0])*11
        digito2 = int(self.__numero[1])*10
        digito3 = int(self.__numero[2])*9
        digito4 = int(self.__numero[3])*8
        digito5 = int(self.__numero[4])*7
        digito6 = int(self.__numero[5])*6
        digito7 = int(self.__numero[6])*5
        digito8 = int(self.__numero[7])*4
        digito9 = int(self.__numero[8])*3
        digito10 = int(self.__numero[9])*2
        digito11 = int(self.__numero[10])
        totalizador = digito1+digito2+digito3+digito4+digito5+digito6+digito7+digito8+digito9+digito10
        validar = (totalizador*10)%11
        if validar == digito11:
            dv2 = True
        if dv1 == True and dv2 ==True:
            self.__cpf_validado = True
        self.__calculado = True

    def calculado(self):
        return self.__calculado

    def validado(self):
        return self.__cpf_validado
