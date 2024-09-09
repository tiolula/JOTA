from unittest import TestCase
import negocio.calculadora
# Gisa
# Jé
# Sérgio
# Beto
class TestesDaCalculadora(TestCase):

    #ARRANGE
    def test_soma_1_e_2_retorna_3(self):
        a = 1
        b = 2
        esperado = 3

        #ACT
        resultado = negocio.calculadora.somar(a, b)

        #ASSERT
        self.assertEqual(resultado, esperado)

    #ARRANGE
    def test_comissao_venda_menor_que_10000_retorna_500(self):
        valor_da_venda = 10000
        comissao_esperada = 500

        #ACT
        comissao_calculada = negocio.calculadora.calcula_comissao(valor_da_venda)

        #ASSERT
        self.assertEqual(comissao_calculada, comissao_esperada)   

    #ARRANGE
    def test_comissao_venda_menor_que_20000_retorna_1400(self):
        valor_da_venda = 20000
        comissao_esperada = 1400

        #ACT
        comissao_calculada = negocio.calculadora.calcula_comissao(valor_da_venda)

        #ASSERT
        self.assertEqual(comissao_calculada, comissao_esperada)   
            
               #ARRANGE
    def test_comissao_venda_maior_que_20000_retorna_2000(self):
        valor_da_venda = 20000
        comissao_esperada = 2000

        #ACT
        comissao_calculada = negocio.calculadora.calcula_comissao(valor_da_venda)

        #ASSERT
        self.assertEqual(comissao_calculada, comissao_esperada)   