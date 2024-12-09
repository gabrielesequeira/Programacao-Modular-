import os

ARQUIVO_QUARTOS = "quartos.txt"

__all__ = ["criaQuarto", "atualizaQuarto", "excluiQuarto", "exibeQuartoNum", "exibeTodosQuartos", "exibeQuartosDisponiveis" , "buscaQuarto", "validaNumeroQuarto"]

# Utilitários
def salvarQuartos(quartos):
    """
    -> Objetivo: Salvar as informações dos quartos no arquivo.
    -> Descrição: A função salvarQuartos() grava as informações de todos os quartos fornecidos em um arquivo de texto, garantindo a persistência dos dados no sistema.
    -> Parâmetros de entrada:
        - `quartos` (list): Uma lista contendo os dados de todos os quartos no formato especificado.
    -> Retornos previstos:
        - Nenhum retorno explícito. A função salva os dados no arquivo definido.
    -> Assertivas de entrada:
        - `quartos` deve ser uma lista de listas contendo os detalhes dos quartos, como número, tipo, preço, etc.
    -> Assertivas de saída:
        - Os dados são salvos no arquivo corretamente.
    """
    with open(ARQUIVO_QUARTOS, "w") as arquivo:
        for quarto in quartos:
            linha = ";".join(map(str, quarto)) + "\n"
            arquivo.write(linha)

def carregarQuartos():
    """
    -> Objetivo: Carregar as informações dos quartos do arquivo.
    -> Descrição: A função carregarQuartos() lê as informações dos quartos de um arquivo de texto, converte os dados para o formato correto e os retorna como uma lista de listas.
    -> Parâmetros de entrada: Nenhum.
    -> Retornos previstos:
        - Retorna uma lista de listas com as informações dos quartos, caso o arquivo exista.
        - Retorna uma lista vazia se o arquivo não existir.
    -> Assertivas de entrada:
        - O arquivo deve estar acessível, caso exista.
    -> Assertivas de saída:
        - Retorna os dados no formato esperado ou uma lista vazia.
    """
    if not os.path.exists(ARQUIVO_QUARTOS):
        return []
    with open(ARQUIVO_QUARTOS, "r") as arquivo:
        quartos = []
        for linha in arquivo:
            dados = linha.strip().split(";")
            quarto = [int(dados[0]), dados[1], float(dados[2]), int(dados[3]), int(dados[4]), dados[5]]
            quartos.append(quarto)
        return quartos


# Validações
def validaPreco(preco_diaria):
    """
    -> Objetivo: Validar o preço da diária.
    -> Descrição: A função validaPreco() verifica se o preço fornecido é um valor decimal positivo.
    -> Parâmetros de entrada:
        - `preco_diaria` (float): O preço da diária a ser validado.
    -> Retornos previstos:
        - Retorna `True` se o preço for válido.
        - Retorna `False` caso contrário.
    -> Assertivas de entrada:
        - `preco_diaria` deve ser do tipo float.
    -> Assertivas de saída:
        - Retorna um booleano indicando a validade do preço.
    """
    if not isinstance(preco_diaria, (float)):
        return False
    if preco_diaria <= 0:
        return False
    return True

def validaNumeroQuarto(numero_quarto):
    """
    -> Objetivo: Validar o número do quarto.
    -> Descrição: A função validaNumeroQuarto() verifica se o número do quarto fornecido é um inteiro positivo válido.
    -> Parâmetros de entrada:
        - `numero_quarto` (int): O número do quarto a ser validado.
    -> Retornos previstos:
        - Retorna `True` se o número do quarto for válido.
        - Retorna `False` caso contrário.
    -> Assertivas de entrada:
        - `numero_quarto` deve ser um número inteiro.
    -> Assertivas de saída:
        - Retorna um booleano indicando se o número do quarto é válido.
    """
    if not isinstance(numero_quarto, int):
        return False
    if numero_quarto <= 0:
        return False
    return True

