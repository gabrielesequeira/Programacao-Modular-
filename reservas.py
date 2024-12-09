import datetime
from quartos import *
from clientes import *

__all__ = [ "exibeTodasHospedagens", "exibeHistoricoHospedagemCPF", "hospedaCliente", "cancelaHospedagem", "verificaConflitoReservas"]

# utilitários
def carregarReservas():
    """
    -> Objetivo: Carregar as reservas de hospedagem a partir de um arquivo.
    -> Descrição: A função carregarReservas() lê o arquivo "reservas.txt" e carrega todas as reservas registradas, retornando uma lista de listas contendo informações de cada reserva (CPF, data de início, data de fim e número do quarto).
    -> Parâmetros de entrada: Nenhum.
    -> Retornos previstos:
        - Retorna uma lista de reservas.
    -> Assertivas de entrada: Nenhuma.
    -> Assertivas de saída:
        - Retorna uma lista de listas, onde cada lista representa uma reserva.
    """
    reservas = []
    with open("reservas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            reserva = [dados[0], dados[1], dados[2], int(dados[3])]
            reservas.append(reserva)
    return reservas

def salvarReservas(reservas):
    """
    -> Objetivo: Salvar as reservas em um arquivo.
    -> Descrição: A função salvarReservas() grava as reservas passadas como parâmetro no arquivo "reservas.txt". Cada reserva é salva em uma linha do arquivo com os dados separados por ponto e vírgula.
    -> Parâmetros de entrada:
        - `reservas` (list): Lista de reservas a serem salvas.
    -> Retornos previstos: Nenhum.
    -> Assertivas de entrada:
        - `reservas` deve ser uma lista de listas, onde cada lista contém informações de uma reserva.
    -> Assertivas de saída:
        - Nenhum retorno, a função grava as informações no arquivo.
    """
    with open("reservas.txt", "w") as arquivo:
        for reserva in reservas:
            linha = f"{reserva[0]};{reserva[1]};{reserva[2]};{reserva[3]}"
            arquivo.write(linha)

# Validações
def validaDatas(data_inicio, data_fim=None):
    """
    -> Objetivo: Validar as datas fornecidas para uma reserva.
    -> Descrição: A função validaDatas() valida as datas de início e fim fornecidas. Ela verifica se estão no formato correto e se a data de início não é posterior à data de fim.
    -> Parâmetros de entrada:
        - `data_inicio` (str): A data de início no formato "dd/mm/aaaa".
        - `data_fim` (str, opcional): A data de fim no formato "dd/mm/aaaa".
    -> Retornos previstos:
        - Retorna `True` se as datas forem válidas.
        - Retorna `False` se as datas forem inválidas ou estiverem em formato incorreto.
    -> Assertivas de entrada:
        - `data_inicio` e `data_fim` devem ser strings no formato "dd/mm/aaaa".
    -> Assertivas de saída:
        - Retorna `True` se as datas forem válidas.
        - Retorna `False` se houver erro no formato ou na lógica das datas.
    """
    try:
        data_inicio = datetime.datetime.strptime(data_inicio, "%d/%m/%Y")
        if data_fim:
            data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
            if data_inicio > data_fim:
                return False
    except ValueError:
        return False

    return True

def verificaConflitoReservas(data_inicio, data_fim, numero_quarto):
    """
    -> Objetivo: Verificar se há conflito de reservas para o mesmo quarto em um período.
    -> Descrição: A função verificaConflitoReservas() verifica se existe algum conflito de datas entre as reservas já registradas e uma nova tentativa de reserva para o mesmo quarto.
    -> Parâmetros de entrada:
        - `data_inicio` (str): A data de início da reserva no formato "dd/mm/aaaa".
        - `data_fim` (str): A data de fim da reserva no formato "dd/mm/aaaa".
        - `numero_quarto` (int): O número do quarto a ser reservado.
    -> Retornos previstos:
        - Retorna `True` se não houver conflito de reservas.
        - Retorna `False` se houver conflito de datas.
    -> Assertivas de entrada:
        - `data_inicio` e `data_fim` devem ser strings no formato "dd/mm/aaaa".
        - `numero_quarto` deve ser um número inteiro positivo.
    -> Assertivas de saída:
        - Retorna `True` se não houver conflito de reservas.
        - Retorna `False` se houver conflito.
    """
    try:
        data_inicio = datetime.datetime.strptime(data_inicio, "%d/%m/%Y")
        data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
    except ValueError:
        print("Parâmetros no formato errado.")
        return False

    if data_inicio > data_fim:
        return False

    reservas = carregarReservas()  # Carrega as reservas do arquivo
    for reserva in reservas:
        if reserva[3] == numero_quarto:  # Acessa o número do quarto pelo índice 3
            data_reserva_inicio = datetime.datetime.strptime(reserva[1], "%d/%m/%Y")  # Data de início está no índice 1
            data_reserva_fim = datetime.datetime.strptime(reserva[2], "%d/%m/%Y")  # Data de fim está no índice 2
            if (data_inicio <= data_reserva_fim and data_fim >= data_reserva_inicio):
                return False

    return True

# Funções Principais
def hospedaCliente(cpf, data_inicio, data_fim, numero_quarto):
    """
    -> Objetivo: Registrar uma nova hospedagem para um cliente.
    -> Descrição: A função hospedaCliente() registra uma nova hospedagem, verificando a validade do CPF, das datas, do número do quarto e se o quarto está disponível no período. Se todas as validações forem bem-sucedidas, a reserva é salva no arquivo e o status do quarto é alterado para "indisponível".
    -> Parâmetros de entrada:
        - `cpf` (str): O CPF do cliente a ser hospedado.
        - `data_inicio` (str): A data de início da hospedagem no formato "dd/mm/aaaa".
        - `data_fim` (str): A data de fim da hospedagem no formato "dd/mm/aaaa".
        - `numero_quarto` (int): O número do quarto a ser reservado.
    -> Retornos previstos:
        - Retorna `True` se a hospedagem for realizada com sucesso.
        - Retorna `False` se ocorrer algum erro ou se as validações falharem.
    -> Assertivas de entrada:
        - `cpf` deve ser uma string contendo um CPF válido.
        - `data_inicio` e `data_fim` devem ser strings no formato "dd/mm/aaaa".
        - `numero_quarto` deve ser um número inteiro positivo.
    -> Assertivas de saída:
        - Retorna `True` caso a hospedagem seja registrada com sucesso.
        - Retorna `False` caso algum erro de validação ocorra.
    """
    if not validaCpf(cpf):
        return False

    if not validaDatas(data_inicio, data_fim):
        return False

    if not validaNumeroQuarto(numero_quarto):
        return False

    if not verificaConflitoReservas(data_inicio, data_fim, numero_quarto):
        return False

    # Carrega as reservas do arquivo e adiciona a nova
    reservas = carregarReservas()
    reservas.append([cpf, data_inicio, data_fim, numero_quarto])
    # Salva novamente no arquivo
    salvarReservas(reservas)
    
    # Acessa o número do quarto da última reserva e atualiza o status
    if len(reservas) > 0:
        if not atualizaQuarto(reservas[-1][3], status='indisponivel'):
            return False
    
    return True

def cancelaHospedagem(cpf, numero_quarto):
    """
    -> Objetivo: Cancelar uma hospedagem de um cliente.
    -> Descrição: A função cancelaHospedagem() permite cancelar uma reserva de um cliente, removendo-a do arquivo de reservas. A função verifica se a reserva existe antes de realizar o cancelamento.
    -> Parâmetros de entrada:
        - `cpf` (str): O CPF do cliente que deseja cancelar a reserva.
        - `numero_quarto` (int): O número do quarto da reserva a ser cancelada.
    -> Retornos previstos:
        - Retorna `True` se a hospedagem for cancelada com sucesso.
        - Retorna `False` se não houver reserva correspondente ao CPF e número do quarto.
    -> Assertivas de entrada:
        - `cpf` deve ser uma string contendo um CPF válido.
        - `numero_quarto` deve ser um número inteiro positivo.
    -> Assertivas de saída:
        - Retorna `True` caso o cancelamento seja realizado com sucesso.
        - Retorna `False` caso não haja reserva correspondente.
    """
    reservas = carregarReservas()  # Carrega as reservas do arquivo
    for reserva in reservas:
        if reserva[0] == cpf and reserva[3] == numero_quarto:  # Acessa o CPF pelo índice 0 e o número do quarto pelo índice 3
            reservas.remove(reserva)
            # Salva as reservas novamente no arquivo
            salvarReservas(reservas)
            return True

    return False

def exibeTodasHospedagens():
    """
    -> Objetivo: Exibir todas as hospedagens registradas.
    -> Descrição: A função exibeTodasHospedagens() mostra todas as reservas registradas no sistema. Se não houver nenhuma reserva, retorna `False`.
    -> Parâmetros de entrada: Nenhum.
    -> Retornos previstos:
        - Retorna `True` e exibe todas as hospedagens.
        - Retorna `False` se não houver nenhuma hospedagem.
    -> Assertivas de entrada: Nenhuma.
    -> Assertivas de saída:
        - Retorna `True` caso existam hospedagens a serem exibidas.
        - Retorna `False` caso não haja nenhuma hospedagem.
    """
    reservas = carregarReservas()
    if not reservas:
        return False
    return True

def exibeHistoricoHospedagemCPF(cpf):
    """
    -> Objetivo: Exibir o histórico de hospedagens de um cliente específico.
    -> Descrição: A função exibeHistoricoHospedagemCPF() busca todas as reservas de um cliente com base no CPF e as exibe. Caso não haja histórico, retorna `False`.
    -> Parâmetros de entrada:
        - `cpf` (str): O CPF do cliente para o qual deseja-se exibir o histórico.
    -> Retornos previstos:
        - Retorna `True` se houver histórico de hospedagens e exibe as reservas.
        - Retorna `False` se não houver reservas para o CPF informado.
    -> Assertivas de entrada:
        - `cpf` deve ser uma string contendo um CPF válido.
    -> Assertivas de saída:
        - Retorna `True` caso o histórico de hospedagem seja exibido com sucesso.
        - Retorna `False` caso o histórico não seja encontrado.
    """
    if not validaCpf(cpf):
        return False

    reservas = carregarReservas()  # Carrega as reservas do arquivo
    historico = [reserva for reserva in reservas if reserva[0] == cpf]
    if not historico:
        return False

    return True
