import unittest
from clientes import *
from quartos import *
from reservas import *

class TesteModuloClientes(unittest.TestCase):

    def test_criaCliente_sucesso(self):
        print("Caso de Teste 01 - Cliente criado com sucesso")
        resultado = criaCliente("João Silva", "19566062702", "Rua A, 123", "1234567890", "joao@example.com")
        self.assertEqual(resultado, 0)  # Ajustar o valor esperado de acordo com a implementação

    def test_criaCliente_cpf_invalido(self):
        print("Caso de Teste 02 - CPF inválido")
        resultado = criaCliente("Maria Oliveira", "1234567890", "Rua B, 456", "9876543210", "maria@example.com")
        self.assertNotEqual(resultado, 0)

    def test_criaCliente_telefone_invalido(self):
        print("Caso de Teste 03 - Telefone inválido")
        resultado = criaCliente("Carlos Souza", "10987654321", "Rua C, 789", "123456789", "carlos@example.com")
        self.assertNotEqual(resultado, 0)

    def test_criaCliente_email_invalido(self):
        print("Caso de Teste 04 - Email inválido")
        resultado = criaCliente("Ana Costa", "98765432100", "Rua D, 100", "1234567890", "ana@com")
        self.assertNotEqual(resultado, 0)

    def test_criaCliente_cpf_existente(self):
        print("Caso de Teste 05 - CPF já existe")
        resultado = criaCliente("Lucas Lima", "19566062702", "Rua E, 202", "1122334455", "lucas@example.com")
        self.assertNotEqual(resultado, 0)

    def test_criaCliente_parametros_invalidos(self):
        print("Caso de Teste 06 - Parâmetros no formato errado")
        resultado = criaCliente("", "", "", "", "")
        self.assertNotEqual(resultado, 0)

    def test_validaCpf_valido(self):
        print("Caso de Teste 07 - CPF válido")
        resultado = validaCpf("19566062702")
        self.assertTrue(resultado)

    def test_validaCpf_invalido(self):
        print("Caso de Teste 08 - CPF inválido")
        resultado = validaCpf("1234567890")
        self.assertFalse(resultado)

    def test_atualizaDados_sucesso(self):
        print("Caso de Teste 09 - Dados atualizados com sucesso")
        resultado = atualizaDados("19566062702", endereco_novo="Rua F, 303", telefone_novo="1234567890", email_novo="joao@updated.com")
        self.assertEqual(resultado, 0)

    def test_atualizaDados_cpf_invalido(self):
        print("Caso de Teste 10 - CPF inválido")
        resultado = atualizaDados("1234567890", endereco_novo="Rua G, 404")
        self.assertNotEqual(resultado, 0)

    def test_exibeCliente_sucesso(self):
        print("Caso de Teste 11 - Cliente exibido com sucesso")
        resultado = exibeCliente("19566062702")
        self.assertIsNotNone(resultado)

    def test_exibeCliente_cpf_invalido(self):
        print("Caso de Teste 12 - CPF inválido")
        resultado = exibeCliente("1234567890")
        self.assertIsNone(resultado)

    def test_exibeTodosClientes_sucesso(self):
        print("Caso de Teste 13 - Todos os clientes exibidos com sucesso")
        resultado = exibeTodosClientes()
        self.assertIsInstance(resultado, list)

    def test_exibeTodosClientes_sem_clientes(self):
        print("Caso de Teste 14 - Não há clientes cadastrados")
        resultado = exibeTodosClientes()
        self.assertEqual(len(resultado), 0)  # Verifica se a lista está vazia

