import json, zlib

__all__ = [
    "compactar_dados",
    "descompactar_dados"
]

# Códigos de Retorno
CODES = {
    "SUCESSO": 0,
    "ERRO_ARQUIVO": 1,           # Erro geral relacionado ao arquivo (leitura/escrita)
    "ERRO_CODIFICACAO": 2,       # Erro durante a codificação dos dados
    "ERRO_DECODIFICACAO": 3,     # Erro durante a decodificação dos dados
    "ERRO_CONSTRUCAO_ARVORE": 4, # Erro na construção da árvore de Huffman
    "ERRO_FORMATO_DADOS": 5      # Erro no formato dos dados do arquivo
}

# Funções de Acesso
def compactar_dados(lista_dicionarios, arquivo):
    """
    Compacta uma lista de dicionários e salva em um arquivo binário já aberto.

    Args:
        lista_dicionarios (list of dict): A lista de dicionários a ser compactada.
        arquivo (file-like object): Um objeto de arquivo binário aberto para escrita.

    Returns:
        int: Um inteiro contendo um código de retorno.
    """
    try:
        string_lista = str(lista_dicionarios)
        frequencias = calcular_frequencias(string_lista)
        arvore_huffman = criar_arvore_huffman(frequencias)
        codigos_huffman = gerar_codigos_huffman(arvore_huffman)
        dados_codificados = codificar_dados(string_lista, codigos_huffman)
        salvar_binario(dados_codificados, codigos_huffman, arquivo)
        return CODES["SUCESSO"]
    except (OSError, IOError):
        return CODES["ERRO_ARQUIVO"]
    except ValueError:
        return CODES["ERRO_CODIFICACAO"]
    except Exception:
        return CODES["ERRO_CODIFICACAO"]

def descompactar_dados(arquivo):
    """
    Lê um arquivo binário compactado e retorna a lista de dicionários descompactada.

    Args:
        arquivo (file-like object): Um objeto de arquivo binário aberto para leitura.

    Returns:
        tuple: Uma tupla contendo um código de retorno e o retorno em si.
    """
    try:
        dados_codificados, codigos_huffman = ler_binario(arquivo)
        dados_decodificados = decodificar_dados(dados_codificados, codigos_huffman)
        lista_dicionarios = converter_para_lista(dados_decodificados)
        return (CODES["SUCESSO"], lista_dicionarios)
    except (OSError, IOError):
        return (CODES["ERRO_ARQUIVO"], [])
    except ValueError as e:
        return (CODES["ERRO_DECODIFICACAO"], str(e))
    except Exception as e:
        return (CODES["ERRO_DECODIFICACAO"], str(e))


# Funções Internas (Auxiliares)
def calcular_frequencias(texto):
    """
    Calcula a frequência de cada caractere na string JSON que representa a lista de dicionários.

    Args:
        texto (str): A string JSON representando a lista de dicionários.

    Returns:
        dict: Um dicionário com a frequência de cada caractere encontrado na string JSON.
    """
    frequencias = {}
    for caractere in texto:
        frequencias[caractere] = frequencias.get(caractere, 0) + 1

    return frequencias

def criar_arvore_huffman(frequencias):
    """
    Constrói a árvore de Huffman usando uma lista de prioridade manual.

    Args:
        frequencias (dict): Um dicionário com a frequência de cada caractere.

    Returns:
        list of tuples: A árvore de Huffman representada como uma lista de tuplas (caractere, código).
    """
    heap = [[freq, [simbolo, ""]] for simbolo, freq in frequencias.items()]

    while len(heap) > 1:
        heap.sort()
        menor = heap.pop(0)
        maior = heap.pop(0)

        for par in menor[1:]:
            par[1] = '0' + par[1]
        for par in maior[1:]:
            par[1] = '1' + par[1]

        heap.append([menor[0] + maior[0]] + menor[1:] + maior[1:])

    return sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

