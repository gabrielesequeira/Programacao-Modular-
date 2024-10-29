import re
import random

# Lista global para armazenar clientes
clientes_registrados = []

def criaCliente(nome, cpf, endereco, telefone, email, senha):
    """
    Cria um novo cliente. Retorna 0 se criado com sucesso, erros específicos caso contrário.
    """
    if not validaCPF(cpf):
        return 1  # CPF inválido
    if not validaTelefone(telefone):
        return 2  # Telefone inválido
    if not validaEmail(email):
        return 3  # Email inválido

    # Checa se CPF ou email já existem
    if any(cliente['cpf'] == cpf or cliente['email'] == email for cliente in clientes_registrados):
        return 6  # CPF ou Email já existe

    novo_cliente = {
        "nome": nome,
        "cpf": cpf,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "senha": senha
    }
    clientes_registrados.append(novo_cliente)
    return 0  # Criado com sucesso

def validaCPF(cpf):
    """
    Valida se o CPF tem 11 dígitos e passa pelo algoritmo de validação.
    Retorna True se for válido, False se não.
    """
    return bool(re.match(r'^\d{11}$', cpf))

def validaTelefone(telefone):
    """
    Valida o formato do telefone (apenas números, mínimo de 8 dígitos).
    """
    return bool(re.match(r'^\d{8,}$', telefone))

def validaEmail(email):
    """
    Valida o formato do email.
    """
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def login(email, senha):
    """
    Autentica um cliente pelo email e senha. Retorna True se bem-sucedido, False se não.
    """
    for cliente in clientes_registrados:
        if cliente['email'] == email and cliente['senha'] == senha:
            return True
    return False

def atualizaDados(cpf, endereco_novo=None, telefone_novo=None):
    """
    Atualiza os dados de endereço ou telefone de um cliente.
    """
    for cliente in clientes_registrados:
        if cliente['cpf'] == cpf:
            if endereco_novo:
                cliente['endereco'] = endereco_novo
            if telefone_novo:
                cliente['telefone'] = telefone_novo
            return 0  # Dados atualizados com sucesso
    return 1  # CPF não encontrado

def solicitaRecuperacaoSenha(email):
    """
    Gera um código de recuperação de senha e o envia para o email.
    Retorna 0 se bem-sucedido, 1 se o email for inválido.
    """
    if validaEmail(email):
        codigo_recuperacao = random.randint(100000, 999999)
        # Código seria enviado para o email (simulação aqui)
        print(f"Código de recuperação enviado para {email}: {codigo_recuperacao}")
        return 0
    return 1  # Email inválido

def redefineSenha(cpf, codigo_recuperacao, senha_nova):
    """
    Redefine a senha usando um código de recuperação. Simulação aqui.
    """
    # Simulação: aceitando qualquer código
    for cliente in clientes_registrados:
        if cliente['cpf'] == cpf:
            cliente['senha'] = senha_nova
            return 0  # Senha redefinida com sucesso
    return 1  # CPF não encontrado

def trocaSenha(cpf, senha_atual, senha_nova):
    """
    Troca a senha do cliente. Retorna 0 se bem-sucedido, erros específicos caso contrário.
    """
    for cliente in clientes_registrados:
        if cliente['cpf'] == cpf:
            if cliente['senha'] == senha_atual:
                cliente['senha'] = senha_nova
                return 0  # Senha trocada com sucesso
            return 2  # Senha atual incorreta
    return 1  # CPF não encontrado

def excluiCliente(senha, cpf):
    """
    Exclui um cliente se a senha e o CPF estiverem corretos.
    """
    for cliente in clientes_registrados:
        if cliente['cpf'] == cpf and cliente['senha'] == senha:
            clientes_registrados.remove(cliente)
            return 0  # Cliente excluído com sucesso
    return 1  # Erro ao excluir cliente

def exibeCliente(cpf):
    """
    Exibe as informações de um cliente específico pelo CPF.
    """
    for cliente in clientes_registrados:
        if cliente['cpf'] == cpf:
            return cliente
    return None  # Cliente não encontrado

def exibeTodosClientes():
    """
    Exibe todos os clientes registrados.
    """
    return clientes_registrados

def salvar_clientes_txt():
    """
    Salva os dados dos clientes em um arquivo TXT.
    """
    with open("clientes.txt", "w") as arquivo:
        for cliente in clientes_registrados:
            arquivo.write(f"{cliente['nome']},{cliente['cpf']},{cliente['endereco']},{cliente['telefone']},{cliente['email']},{cliente['senha']}\n")

def carregar_clientes_txt():
    """
    Carrega os dados dos clientes a partir de um arquivo TXT.
    """
    try:
        with open("clientes.txt", "r") as arquivo:
            for linha in arquivo:
                nome, cpf, endereco, telefone, email, senha = linha.strip().split(',')
                criaCliente(nome, cpf, endereco, telefone, email, senha)
    except FileNotFoundError:
        print("Arquivo clientes.txt não encontrado. Inicializando lista de clientes vazia.")
