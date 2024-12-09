import re

ARQUIVO_CLIENTES = "clientes.txt"

__all__ = ["validaCpf", "criaCliente", "atualizaDados", "excluiCliente", "exibeCliente", "exibeTodosClientes"]

# Funções de validação


def validaCpf(cpf):
    """
    -> Objetivo: Validar o CPF fornecido.
    -> Descrição: A função validaCpf() tem como objetivo verificar se o CPF informado é válido, realizando a remoção de caracteres não numéricos e aplicando o algoritmo de verificação do CPF.
    -> Parâmetros de entrada: 
        - cpf (str): O CPF a ser validado.
    -> Retornos previstos:
        - Retorna `True` se o CPF for válido, `False` caso contrário.
    -> Assertivas de entrada:
        - O parâmetro cpf deve ser uma string.
    -> Assertivas de saída:
        - Retorna um valor booleano (True ou False) indicando a validade do CPF.
    """
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False

    def calcula_dv(cpf, pesos):
        soma = sum(int(digit) * peso for digit, peso in zip(cpf, pesos))
        dv = 11 - (soma % 11)
        return 0 if dv > 9 else dv

    if cpf == cpf[0] * len(cpf):
        return False

    pesos_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    dv1 = calcula_dv(cpf[:9], pesos_1)
    dv2 = calcula_dv(cpf[:9] + str(dv1), pesos_2)

    return cpf[-2:] == f'{dv1}{dv2}'

def validaTelefone(telefone):
    """
    -> Objetivo: Validar o número de telefone fornecido.
    -> Descrição: A função validaTelefone() tem como objetivo validar se o telefone informado possui o formato correto (10 ou 11 dígitos).
    -> Parâmetros de entrada:
        - telefone (str): O número de telefone a ser validado.
    -> Retornos previstos:
        - Retorna `True` se o telefone for válido, `False` caso contrário.
    -> Assertivas de entrada:
        - O parâmetro telefone deve ser uma string contendo apenas números.
    -> Assertivas de saída:
        - Retorna um valor booleano (True ou False) indicando a validade do telefone.
    """
    return re.fullmatch(r"\d{10,11}", telefone) is not None

def validaEmail(email):
    """
    -> Objetivo: Validar o endereço de e-mail fornecido.
    -> Descrição: A função validaEmail() tem como objetivo validar o formato de um e-mail, verificando se ele segue o padrão correto.
    -> Parâmetros de entrada:
        - email (str): O endereço de e-mail a ser validado.
    -> Retornos previstos:
        - Retorna `True` se o e-mail for válido, `False` caso contrário.
    -> Assertivas de entrada:
        - O parâmetro email deve ser uma string.
    -> Assertivas de saída:
        - Retorna um valor booleano (True ou False) indicando a validade do e-mail.
    """
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Funções principais

def criaCliente(nome, cpf, endereco, telefone, email):
    """
    -> Objetivo: Criar um novo cliente no sistema.
    -> Descrição: A função criaCliente() tem como objetivo adicionar um novo cliente ao sistema, realizando a validação dos dados (CPF, telefone, e-mail) e verificando se o CPF já está cadastrado.
    -> Parâmetros de entrada: 
        - nome (str): Nome do cliente.
        - cpf (str): CPF do cliente.
        - endereco (str): Endereço do cliente.
        - telefone (str): Número de telefone do cliente.
        - email (str): Endereço de e-mail do cliente.
    -> Retornos previstos:
        - Retorna `True` se o cliente for criado com sucesso, `False` caso contrário.
    -> Assertivas de entrada:
        - O nome, cpf, endereco, telefone e email devem ser strings.
    -> Assertivas de saída:
        - Retorna um valor booleano (True ou False) indicando o sucesso da criação.
    """
    if not validaCpf(cpf):
        return False
    if not validaTelefone(telefone):
        return False
    if not validaEmail(email):
        return False
    if buscaCliente(cpf) != "Cliente não encontrado.":
        return False
    with open(ARQUIVO_CLIENTES, "a") as arquivo:
        arquivo.write(f"{nome};{cpf};{endereco};{telefone};{email}\n")
    return True

