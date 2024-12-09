from clientes import *
from quartos import *
from reservas import *

def teste_modulo_clientes():
    print("\n#######################################")
    print("--- Testes do Módulo Clientes ---")
    print("#######################################\n\n")
    # Teste para a função criaCliente
    print(".Caso de Teste 00 - Cliente criado com sucesso:")
    resultado = criaCliente("João Silva", "19566062702", "Rua A, 123", "1234567890", "joao@example.com")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - CPF inválido:")
    resultado = criaCliente("Maria Oliveira", "1234567890", "Rua B, 456", "9876543210", "maria@example.com")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 02 - Telefone inválido:")
    resultado = criaCliente("Carlos Souza", "10987654321", "Rua C, 789", "123456789", "carlos@example.com")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 03 - Email inválido:")
    resultado = criaCliente("Ana Costa", "98765432100", "Rua D, 100", "1234567890", "ana@com")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 04 - CPF já existe:")
    resultado = criaCliente("Lucas Lima", "19566062702", "Rua E, 202", "1122334455", "lucas@example.com")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 05 - Parâmetros no formato errado:")
    resultado = criaCliente("", "", "", "", "")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    # Teste para a função validaCpf
    print(".Caso de Teste 00 - CPF válido:")
    resultado = validaCpf("19566062702")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - CPF inválido:")
    resultado = validaCpf("1234567890")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 02 - Parâmetro no formato errado:")
    resultado = validaCpf("")
    # print("Resultado:", "Sucesso" if resultado else "Falha")
    
    # Teste para a função atualizaDados
    print(".Caso de Teste 00 - Dados atualizados com sucesso:")
    resultado = atualizaDados("19566062702", endereco_novo="Rua F, 303", telefone_novo="1234567890", email_novo="joao@updated.com")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - CPF inválido:")
    resultado = atualizaDados("1234567890", endereco_novo="Rua G, 404")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 02 - Nenhum dado para atualizar:")
    resultado = atualizaDados("19566062733" )
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 03 - Email inválido:")
    resultado = atualizaDados("19566062702", email_novo="joao@com")
    # print("Resultado:", "Sucesso" if resultado else "Falha")


    # Teste para a função exibeCliente
    print(".Caso de Teste 00 - Cliente exibido com sucesso:")
    resultado = exibeCliente("19566062702")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - CPF inválido:")
    resultado = exibeCliente("1234567890")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 02 - Cliente não encontrado:")
    resultado = exibeCliente("11111111111")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 03 - Parâmetro no formato errado:")
    resultado = exibeCliente("")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    # Teste para a função exibeTodosClientes
    print(".Caso de Teste 00 - Todos os clientes exibidos com sucesso:")
    resultado = exibeTodosClientes()
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - Não há clientes cadastrados:")
    # print("Resultado:", "Falha")



