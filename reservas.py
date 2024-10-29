from datetime import datetime

# Listas globais para armazenar reservas e massagens
reservas = []
massagens = []

def hospedaCliente(cpf, data_inicio, data_fim, numero_quarto):
    """
    Hospeda um cliente se houver disponibilidade do quarto no período especificado.
    Retorna 0 se bem-sucedido, erros específicos caso contrário.
    """
    if not validaDatas(data_inicio, data_fim):
        return 2  # Datas inválidas

    if verificaConflitoReservas(data_inicio, data_fim, numero_quarto):
        return 3  # Conflito de reserva, quarto já reservado nesse período

    nova_reserva = {
        "cpf": cpf,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "numero_quarto": numero_quarto
    }
    reservas.append(nova_reserva)
    return 0  # Hospedagem feita com sucesso

def verificaConflitoReservas(data_inicio, data_fim, numero_quarto):
    """
    Verifica se há conflito de reserva para o quarto e período especificado.
    Retorna True se houver conflito, False caso contrário.
    """
    for reserva in reservas:
        if reserva['numero_quarto'] == numero_quarto:
            if not (data_fim < reserva['data_inicio'] or data_inicio > reserva['data_fim']):
                return True
    return False

def cancelaHospedagem(cpf, data_inicio, data_fim, numero_quarto):
    """
    Cancela uma hospedagem existente.
    Retorna 0 se cancelada com sucesso, erros específicos caso contrário.
    """
    for reserva in reservas:
        if reserva['cpf'] == cpf and reserva['data_inicio'] == data_inicio and reserva['data_fim'] == data_fim and reserva['numero_quarto'] == numero_quarto:
            reservas.remove(reserva)
            # Cancelar massagens associadas a essa hospedagem
            massagens[:] = [m for m in massagens if not (m['cpf'] == cpf and m['data'] >= data_inicio and m['data'] <= data_fim)]
            return 0  # Hospedagem cancelada com sucesso
    return 4  # Hospedagem não existe

def validaDatas(data_inicio, data_fim=None):
    """
    Valida o formato e a consistência das datas fornecidas.
    Retorna True se forem válidas, False caso contrário.
    """
    try:
        data_inicio_obj = datetime.strptime(data_inicio, '%d/%m/%Y')
        if data_fim:
            data_fim_obj = datetime.strptime(data_fim, '%d/%m/%Y')
            if data_fim_obj < data_inicio_obj:
                return False  # Data de fim é anterior à data de início
        return True
    except ValueError:
        return False  # Formato de data inválido

def exibeTodasHospedagens():
    """
    Exibe todas as hospedagens registradas.
    """
    return reservas if reservas else "Não existe nenhuma hospedagem marcada."

def exibeHistoricoHospedagemCPF(cpf):
    """
    Exibe o histórico de hospedagens de um cliente específico.
    Retorna None se não houver histórico.
    """
    historico = [reserva for reserva in reservas if reserva['cpf'] == cpf]
    return historico if historico else None

def salvar_reservas_txt():
    """
    Salva os dados das reservas em um arquivo TXT.
    """
    with open("reservas.txt", "w") as arquivo:
        for reserva in reservas:
            arquivo.write(f"{reserva['cpf']},{reserva['data_inicio']},{reserva['data_fim']},{reserva['numero_quarto']}\n")

def carregar_reservas_txt():
    """
    Carrega os dados das reservas a partir de um arquivo TXT.
    """
    try:
        with open("reservas.txt", "r") as arquivo:
            for linha in arquivo:
                cpf, data_inicio, data_fim, numero_quarto = linha.strip().split(',')
                hospedaCliente(cpf, data_inicio, data_fim, int(numero_quarto))
    except FileNotFoundError:
        print("Arquivo reservas.txt não encontrado. Inicializando lista de reservas vazia.")