def validaTipoDeQuarto(tipo_de_quarto):
    """
    -> Objetivo: Validar o tipo de quarto.
    -> Descrição: A função validaTipoDeQuarto() verifica se o tipo fornecido é válido, com base em uma lista predefinida de tipos de quartos.
    -> Parâmetros de entrada:
        - `tipo_de_quarto` (str): O tipo de quarto a ser validado.
    -> Retornos previstos:
        - Retorna `True` se o tipo for válido.
        - Retorna `False` caso contrário.
    -> Assertivas de entrada:
        - `tipo_de_quarto` deve ser uma string.
    -> Assertivas de saída:
        - Retorna um booleano indicando a validade do tipo.
    """
    tipos_validos = ["single", "double", "suite", "luxo"]
    if not isinstance(tipo_de_quarto, str):
        return False
    if tipo_de_quarto.lower() not in tipos_validos:
        return False
    return True

def validaAndar(andar):
    """
    -> Objetivo: Validar o número do andar.
    -> Descrição: A função validaAndar() verifica se o número do andar é um inteiro não negativo.
    -> Parâmetros de entrada:
        - `andar` (int): O número do andar a ser validado.
    -> Retornos previstos:
        - Retorna `True` se o número do andar for válido.
        - Retorna `False` caso contrário.
    -> Assertivas de entrada:
        - `andar` deve ser um número inteiro.
    -> Assertivas de saída:
        - Retorna um booleano indicando a validade do andar.
    """
    if not isinstance(andar, int):
        return False
    if andar < 0:
        return False
    return True

def validaStatus(status):
    """
    -> Objetivo: Validar o status do quarto.
    -> Descrição: A função validaStatus() verifica se o status fornecido é válido, com base em uma lista predefinida de status.
    -> Parâmetros de entrada:
        - `status` (str): O status do quarto a ser validado.
    -> Retornos previstos:
        - Retorna `True` se o status for válido.
        - Retorna `False` caso contrário.
    -> Assertivas de entrada:
        - `status` deve ser uma string.
    -> Assertivas de saída:
        - Retorna um booleano indicando a validade do status.
    """
    status_validos = ["disponivel", "indisponivel"]
    if not isinstance(status, str):
        return False
    if status.lower() not in status_validos:
        return False
    return True



# Funções principais

def criaQuarto(numero_quarto, tipo_de_quarto, preco_diaria, qt_camas, andar, status = "disponivel"):
    """
    -> Objetivo: Criar um novo quarto no sistema.
    -> Descrição: A função criaQuarto() é responsável por adicionar um novo quarto ao sistema de reservas. Para isso, a função valida todos os parâmetros de entrada e garante que o quarto ainda não esteja registrado. Se todas as validações forem bem-sucedidas, o quarto é adicionado à lista de quartos e os dados são salvos no arquivo.
    -> Parâmetros de entrada:
        - `numero_quarto` (int): O número do quarto a ser criado.
        - `tipo_de_quarto` (str): O tipo do quarto (exemplo: "single", "suite").
        - `preco_diaria` (float): O preço da diária do quarto.
        - `qt_camas` (int): A quantidade de camas no quarto.
        - `andar` (int): O andar onde o quarto está localizado.
        - `status` (str, opcional): O status do quarto ("disponível" ou "indisponível").
    -> Retornos previstos:
        - Retorna `True` caso o quarto tenha sido criado com sucesso.
        - Retorna `False` caso ocorra algum erro, como validação falhada ou quarto já existente.
    -> Assertivas de entrada:
        - `numero_quarto` deve ser um número inteiro positivo.
        - `tipo_de_quarto` deve ser uma string válida representando um tipo de quarto.
        - `preco_diaria` deve ser um número decimal positivo.
        - `qt_camas` deve ser um número inteiro positivo.
        - `andar` deve ser um número inteiro não negativo.
        - `status` deve ser uma string válida ("disponível" ou "indisponível").
    -> Assertivas de saída:
        - Retorna `True` caso o quarto seja criado corretamente.
        - Retorna `False` caso o quarto já exista ou algum dado de entrada seja inválido.
    """
    if not validaNumeroQuarto(numero_quarto): return False
    if not validaTipoDeQuarto(tipo_de_quarto): return False
    if not validaPreco(preco_diaria): return False
    if not validaAndar(andar): return False
    if not validaStatus(status): return False

    quartos = carregarQuartos()
    if any(q[0] == numero_quarto for q in quartos):
        return False

    novo_quarto = [numero_quarto, tipo_de_quarto, preco_diaria, qt_camas, andar, status]
    quartos.append(novo_quarto)
    salvarQuartos(quartos)
    return True