class TesteModuloQuartos(unittest.TestCase):

    def test_criaQuarto_sucesso(self):
        print(".Caso de Teste 00 - Quarto criado com sucesso:")
        resultado = criaQuarto(101, "single", 150.0, 1, 1)
        self.assertEqual(resultado, 0)

    def test_criaQuarto_numero_invalido(self):
        print(".Caso de Teste 01 - Número do quarto inválido:")
        resultado = criaQuarto("abc", "single", 150.0, 1, 1)
        self.assertNotEqual(resultado, 0)

    def test_criaQuarto_preco_invalido(self):
        print(".Caso de Teste 02 - Preço inválido:")
        resultado = criaQuarto(102, "single", "caro", 1, 1)
        self.assertNotEqual(resultado, 0)

    def test_criaQuarto_tipo_invalido(self):
        print(".Caso de Teste 03 - Tipo de quarto inválido:")
        resultado = criaQuarto(103, "luxury", 150.0, 1, 1)
        self.assertNotEqual(resultado, 0)

    def test_criaQuarto_andar_invalido(self):
        print(".Caso de Teste 04 - Andar inválido:")
        resultado = criaQuarto(104, "single", 150.0, 1, -1)
        self.assertNotEqual(resultado, 0)

    def test_criaQuarto_numero_existente(self):
        print(".Caso de Teste 05 - Número do quarto já existe:")
        criaQuarto(101, "double", 180.0, 2, 2)  # Criar o quarto para simular a existência
        resultado = criaQuarto(101, "double", 180.0, 2, 2)
        self.assertNotEqual(resultado, 0)

    def test_criaQuarto_parametros_invalidos(self):
        print(".Caso de Teste 06 - Parâmetros no formato errado:")
        resultado = criaQuarto("", "", "", "", "")
        self.assertNotEqual(resultado, 0)

    def test_atualizaQuarto_sucesso(self):
        print(".Caso de Teste 00 - Quarto atualizado com sucesso:")
        criaQuarto(101, "single", 150.0, 1, 1)
        resultado = atualizaQuarto(101, preco_diaria=200.0, tipo_de_quarto="double", andar=2, qt_camas=2)
        self.assertEqual(resultado, 0)

    def test_atualizaQuarto_numero_invalido(self):
        print(".Caso de Teste 01 - Número do quarto inválido:")
        resultado = atualizaQuarto("abc", preco_diaria=200.0, tipo_de_quarto="double", andar=2)
        self.assertNotEqual(resultado, 0)

    def test_atualizaQuarto_preco_invalido(self):
        print(".Caso de Teste 02 - Preço inválido:")
        resultado = atualizaQuarto(101, preco_diaria="caro")
        self.assertNotEqual(resultado, 0)

    def test_atualizaQuarto_tipo_invalido(self):
        print(".Caso de Teste 03 - Tipo de quarto inválido:")
        resultado = atualizaQuarto(101, tipo_de_quarto="luxury")
        self.assertNotEqual(resultado, 0)

    def test_atualizaQuarto_andar_invalido(self):
        print(".Caso de Teste 04 - Andar inválido:")
        resultado = atualizaQuarto(101, andar=-1)
        self.assertNotEqual(resultado, 0)

    def test_exibeQuartosDisponiveis_sucesso(self):
        print(".Caso de Teste 00 - Quartos disponíveis exibidos com sucesso:")
        criaQuarto(102, "single", 150.0, 1, 1)
        resultado = exibeQuartosDisponiveis(preco_max=200.0)
        self.assertIsInstance(resultado, list)

    def test_exibeQuartosDisponiveis_sem_resultados(self):
        print(".Caso de Teste 01 - Não há quartos disponíveis para o filtro aplicado:")
        resultado = exibeQuartosDisponiveis(preco_max=50.0)
        self.assertEqual(len(resultado), 0)

    def test_exibeQuarto_sucesso(self):
        print(".Caso de Teste 00 - Quarto exibido com sucesso:")
        criaQuarto(103, "single", 150.0, 1, 1)
        resultado = exibeQuartoNum(103)
        self.assertIsNotNone(resultado)

    def test_exibeQuarto_inexistente(self):
        print(".Caso de Teste 01 - Quarto não encontrado:")
        resultado = exibeQuartoNum(999)
        self.assertIsNone(resultado)

    def test_exibeTodosQuartos_sucesso(self):
        print(".Caso de Teste 00 - Todos os quartos exibidos com sucesso:")
        criaQuarto(104, "double", 180.0, 2, 2)
        resultado = exibeTodosQuartos()
        self.assertIsInstance(resultado, list)

    def test_buscaQuarto_sucesso(self):
        print(".Caso de Teste 00 - Encontra o quarto com sucesso pelo número:")
        criaQuarto(105, "single", 150.0, 1, 1)
        resultado = buscaQuarto(105)
        self.assertIsNotNone(resultado)

    def test_validaNumeroQuarto_valido(self):
        print(".Caso de Teste 00 - Número do quarto válido:")
        criaQuarto(106, "single", 150.0, 1, 1)
        resultado = validaNumeroQuarto(106)
        self.assertTrue(resultado)

    def test_validaNumeroQuarto_invalido(self):
        print(".Caso de Teste 01 - Número do quarto inválido:")
        resultado = validaNumeroQuarto("abc")
        self.assertFalse(resultado)