def atualizaDados(cpf, endereco_novo=None, telefone_novo=None, email_novo=None):
    """
    -> Objetivo: Atualizar os dados de um cliente existente.
    -> Descrição: A função atualizaDados() tem como objetivo atualizar as informações de um cliente no sistema, validando os novos dados fornecidos (CPF, telefone, e-mail).
    -> Parâmetros de entrada: 
        - cpf (str): O CPF do cliente a ser atualizado.
        - endereco_novo (str, opcional): Novo endereço do cliente.
        - telefone_novo (str, opcional): Novo telefone do cliente.
        - email_novo (str, opcional): Novo e-mail do cliente.
    -> Retornos previstos:
        - Retorna `True` se os dados forem atualizados com sucesso, `False` caso contrário.
    -> Assertivas de entrada:
        - O cpf deve ser uma string e os novos dados (endereco_novo, telefone_novo, email_novo) devem ser strings ou None.
    -> Assertivas de saída:
        - Retorna um valor booleano (True ou False) indicando o sucesso da atualização.
    """
    if not validaCpf(cpf):
        return False
    if telefone_novo and not validaTelefone(telefone_novo):
        return False
    if email_novo and not validaEmail(email_novo):
        return False

    cliente = buscaCliente(cpf)
    if cliente == "Cliente não encontrado.":
        return False

    linhas = []
    atualizado = False

    with open(ARQUIVO_CLIENTES, "r+") as arquivo:
        linhas = arquivo.readlines()
        arquivo.seek(0)
        for linha in linhas:
            dados = linha.strip().split(";")
            if dados[1] == cpf:
                if endereco_novo:
                    dados[2] = endereco_novo
                if telefone_novo:
                    dados[3] = telefone_novo
                if email_novo:
                    dados[4] = email_novo
                atualizado = True
            arquivo.write(";".join(dados) + "\n")
        arquivo.truncate()
    return atualizado

def excluiCliente(cpf):
    """
    -> Objetivo: Excluir um cliente do sistema.
    -> Descrição: A função excluiCliente() tem como objetivo remover um cliente do sistema com base no CPF fornecido, após validar o CPF.
    -> Parâmetros de entrada:
        - cpf (str): O CPF do cliente a ser excluído.
    -> Retornos previstos:
        - Retorna `True` se o cliente for excluído com sucesso, `False` caso contrário.
    -> Assertivas de entrada:
        - O parâmetro cpf deve ser uma string.
    -> Assertivas de saída:
        - Retorna um valor booleano (True ou False) indicando o sucesso da exclusão.
    """
    if not validaCpf(cpf):
        return False

    cliente = buscaCliente(cpf)
    if cliente == "Cliente não encontrado.":
        return False

    with open(ARQUIVO_CLIENTES, "r+") as arquivo:
        linhas = arquivo.readlines()
        arquivo.seek(0)
        for linha in linhas:
            dados = linha.strip().split(";")
            if dados[1] != cpf:
                arquivo.write(linha)
        arquivo.truncate()

    return True

def exibeCliente(cpf):
    """
    -> Objetivo: Exibir os dados de um cliente específico.
    -> Descrição: A função exibeCliente() tem como objetivo mostrar as informações de um cliente, localizado pelo CPF fornecido.
    -> Parâmetros de entrada:
        - cpf (str): O CPF do cliente a ser exibido.
    -> Retornos previstos:
        - Retorna `True` se o cliente for encontrado e exibido com sucesso, `False` caso contrário.
    -> Assertivas de entrada:
        - O parâmetro cpf deve ser uma string.
    -> Assertivas de saída:
        - Retorna um valor booleano (True ou False) indicando o sucesso da exibição.
    """
    cliente = buscaCliente(cpf)
    if cliente == "Cliente não encontrado.":
        return False
    return True

def exibeTodosClientes():
    """
    -> Objetivo: Exibir todos os clientes cadastrados no sistema.
    -> Descrição: A função exibeTodosClientes() tem como objetivo listar todos os clientes registrados no sistema.
    -> Parâmetros de entrada: Nenhum.
    -> Retornos previstos:
        - Retorna `True` se todos os clientes forem exibidos com sucesso, `False` caso contrário.
    -> Assertivas de entrada:
        - Não há validação de entrada, pois a função não recebe parâmetros.
    -> Assertivas de saída:
        - Retorna um valor booleano (True ou False) indicando o sucesso da exibição.
    """
    with open(ARQUIVO_CLIENTES, "r") as arquivo:
        clientes = arquivo.readlines()
        if not clientes:
            return False
    return True

def buscaCliente(cpf):
    """
    -> Objetivo: Buscar um cliente pelo CPF.
    -> Descrição: A função buscaCliente() tem como objetivo procurar um cliente no sistema utilizando o CPF fornecido. Se encontrado, retorna os dados do cliente.
    -> Parâmetros de entrada:
        - cpf (str): O CPF do cliente a ser buscado.
    -> Retornos previstos:
        - Retorna um dicionário com os dados do cliente, caso encontrado. Retorna uma string "Cliente não encontrado." caso não encontre o cliente.
    -> Assertivas de entrada:
        - O parâmetro cpf deve ser uma string.
    -> Assertivas de saída:
        - Retorna um dicionário ou uma string, dependendo se o cliente foi encontrado.
    """
    with open(ARQUIVO_CLIENTES, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if dados[1] == cpf:
                return {
                    "cpf": dados[1],
                    "endereco": dados[2],
                    "telefone": dados[3],
                    "email": dados[4]
                }
    return "Cliente não encontrado."