def excluiQuarto(numero_quarto):
    """
    -> Objetivo: Excluir um quarto do sistema.
    -> Descrição: A função excluiQuarto() tem como objetivo remover um quarto do sistema de reservas, dado seu número. A função valida o número do quarto e, se o quarto for encontrado, o remove da lista de quartos. Os dados são atualizados no arquivo de armazenamento.
    -> Parâmetros de entrada:
        - `numero_quarto` (int): O número do quarto a ser excluído.
    -> Retornos previstos:
        - Retorna `True` se o quarto for excluído com sucesso.
        - Retorna `False` caso o quarto não exista ou o número fornecido seja inválido.
    -> Assertivas de entrada:
        - `numero_quarto` deve ser um número inteiro positivo.
    -> Assertivas de saída:
        - Retorna `True` caso o quarto tenha sido excluído.
        - Retorna `False` caso o quarto não seja encontrado ou a entrada seja inválida.
    """
    if not validaNumeroQuarto(numero_quarto): return False

    quartos = carregarQuartos()
    quartos_filtrados = [q for q in quartos if q[0] != numero_quarto]

    if len(quartos) == len(quartos_filtrados):
        return False

    salvarQuartos(quartos_filtrados)
    return True

def atualizaQuarto(numero_quarto, qt_camas=None, preco_diaria=None, tipo_de_quarto=None, andar=None, status = None):
    """
    -> Objetivo: Atualizar as informações de um quarto no sistema.
    -> Descrição: A função atualizaQuarto() permite a atualização de informações específicas de um quarto, como o número de camas, preço da diária, tipo de quarto, andar e status. A função valida cada dado antes de aplicar as alterações. Se o quarto for encontrado, as mudanças são salvas no arquivo de quartos.
    -> Parâmetros de entrada:
        - `numero_quarto` (int): O número do quarto a ser atualizado.
        - `qt_camas` (int, opcional): A nova quantidade de camas do quarto.
        - `preco_diaria` (float, opcional): O novo preço da diária.
        - `tipo_de_quarto` (str, opcional): O novo tipo de quarto.
        - `andar` (int, opcional): O novo andar do quarto.
        - `status` (str, opcional): O novo status do quarto.
    -> Retornos previstos:
        - Retorna `True` se as atualizações forem feitas com sucesso.
        - Retorna `False` se o quarto não for encontrado ou se algum dado for inválido.
    -> Assertivas de entrada:
        - `numero_quarto` deve ser um número inteiro positivo.
        - `qt_camas`, `preco_diaria`, `tipo_de_quarto`, `andar` e `status` são opcionais, mas devem ser validados quando fornecidos.
    -> Assertivas de saída:
        - Retorna `True` caso a atualização tenha sido realizada com sucesso.
        - Retorna `False` caso o quarto não seja encontrado ou algum dado de entrada seja inválido.
    """
    if not validaNumeroQuarto(numero_quarto): return False

    quartos = carregarQuartos()
    for quarto in quartos:
        if quarto[0] == numero_quarto:
            if preco_diaria is not None:
                if not validaPreco(preco_diaria): return False
                quarto[2] = preco_diaria
            if tipo_de_quarto is not None:
                if not validaTipoDeQuarto(tipo_de_quarto): return False
                quarto[1] = tipo_de_quarto
            if andar is not None:
                if not validaAndar(andar): return False
                quarto[4] = andar
            if qt_camas is not None:
                quarto[3] = qt_camas
            

            salvarQuartos(quartos)
            return True
    return False