def gerar_codigos_huffman(arvore_huffman):
    """
    Gera um dicionário de códigos de Huffman a partir da árvore.

    Args:
        arvore_huffman (list of tuples): A árvore de Huffman representada como uma lista de tuplas (caractere, código).

    Returns:
        dict: Um dicionário com os códigos de Huffman para cada caractere.
    """
    return {simbolo: codigo for simbolo, codigo in arvore_huffman}

def codificar_dados(texto, codigos_huffman):
    """
    Codifica a string JSON que representa a lista de dicionários utilizando os códigos de Huffman.

    Args:
        texto (str): A string JSON representando a lista de dicionários.
        codigos_huffman (dict): Um dicionário com os códigos de Huffman para cada caractere.

    Returns:
        str: O texto codificado resultante da codificação da string JSON.
    """
    texto_codificado = ""

    for caractere in texto:
        if caractere in codigos_huffman:
            texto_codificado += codigos_huffman[caractere]
        else:
            raise ValueError(f"Caractere '{caractere}' não encontrado no código de Huffman.")

    return texto_codificado

def decodificar_dados(texto_codificado, codigos_huffman):
    """
    Decodifica o texto codificado utilizando o código de Huffman.

    Args:
        texto_codificado (str): O texto codificado a ser decodificado.
        codigos_huffman (dict): Um dicionário com os códigos de Huffman para cada caractere.

    Returns:
        str: O texto decodificado.
    """
    # Inverte o dicionário de códigos de Huffman para decodificação
    codigos_invertidos = {codigo: simbolo for simbolo, codigo in codigos_huffman.items()}

    simbolo_atual = ""
    texto_decodificado = ""

    for bit in texto_codificado:
        simbolo_atual += bit

        # Verifica se o prefixo atual corresponde a um símbolo no código invertido
        if simbolo_atual in codigos_invertidos:
            texto_decodificado += codigos_invertidos[simbolo_atual]
            simbolo_atual = ""

    return texto_decodificado

def converter_para_lista(texto):
    """
    Converte o texto decodificado de volta para uma lista de dicionários.

    Args:
        texto (str): O texto decodificado em formato JSON a ser convertido em lista de dicionários.

    Returns:
        list of dict: A lista de dicionários resultante da conversão do texto.
    """
    try:
        texto = texto.replace("'", '"')
        lista_dicionarios = json.loads(texto)
        if not isinstance(lista_dicionarios, list):
            raise ValueError("O texto JSON não representa uma lista.")
        for item in lista_dicionarios:
            if not isinstance(item, dict):
                raise ValueError("Os itens na lista JSON não são dicionários.")
        return lista_dicionarios
    except json.JSONDecodeError:
        raise ValueError("Erro ao decodificar o texto JSON.")

def salvar_binario(dados_codificados, codigos_huffman, arquivo):
    """
    Escreve o texto codificado e o código de Huffman manualmente em um arquivo binário já aberto.

    Args:
        dados_codificados (str): O texto codificado a ser escrito no arquivo.
        codigos_huffman (dict): Um dicionário com os códigos de Huffman para cada caractere.
        arquivo (file-like object): Um objeto de arquivo binário aberto para escrita.

    Returns:
        None: A função não retorna nada. Os dados são escritos no arquivo.
    """
    try:
        tamanho = len(dados_codificados)
        arquivo.write(tamanho.to_bytes(4, 'little')) 

        valor = int(dados_codificados, 2).to_bytes((tamanho + 7) // 8, 'big')
        arquivo.write(valor)

        dados_json = json.dumps(codigos_huffman).encode('utf-8')
        dados_comprimidos = zlib.compress(dados_json)

        arquivo.write(len(dados_comprimidos).to_bytes(4, 'little'))  

        arquivo.write(dados_comprimidos)
    except (OSError, IOError) as e:
        raise RuntimeError(f"Erro ao escrever no arquivo: {e}")


def ler_binario(arquivo):
    """
    Lê o texto codificado e o código de Huffman manualmente de um arquivo binário já aberto.

    Args:
        arquivo (file-like object): Um objeto de arquivo binário aberto para leitura.

    Returns:
        tuple: Uma tupla contendo o texto codificado (str) e o dicionário de códigos de Huffman (dict).
g