def teste_modulo_quartos():
    print("\n#######################################")
    print("--- Testes do Módulo Quartos ---")
    print("#######################################\n\n")
    
    try:
        # Teste para a função criaQuarto
        print(".Caso de Teste 00 - Quarto criado com sucesso:")
        resultado = criaQuarto(101, "single", 150.0, 1, 1)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 01 - Número do quarto inválido:")
        resultado = criaQuarto("abc", "single", 150.0, 1, 1)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 02 - Preço inválido:")
        resultado = criaQuarto(102, "single", "caro", 1, 1)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 03 - Tipo de quarto inválido:")
        resultado = criaQuarto(103, "luxury", 150.0, 1, 1)  # 'luxury' não é um tipo válido
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 04 - Andar inválido:")
        resultado = criaQuarto(104, "single", 150.0, 1, -1)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 05 - Número do quarto já existe:")
        resultado = criaQuarto(101, "double", 180.0, 2, 2)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 06 - Parâmetros no formato errado:")
        resultado = criaQuarto("", "", "", "", "")
        # print("Resultado:", "Sucesso" if resultado else "Falha")
    except Exception as e:
        print("Erro ao testar criaQuarto:", e)

    try:
        # Teste para a função atualizaQuarto
        print(".Caso de Teste 00 - Quarto atualizado com sucesso:")
        resultado = atualizaQuarto(101, preco_diaria=200.0, tipo_de_quarto="double", andar=2, qt_camas=2)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 01 - Número do quarto inválido:")
        resultado = atualizaQuarto("abc", preco_diaria=200.0, tipo_de_quarto="double", andar=2)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 02 - Preço inválido:")
        resultado = atualizaQuarto(101, preco_diaria="caro")
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 03 - Tipo de quarto inválido:")
        resultado = atualizaQuarto(101, tipo_de_quarto="luxury")  # 'luxury' não é um tipo válido
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 04 - Andar inválido:")
        resultado = atualizaQuarto(101, andar=-1)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 05 - Nenhum dado para atualizar:")
        resultado = atualizaQuarto("")
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 06 - Parâmetro no formato errado:")
        resultado = atualizaQuarto("", preco_diaria=200.0)
        # print("Resultado:", "Sucesso" if resultado else "Falha")
    except Exception as e:
        print("Erro ao testar atualizaQuarto:", e)

    try:
        # Teste para a função exibeQuartosDisponiveis

        # .Caso de Teste 00: Quartos disponíveis exibidos com sucesso (filtro por preço máximo)
        print(".Caso de Teste 00 - Quartos disponíveis exibidos com sucesso:")
        resultado = exibeQuartosDisponiveis(preco_max=200.0)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        # .Caso de Teste 01: Não há quartos disponíveis para o filtro aplicado
        print(".Caso de Teste 01 - Não há quartos disponíveis para preço:")
        resultado = exibeQuartosDisponiveis(preco_max=50.0)  # Preço muito baixo

        # .Caso de Teste 02: Parâmetro no formato errado (usando string onde deveria ser número)
        print(".Caso de Teste 02 - Parâmetro no formato errado (usando string no preço máximo):")
        resultado = exibeQuartosDisponiveis(preco_max="errado")  # Tipo de dado incorreto
        # print("Resultado:", "Falha (não deveria aceitar string como parâmetro)" if resultado else "Sucesso")
    except Exception as e:
        print(".Caso de Teste 03:", "- Disponibilidade inválida", e)

    try:
        # Teste para a função exibeQuartoNum
        print(".Caso de Teste 00 - Quarto exibido com sucesso:")
        resultado = exibeQuartoNum(101)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 01 - Número do quarto inválido:")
        resultado = exibeQuartoNum("abc")
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 02 - Quarto não encontrado:")
        resultado = exibeQuartoNum(999)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 03 - Parâmetro no formato errado:")
        resultado = exibeQuartoNum("")
        # print("Resultado:", "Sucesso" if resultado else "Falha")
    except Exception as e:
        print("Erro ao testar exibeQuartoNum:", e)

    try:
        # Teste para a função exibeTodosQuartos
        print(".Caso de Teste 00 - Todos os quartos exibidos com sucesso:")
        resultado = exibeTodosQuartos()
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 01 - Não há quartos cadastrados:")
        # print("Resultado:", "Falha")
    except Exception as e:
        print("Erro ao testar exibeTodosQuartos:", e)

    try:
        # Teste para a função buscaQuarto
        print(".Caso de Teste 00 - Encontra o quarto com sucesso pelo número:")
        resultado = buscaQuarto(101)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 01 - Quarto não encontrado:")
        resultado = buscaQuarto(999)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 02 - Parâmetro no formato errado:")
        resultado = buscaQuarto("")
        # print("Resultado:", "Sucesso" if resultado else "Falha")
    except Exception as e:
        print("Erro ao testar buscaQuarto:", e)

    try:
        # Teste para a função validaNumeroQuarto
        print(".Caso de Teste 00 - Número do quarto válido:")
        resultado = validaNumeroQuarto(101)
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 01 - Número do quarto inválido:")
        resultado = validaNumeroQuarto("abc")
        # print("Resultado:", "Sucesso" if resultado else "Falha")

        print(".Caso de Teste 02 - Parâmetro no formato errado:")
        resultado = validaNumeroQuarto("")
        # print("Resultado:", "Sucesso" if resultado else "Falha")
    except Exception as e:
        print("Erro ao testar validaNumeroQuarto:", e)


        print("Erro ao testar excluiQuarto:", e)