def exibeQuartosDisponiveis(preco_max=None, preco_min=None, qt_camas=None, andar=None, tipo_de_quarto=None):
    """
    -> Objetivo: Exibir os quartos disponíveis com base em filtros.
    -> Descrição: A função exibeQuartosDisponiveis() lista os quartos disponíveis para reserva com base nos filtros fornecidos, como preço, quantidade de camas, andar e tipo de quarto. Apenas quartos com o status "disponível" são exibidos.
    -> Parâmetros de entrada:
        - `preco_max` (float, opcional): O preço máximo da diária dos quartos.
        - `preco_min` (float, opcional): O preço mínimo da diária dos quartos.
        - `qt_camas` (int, opcional): A quantidade de camas do quarto.
        - `andar` (int, opcional): O andar onde o quarto está localizado.
        - `tipo_de_quarto` (str, opcional): O tipo de quarto (exemplo: "single", "luxo").
    -> Retornos previstos:
        - Retorna `True` se houver quartos disponíveis que atendem aos filtros fornecidos.
        - Retorna `False` se não houver quartos disponíveis ou se os filtros não corresponderem a nenhum quarto.
    -> Assertivas de entrada:
        - Os filtros são opcionais, mas devem ser do tipo correto quando fornecidos.
    -> Assertivas de saída:
        - Retorna `True` caso haja quartos que atendem aos critérios.
        - Retorna `False` caso não haja quartos disponíveis ou se os filtros não resultarem em nenhum quarto.
    """
    quartos = carregarQuartos()
    filtrados = []

    for quarto in quartos:
        if preco_max is not None and quarto[2] > preco_max:
            continue
        if preco_min is not None and quarto[2] < preco_min:
            continue
        if qt_camas is not None and quarto[3] != qt_camas:
            continue
        if andar is not None and quarto[4] != andar:
            continue
        if tipo_de_quarto is not None and quarto[1].lower() != tipo_de_quarto.lower():
            continue
        if quarto[5] != "disponível":
            continue
        filtrados.append(quarto)

    if not filtrados:
        return False

    for quarto in filtrados:
        print(quarto)
    return True

def exibeQuartoNum(numero_quarto):
    """
    -> Objetivo: Exibir os detalhes de um quarto específico.
    -> Descrição: A função exibeQuartoNum() busca e exibe as informações de um quarto específico, dado seu número. Se o quarto não for encontrado, a função retorna `False`.
    -> Parâmetros de entrada:
        - `numero_quarto` (int): O número do quarto a ser exibido.
    -> Retornos previstos:
        - Retorna `True` e exibe as informações do quarto se ele for encontrado.
        - Retorna `False` se o quarto não for encontrado.
    -> Assertivas de entrada:
        - `numero_quarto` deve ser um número inteiro positivo.
    -> Assertivas de saída:
        - Retorna `True` caso o quarto seja encontrado e exibido.
        - Retorna `False` caso o quarto não seja encontrado.
    """
    if not validaNumeroQuarto(numero_quarto): return False

    quartos = carregarQuartos()
    for quarto in quartos:
        if quarto[0] == numero_quarto:
            return True
    return False

def exibeTodosQuartos():
    """
    -> Objetivo: Exibir todos os quartos cadastrados no sistema.
    -> Descrição: A função exibeTodosQuartos() exibe todas as informações de todos os quartos registrados no sistema.
    -> Parâmetros de entrada: Nenhum.
    -> Retornos previstos:
        - Retorna `True` e exibe todos os quartos.
        - Retorna `False` se não houver quartos registrados.
    -> Assertivas de entrada:
        - Não há validação de entrada, pois a função não recebe parâmetros.
    -> Assertivas de saída:
        - Retorna `True` caso haja quartos cadastrados.
        - Retorna `False` caso não haja quartos cadastrados.
    """
    quartos = carregarQuartos()
    if not quartos:
        return False
    return True

def buscaQuarto(numero_quarto):
    """
    -> Objetivo: Buscar um quarto pelo número.
    -> Descrição: A função buscaQuarto() busca um quarto específico pelo seu número. Se o quarto for encontrado, suas informações são exibidas.
    -> Parâmetros de entrada:
        - `numero_quarto` (int): O número do quarto a ser buscado.
    -> Retornos previstos:
        - Retorna `True` e exibe as informações do quarto se encontrado.
        - Retorna `False` se o quarto não for encontrado.
    -> Assertivas de entrada:
        - `numero_quarto` deve ser um número inteiro positivo.
    -> Assertivas de saída:
        - Retorna `True` caso o quarto seja encontrado e exibido.
        - Retorna `False` caso o quarto não seja encontrado.
    """
    if not validaNumeroQuarto(numero_quarto): return False

    quartos = carregarQuartos()
    for quarto in quartos:
        if quarto[0] == numero_quarto:
            return True
    return False
