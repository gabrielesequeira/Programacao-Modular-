# Lista global para armazenar os quartos
quartos_disponiveis = []

def criaQuarto(numero_quarto, descricao, preco_diaria, qt_camas, andar, status='disponível'):
    """
    Cria um novo quarto e adiciona à lista de quartos disponíveis.
    Retorna 0 se criado com sucesso, 1 se o número do quarto já existir.
    """
    if not validaNumeroQuarto(numero_quarto):
        return 1  # Número do quarto já existe ou é inválido

    if not validaPreco(preco_diaria):
        return 2  # Preço inválido

    novo_quarto = {
        "numero": numero_quarto,
        "descricao": descricao,
        "preco_diaria": preco_diaria,
        "qt_camas": qt_camas,
        "andar": andar,
        "status": status
    }
    quartos_disponiveis.append(novo_quarto)
    return 0  # Criado com sucesso

def validaPreco(preco_diaria):
    """
    Valida se o preço da diária é positivo.
    Retorna True se for válido, False se não.
    """
    return preco_diaria > 0

def validaNumeroQuarto(numero_quarto):
    """
    Valida se o número do quarto é positivo e se já existe.
    Retorna True se for válido, False se não.
    """
    return numero_quarto > 0 and not any(quarto['numero'] == numero_quarto for quarto in quartos_disponiveis)

def excluiQuarto(numero_quarto):
    """
    Exclui um quarto pelo número. Retorna 0 se excluído com sucesso, 1 se o quarto não existir.
    """
    for quarto in quartos_disponiveis:
        if quarto['numero'] == numero_quarto:
            quartos_disponiveis.remove(quarto)
            return 0  # Excluído com sucesso
    return 1  # Quarto não encontrado

def atualizaQuarto(numero_quarto, status=None, preco_diaria=None, descricao=None):
    """
    Atualiza as informações de um quarto. Retorna 0 se atualizado com sucesso, 1 se o quarto não existir.
    """
    for quarto in quartos_disponiveis:
        if quarto['numero'] == numero_quarto:
            if status is not None:
                quarto['status'] = status
            if preco_diaria is not None and validaPreco(preco_diaria):
                quarto['preco_diaria'] = preco_diaria
            if descricao is not None:
                quarto['descricao'] = descricao
            return 0  # Atualizado com sucesso
    return 1  # Quarto não encontrado

def exibeQuartosDisponiveis(preco_max=None, qt_camas=None, andar=None):
    """
    Exibe os quartos disponíveis que atendem aos critérios fornecidos.
    """
    resultados = [quarto for quarto in quartos_disponiveis if quarto['status'] == 'disponível']

    if preco_max is not None:
        resultados = [q for q in resultados if q['preco_diaria'] <= preco_max]

    if qt_camas is not None:
        resultados = [q for q in resultados if q['qt_camas'] == qt_camas]

    if andar is not None:
        resultados = [q for q in resultados if q['andar'] == andar]

    return resultados

def exibeQuartoNum(numero_quarto):
    """
    Exibe as informações de um quarto específico pelo número.
    Retorna None se o quarto não for encontrado.
    """
    for quarto in quartos_disponiveis:
        if quarto['numero'] == numero_quarto:
            return quarto
    return None

def exibeTodosQuartos():
    """
    Exibe todos os quartos cadastrados.
    """
    return quartos_disponiveis

def salvar_quartos_txt():
    """
    Salva os dados dos quartos em um arquivo TXT.
    """
    with open("quartos.txt", "w") as arquivo:
        for quarto in quartos_disponiveis:
            arquivo.write(f"{quarto['numero']},{quarto['descricao']},{quarto['preco_diaria']},{quarto['qt_camas']},{quarto['andar']},{quarto['status']}\n")

def carregar_quartos_txt():
    """
    Carrega os dados dos quartos a partir de um arquivo TXT.
    """
    try:
        with open("quartos.txt", "r") as arquivo:
            for linha in arquivo:
                numero, descricao, preco, qt_camas, andar, status = linha.strip().split(',')
                criaQuarto(int(numero), descricao, float(preco), int(qt_camas), int(andar), status)
    except FileNotFoundError:
        print("Arquivo quartos.txt não encontrado. Inicializando lista de quartos vazia.")