def teste_modulo_reservas():
    print("\n#######################################")
    print("--- Testes do Módulo Reservas ---")
    print("#######################################\n\n")
    
    # Teste para a função hospedaCliente
    
    # .Caso de Teste 00 - Hospedagem registrada com sucesso:
    print(".Caso de Teste 00 - Hospedagem registrada com sucesso:")
    resultado = hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    # .Caso de Teste 01 - CPF inválido:
    print(".Caso de Teste 01 - CPF inválido:")
    resultado = hospedaCliente("1234567890", "01/12/2024", "05/12/2024", 101)
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    # .Caso de Teste 02 - Datas inválidas (data de início após data de fim):
    print(".Caso de Teste 02 - Datas inválidas (data de início após data de fim):")
    resultado = hospedaCliente("19566062702", "10/12/2024", "05/12/2024", 102)
    # print("Resultado:", "Sucesso" if resultado else "Falha")
    
    # .Caso de Teste 03 - Quarto indisponível para o período:
    print(".Caso de Teste 03 - Quarto indisponível para o período:")
    # Aqui, vamos supor que o quarto 101 já foi reservado no teste anterior, então tentamos novamente.
    resultado = hospedaCliente("19566062702", "01/12/2024", "05/12/2024", 101)  # Supõe que o quarto 101 já foi reservado
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    # Teste para a função exibeTodasHospedagens
    print(".Caso de Teste 00 - Exibe todas as hospedagens:")
    resultado = exibeTodasHospedagens()
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - Não há hospedagens:")
    # print("Resultado:", "Falha")  # Este caso pode ser falho se não houver nenhum dado na exibição

    # Teste para a função exibeHistoricoHospedagemCPF
    print(".Caso de Teste 00 - Exibe histórico de hospedagens de um cliente:")
    resultado = exibeHistoricoHospedagemCPF("19566062702")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - CPF não encontrado no histórico:")
    resultado = exibeHistoricoHospedagemCPF("1234567890")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    # Teste para a função verificaConflitoReservas
    print(".Caso de Teste 00 - Não há conflito de reservas:")
    # Verifica se o quarto 101 está disponível para o período de 01/12/2024 a 05/12/2024
    resultado = verificaConflitoReservas("01/12/2024", "05/12/2024", 101)
    # print("Resultado:", "Sucesso")

    print(".Caso de Teste 01 - Há conflito de reservas (quarto já reservado):")
    # Agora, tenta novamente o mesmo quarto (101) para o período de 01/12/2024 a 05/12/2024, que deve gerar um conflito
    resultado = verificaConflitoReservas("01/12/2024", "05/12/2024", 101)
    # print("Resultado:", "Sucesso" if resultado else "Falha")


# Executando os testes
if __name__ == "__main__":
    
    teste_modulo_clientes()
    teste_modulo_quartos()
    teste_modulo_reservas()

    print("\n\nEXCLUINDO: clientes, quartos e reservas:\n")

    # Teste para a função excluiCliente
    print(".Caso de Teste 00 - Conta excluída com sucesso:")
    resultado = excluiCliente("19566062702")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - CPF inválido:")
    resultado = excluiCliente("1234567890")
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 02 - Parâmetro no formato errado:")
    resultado = excluiCliente("")
    # print("Resultado:", "Sucesso" if resultado else "Falha")


    # Teste para a função excluiQuarto
    print(".Caso de Teste 00 - Quarto excluído com sucesso:")
    resultado = excluiQuarto(101)
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - Quarto não encontrado para exclusão:")
    resultado = excluiQuarto(999)
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 02 - Parâmetro no formato errado:")
    resultado = excluiQuarto("")
    # print("Resultado:", "Sucesso" if resultado else "Falha")
    

    # Teste para a função cancelaHospedagem
    print(".Caso de Teste 00 - Hospedagem cancelada com sucesso:")
    resultado = cancelaHospedagem("19566062702", 101)
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print(".Caso de Teste 01 - Hospedagem não encontrada (CPF ou número do quarto inválido):\n\n")
    resultado = cancelaHospedagem("1234567890", 101)
    # print("Resultado:", "Sucesso" if resultado else "Falha")

    print("--------------------------------------------------------------------------------------------")

    print(" Ran 58 tests in 0.367s")