import datetime

# Importa funções relacionadas a clientes
from clientes import validaCpf, buscaCliente

# Importa funções relacionadas a quartos
from quartos import validaNumeroQuarto, buscaQuarto, verificaConflitoReservas

# Importa funções relacionadas a reservas
from reservas import verificaConflitoReservas

# Importa status e suas funções
from status_code import STATUS_CODE, getStatusName




__all__ = ["STATUS_CODE", "getStatusName", "validaData", "validaHorario", 
           "verificaConflitoHospedagem", "validaQuarto", "validaCliente", 
           "processaErro"]

STATUS_CODE = {
    "SUCESSO": 0,
    # Hospedagem
    "DATA_FIM_MENOR_QUE_INICIO": 771,
    "DATA_PASSOU": 772,
    "FORMATO_DATA_INVALIDO": 773,
    "CONFLITO_RESERVA": 774,
    "HOSPEDAGEM_INEXISTENTE": 775,
    "FORMATO_HORA_INVALIDO": 776,
    "HORA_PASSOU_HOJE": 777,
    "HORA_INVALIDA": 778,
    "HOSPEDAGENS_VAZIAS": 781,
    "HISTORICO_HOSPEDAGEM_CPF_VAZIO": 784,
    # Quartos
    "QUARTO_INVALIDO": 20,
    "PRECO_INVALIDO": 21,
    "QUARTO_EXISTENTE": 22,
    "QUARTO_INEXISTENTE": 27,
    "DATA_INVALIDA": 29,
    "SEM_QUARTOS_DISPONIVEIS": 30,
    # Clientes
    "CPF_INVALIDO": 1,
    # Software
    "ARQUIVOS_NAO_ENCONTRADOS": 2,
    "ERRO_AO_GRAVAR": 3,
}

def getStatusName(retorno):
    """
    Retorna o nome do código de status correspondente ao valor fornecido.
    """
    for nome, valor in STATUS_CODE.items():
        if retorno == valor:
            return nome
    return "Código de status desconhecido"

# Validações
def validaData(data_inicio, data_fim=None):
    """
    Valida as datas fornecidas e retorna o código de status.
    """
    try:
        inicio = datetime.datetime.strptime(data_inicio, "%d/%m/%Y")
        if data_fim:
            fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y")
            if inicio > fim:
                return STATUS_CODE["DATA_FIM_MENOR_QUE_INICIO"]
        if inicio < datetime.datetime.now():
            return STATUS_CODE["DATA_PASSOU"]
    except ValueError:
        return STATUS_CODE["FORMATO_DATA_INVALIDO"]
    return STATUS_CODE["SUCESSO"]

def validaHorario(horario):
    """
    Valida o formato do horário e se já passou no dia atual.
    """
    try:
        hora_atual = datetime.datetime.now()
        hora = datetime.datetime.strptime(horario, "%H:%M").time()
        if hora < hora_atual.time():
            return STATUS_CODE["HORA_PASSOU_HOJE"]
    except ValueError:
        return STATUS_CODE["FORMATO_HORA_INVALIDO"]
    return STATUS_CODE["SUCESSO"]

def verificaConflitoHospedagem(data_inicio, data_fim, numero_quarto):
    """
    Verifica conflito de hospedagens e retorna o status.
    """
    if not validaNumeroQuarto(numero_quarto):  # Origem: quartos.py
        return STATUS_CODE["QUARTO_INVALIDO"]

    status_data = validaData(data_inicio, data_fim)
    if status_data != STATUS_CODE["SUCESSO"]:
        return status_data

    if not verificaConflitoReservas(data_inicio, data_fim, numero_quarto):  # Origem: reservas.py
        return STATUS_CODE["CONFLITO_RESERVA"]
    return STATUS_CODE["SUCESSO"]

def validaQuarto(numero_quarto):
    """
    Valida o número do quarto.
    """
    if not validaNumeroQuarto(numero_quarto):  # Origem: quartos.py
        return STATUS_CODE["QUARTO_INVALIDO"]
    if not buscaQuarto(numero_quarto):  # Origem: quartos.py
        return STATUS_CODE["QUARTO_INEXISTENTE"]
    return STATUS_CODE["SUCESSO"]

def validaCliente(cpf):
    """
    Valida o CPF do cliente.
    """
    if not validaCpf(cpf):  # Origem: clientes.py
        return STATUS_CODE["CPF_INVALIDO"]
    return STATUS_CODE["SUCESSO"]

def processaErro(codigo_erro):
    """
    Processa o erro e retorna a mensagem correspondente.
    """
    status_nome = getStatusName(codigo_erro)
    print(f"Erro ({codigo_erro}): {status_nome}")
    return codigo_erro

# Exemplos de Uso
if __name__ == "__main__":
    # Exemplo: Validação de data
    resultado = validaData("01/12/2024", "30/11/2024")
    processaErro(resultado)

    # Exemplo: Verificação de conflito
    resultado = verificaConflitoHospedagem("02/12/2024", "05/12/2024", 101)
    processaErro(resultado)
