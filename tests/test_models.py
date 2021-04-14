from src.models import Cpf

def test_verifica_criacao_em_branco():
    cpf1 = Cpf(1)
    assert None == cpf1.numero()

def test_se_insere_dados_cpf():
    cpf1 = Cpf(1)
    cpf1.set_numero(0)
    assert cpf1.numero() is not None

def test_verifica_se_quantidade_de_digitos_sao_validos():
    cpf1 = Cpf(1)
    cpf1.set_numero('00000000000')
    assert 11 == len(str(cpf1.numero()))

def test_verifica_calculo_de_digitos_verificadores():
    cpf1 = Cpf(1)
    cpf1.set_numero('00000000000')#inserir cpf valido antes de testar
    cpf1.calcula_digitos_validade_cpf()
    assert cpf1.calculado() == True
    assert cpf1.validado() == True