class TesteModuloReservas(unittest.TestCase):

    def test_hospedaCliente_sucesso(self):
        print(".Caso de Teste 00 - Hospedagem registrada com sucesso:")
        resultado = hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)
        self.assertEqual(resultado, 0)

    def test_hospedaCliente_cpf_invalido(self):
        print(".Caso de Teste 01 - CPF inválido:")
        resultado = hospedaCliente("1234567890", "01/12/2024", "05/12/2024", 101)
        self.assertNotEqual(resultado, 0)

    def test_hospedaCliente_datas_invalidas(self):
        print(".Caso de Teste 02 - Datas inválidas (data de início após data de fim):")
        resultado = hospedaCliente("19566062702", "10/12/2024", "05/12/2024", 102)
        self.assertNotEqual(resultado, 0)

    def test_hospedaCliente_quarto_indisponivel(self):
        print(".Caso de Teste 03 - Quarto indisponível para o período:")
        hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)  # Registrar reserva
        resultado = hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)  # Repetir no mesmo período
        self.assertNotEqual(resultado, 0)

    def test_exibeTodasHospedagens_sucesso(self):
        print(".Caso de Teste 00 - Exibe todas as hospedagens:")
        hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)
        resultado = exibeTodasHospedagens()
        self.assertIsInstance(resultado, list)

    def test_exibeTodasHospedagens_sem_dados(self):
        print(".Caso de Teste 01 - Não há hospedagens:")
        resultado = exibeTodasHospedagens()
        self.assertEqual(len(resultado), 0)

    def test_exibeHistoricoHospedagemCPF_sucesso(self):
        print(".Caso de Teste 00 - Exibe histórico de hospedagens de um cliente:")
        hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)
        resultado = exibeHistoricoHospedagemCPF("19566062702")
        self.assertIsInstance(resultado, list)

    def test_exibeHistoricoHospedagemCPF_nao_encontrado(self):
        print(".Caso de Teste 01 - CPF não encontrado no histórico:")
        resultado = exibeHistoricoHospedagemCPF("1234567890")
        self.assertEqual(len(resultado), 0)

    def test_verificaConflitoReservas_sem_conflito(self):
        print(".Caso de Teste 00 - Não há conflito de reservas:")
        hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)
        resultado = verificaConflitoReservas("06/12/2024", "10/12/2024", 101)  # Período fora do conflito
        self.assertFalse(resultado)

    def test_verificaConflitoReservas_com_conflito(self):
        print(".Caso de Teste 01 - Há conflito de reservas (quarto já reservado):")
        hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)
        resultado = verificaConflitoReservas("01/12/2024", "05/12/2024", 101)  # Mesmo período
        self.assertTrue(resultado)


if __name__ == "__main__":
    unittest.main()
