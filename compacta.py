import pickle

# Códigos de retorno para operações de compactação/descompactação
CODES = {
    "SUCESSO": 0,
    "ERRO_IO": 1,
    "ERRO_SERIALIZACAO": 2,
    "ERRO_DESERIALIZACAO": 3
}

def compactar_lista(lista, arquivo):
    """
    Compacta uma lista de dicionários e grava em um arquivo binário.
    Retorna o código de sucesso ou erro.
    """
    try:
        pickle.dump(lista, arquivo)  # Aqui ocorre a transformação para binário
        return CODES["SUCESSO"]
    except IOError:
        return CODES["ERRO_IO"]
    except pickle.PicklingError:
        return CODES["ERRO_SERIALIZACAO"]

def descompactar_lista(arquivo):
    """
    Descompacta dados de um arquivo binário para uma lista de dicionários.
    Retorna um tuplo (código de sucesso/erro, lista de dados).
    """
    try:
        lista = pickle.load(arquivo)  # Aqui ocorre a leitura dos dados binários e a transformação de volta para Python
        return (CODES["SUCESSO"], lista)
    except IOError:
        return (CODES["ERRO_IO"], [])
    except pickle.UnpicklingError:
        return (CODES["ERRO_DESERIALIZACAO"], [])
