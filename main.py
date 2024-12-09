from InquirerPy import prompt
import pyfiglet
import emoji
import os
from time import sleep
from tqdm import tqdm
from yaspin import yaspin
from yaspin.spinners import Spinners
from clientes import *
from quartos import * 
from reservas import *
from software_basico import *



def clear_terminal():
    """Clears the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    """Displays the title with ASCII art and emojis."""
    ascii_art = pyfiglet.figlet_format("Sistema de Hotel")
    moon_emoji = emoji.emojize(":house:")
    border = f"{moon_emoji * 40}\n"
    title_with_moon = f"{border} {ascii_art.strip()} \n{border}"
    print(title_with_moon.center(80))
    
def show_spinner(message,erro=False,cancela=False):
    """Displays a loading spinner with a custom message."""
    with yaspin(Spinners.dots, text=message, color="cyan") as spinner:
        sleep(2)  # Simula a duração do loading
        if erro:
            spinner.fail("❌")
        elif cancela:
            spinner.fail("⛔")
        else:
            spinner.ok("✅")  # Substitui o spinner por um checkmark
        
def descompactando_arquivos():
    print("Descompactando arquivos...")
    for _ in tqdm(range(100), desc="Progresso", ncols=70, ascii=" ▮-", colour="green"):
        sleep(0.03)  # Simula o tempo de descompactação
    decompress("clientes.bin", "clientes.txt")
    decompress("quartos.bin", "quartos.txt")
    decompress("reservas.bin", "reservas.txt")
        
def compactando_arquivos():
    print("Compactando arquivos...")
    for _ in tqdm(range(100), desc="Progresso", ncols=70, ascii=" ▮-", colour="blue"):
        sleep(0.03)  # Simula o tempo de compactação
    compress("clientes.txt" , "clientes.bin")
    compress("quartos.txt" , "quartos.bin")
    compress("reservas.txt" , "reservas.bin")
    decompress("clientes.bin", "saidaCliente.txt")
    decompress("quartos.bin", "saidaQuarto.txt")
    decompress("reservas.bin", "saidaReserva.txt")
        
def prompt_user(questions):
    """Prompts the user with a list of questions and returns the answers."""
    return prompt(questions)

def handle_cancel(message):
    """Handles the cancel operation by displaying a message and waiting for 2 seconds."""
    show_spinner(message,cancela=True)
    sleep(2)

def has_anyBlank(dict,list_exeptions ):
    """Checks if any value in the dictionary is blank."""
    return any(not value and key not in list_exeptions for key, value in dict.items())

def add_cliente_form():
    """Form to add a client."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "cpf", "message": "Digite o cpf do cliente:"},
            {"type": "input", "name": "nome", "message": "Digite o nome do cliente:"},
            {"type": "input", "name": "endereço", "message": "Digite o endereço do cliente:"},
            {"type": "input", "name": "email", "message": "Digite o e-mail do cliente:"},
            {"type": "input", "name": "telefone", "message": "Digite o telefone do cliente:"},
            {"type": "list", "name": "cancelar", "message": "Deseja salvar ou cancelar?", "choices": ["Salvar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de clientes...")
            break

        clear_terminal()
        display_title()
        if not answers["cpf"] and has_anyBlank(answers,['cpf']):
            show_spinner("Salvando cliente...",erro=True)
            print("CPF do cliente é necessario para registra-lo")
            print("informações faltando")
            sleep(3)
            continue
        elif not answers["cpf"]:
            show_spinner("Salvando cliente...",erro=True)
            print("CPF do cliente é necessario para registra-lo")
            sleep(3)
            continue
        elif has_anyBlank(answers,['cpf']):
            show_spinner("Salvando cliente...",erro=True)
            print("Informações faltando")
            sleep(3)
            continue
        show_spinner("Salvando cliente...")
        criaCliente(answers['nome'], answers['cpf'], answers['endereço'], answers["telefone"], answers["email"])
        print(f"CPF: {answers['cpf']}")
        print(f"Nome: {answers['nome']}")
        print(f"Nome: {answers['endereço']}")
        print(f"E-mail: {answers['email']}")
        print(f"Telefone: {answers['telefone']}")
        sleep(3)
        break

def remove_cliente_form():
    """Form to remove a client."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "cpf", "message": "Digite o cpf do cliente a ser removido:"},
            {"type": "list", "name": "cancelar", "message": "Deseja remover ou cancelar?", "choices": ["Remover", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de clientes...")
            break

        clear_terminal()
        display_title()
        if not answers["cpf"]:
            show_spinner("Removendo cliente...",erro=True)
            print("CPF do cliente é necessário para remove-lo")
            sleep(3)
            continue
        show_spinner("Removendo cliente...")
        excluiCliente(answers["cpf"])
        print(f"Cliente com cpf {answers['cpf']} removido com sucesso.")
        sleep(7)
        break

def edit_cliente_form():
    """Form to edit a client."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "cpf", "message": "Digite o cpf do cliente a ser editado:"},
            {"type": "input", "name": "endereço", "message": "Digite o endereço do cliente (deixe em branco para não editar):"},
            {"type": "input", "name": "email", "message": "Digite o e-mail do cliente (deixe em branco para não editar):"},
            {"type": "input", "name": "telefone", "message": "Digite o telefone do cliente (deixe em branco para não editar):"},
            {"type": "list", "name": "cancelar", "message": "Deseja salvar ou cancelar?", "choices": ["Salvar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de clientes...")
            break

        updated_cliente = {key: value for key, value in answers.items() if value and key != 'cancelar'}

        clear_terminal()
        display_title()
        if 'cpf' not in updated_cliente:
            show_spinner("Editando cliente...",erro=True)
            print("Erro: O CPF é obrigatório para editar um cliente.")
            sleep(3)
            continue
        show_spinner("Editando cliente...")
        # Pegando os valores com None caso não tenham sido preenchidos
        cpf = updated_cliente['cpf']
        endereco = updated_cliente.get('endereço', None)
        email = updated_cliente.get('email', None)
        telefone = updated_cliente.get('telefone', None)

        # Chamando a função edit_cliente
        atualizaDados(cpf, endereco_novo= endereco, email_novo= email, telefone_novo= telefone)

        print("Cliente editado com sucesso!")
        sleep(3)
        break

def listar_cliente_form():
    """Form to list a client."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "cpf", "message": "Digite o cpf do cliente a ser listado:"},
            {"type": "list", "name": "cancelar", "message": "Deseja listar ou cancelar?", "choices": ["Listar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de clientes...")
            break

        clear_terminal()
        display_title()
        if not answers["cpf"]:
            show_spinner("Listando cliente...",erro=True)
            print("CPF do cliente é necessário para lista-lo")
            sleep(3)
            continue
        show_spinner("Listando cliente...")
        exibeCliente(answers["cpf"])
        print(f"Cliente com cpf {answers['cpf']} listado com sucesso.")
        sleep(3)
        break

def add_quarto_form():
    """Form to add a room."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "número", "message": "Digite o número do quarto:"},
            {"type": "input", "name": "tipo", "message": "Digite o tipo do quarto:"},
            {"type": "input", "name": "preço", "message": "Digite o preço da diária:"},
            {"type": "input", "name": "camas", "message": "Digite a quantidade de camas:"},
            {"type": "input", "name": "andar", "message": "Digite o andar do quarto:"},
            {"type": "list", "name": "cancelar", "message": "Deseja salvar ou cancelar?", "choices": ["Salvar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de quartos...")
            break

        clear_terminal()
        display_title()
        if not answers["número"] and has_anyBlank(answers,["número"]):
            show_spinner("Salvando quarto...",erro=True)
            print("Número do quarto é necessário para registra-lo")
            print("informações faltando")
            sleep(3)
            continue
        elif not answers["número"]:
            show_spinner("Salvando quarto...",erro=True)
            print("Número do quarto é necessário para registra-lo")
            sleep(3)
            continue
        elif has_anyBlank(answers,["número"]):
            show_spinner("Salvando quarto...",erro=True)
            print("Informações faltando")
            sleep(3)
            continue
        show_spinner("Salvando quarto...")
        criaQuarto(int(answers["número"]), answers["tipo"], float(answers["preço"]), answers["camas"], int(answers["andar"]))  
        print("Quarto cadastrado com sucesso:")
        print(f"Número: {answers['número']}")
        print(f"Tipo: {answers['tipo']}")
        print(f"Preço: {answers['preço']}")
        print(f"Camas: {answers['camas']}")
        print(f"Andar: {answers['andar']}")
        sleep(3)
        break

def remove_quarto_form():
    """Form to remove a room."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "número", "message": "Digite o número do quarto a ser removido:"},
            {"type": "list", "name": "cancelar", "message": "Deseja remover ou cancelar?", "choices": ["Remover", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de quartos...")
            break

        clear_terminal()
        display_title()
        if not answers["número"]:
            show_spinner("Removendo quarto...",erro=True)
            print("Número do quarto é necessário para remove-lo")
            sleep(3)
            continue
        show_spinner("Removendo quarto...")
        excluiQuarto(int(answers["número"]))
        print(f"Quarto com número {answers['número']} removido com sucesso.")
        sleep(3)
        break

def edit_quarto_form():
    """Form to edit a room."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "número", "message": "Digite o número do quarto a ser editado:"},
            {"type": "input", "name": "tipo", "message": "Digite o tipo do quarto (deixe em branco para não editar):"},
            {"type": "input", "name": "preço", "message": "Digite o preço da diária (deixe em branco para não editar):"},
            {"type": "input", "name": "camas", "message": "Digite a quantidade de camas (deixe em branco para não editar):"},
            {"type": "input", "name": "andar", "message": "Digite o andar do quarto (deixe em branco para não editar):"},
            {"type": "list", "name": "cancelar", "message": "Deseja salvar ou cancelar?", "choices": ["Salvar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de quartos...")
            break

        updated_quarto = {key: value for key, value in answers.items() if value and key != 'cancelar'}

        clear_terminal()
        display_title()
        if 'número' not in updated_quarto:
            show_spinner("Editando quarto...",erro=True)
            print("Erro: O número do quarto é obrigatório para editar um quarto.")
            sleep(3)
            continue
        show_spinner("Editando quarto...")
        numero = updated_quarto.get('número',None)
        if numero != None:
            numero = int(numero)
        tipo = updated_quarto.get('tipo',None)
        preco = updated_quarto.get('preço',None)
        if preco != None:
            preco = float(preco)
        camas = updated_quarto.get('camas',None)
        if camas != None:
            camas = int(camas)
        andar = updated_quarto.get('andar',None)
        if andar != None:
            andar = int(andar)
        atualizaQuarto(numero_quarto=numero, qt_camas=camas, preco_diaria=preco, tipo_de_quarto=tipo, andar=andar)
        print("Quarto editado com sucesso:")
        sleep(3)
        break

def listar_quarto_form():
    """Form to list a room."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "número", "message": "Digite o número do quarto a ser listado:"},
            {"type": "list", "name": "cancelar", "message": "Deseja listar ou cancelar?", "choices": ["Listar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de quartos...")
            break

        clear_terminal()
        display_title()
        if not answers["número"]:
            show_spinner("Listando quarto...",erro=True)
            print("O número do quarto é necessário para poder lista-lo")
            sleep(3)
            continue
        show_spinner("Listando quarto...")
        exibeQuartoNum(int(answers["número"]))
        print(f"Quarto com número {answers['número']} listado com sucesso.")
        sleep(3)
        break

#def quartos disponiveis


def add_reserva_form():
    """Form to add a reservation."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "cpf", "message": "Digite o cpf do cliente:"},
            {"type": "input", "name": "número do quarto", "message": "Digite o número do quarto:"},
            {"type": "input", "name": "data de inicio", "message": "Digite a data de início da reserva (Use o formato DD/MM/AAAA):"},
            {"type": "input", "name": "data de fim", "message": "Digite a data de fim da reserva (Use o formato DD/MM/AAAA):"},
            {"type": "list", "name": "cancelar", "message": "Deseja salvar ou cancelar?", "choices": ["Salvar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de reservas...")
            break

        clear_terminal()
        display_title()
        if (not answers["cpf"] or (not answers["número do quarto"])) and has_anyBlank(answers,['cpf','número do quarto']):
            show_spinner("Salvando reserva...",erro=True)
            print("CPF do cliente e o número do quarto são necessários pra adicionar a reserva")
            print("informações faltando")
            sleep(3)
            continue
        elif not answers["cpf"] or (not answers["número do quarto"]):
            show_spinner("Salvando reserva...",erro=True)
            print("CPF do cliente e o número do quarto são necessários pra adicionar a reserva")
            sleep(3)
            continue
        elif has_anyBlank(answers,['cpf','número do quarto']):
            show_spinner("Salvando reserva...",erro=True)
            print("Informações faltando")
            sleep(3)
            continue
        show_spinner("Salvando reserva...")
        hospedaCliente(answers["cpf"], answers["data de inicio"], answers["data de fim"], int(answers["número do quarto"]))
        # print("Reserva cadastrada com sucesso:")
        # print(f"CPF: {answers['cpf']}")
        # print(f"Número do quarto: {answers['número do quarto']}")
        # print(f"Data de início: {answers['data de inicio']}")
        # print(f"Data de fim: {answers['data de fim']}")
        sleep(6)
        break

def remove_reserva_form():
    """Form to remove a reservation."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "cpf", "message": "Digite o cpf do cliente:"},
            {"type": "input", "name": "número do quarto", "message": "Digite o número do quarto:"},
            {"type": "list", "name": "cancelar", "message": "Deseja remover ou cancelar?", "choices": ["Remover", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de reservas...")
            break

        clear_terminal()
        display_title()
        if not answers["cpf"] or (not answers["número do quarto"]):
            show_spinner("Removendo reserva...",erro=True)
            print("CPF do cliente e o número do quarto são necessários pra remover a reserva")
            sleep(3)
            continue
        show_spinner("Removendo reserva...")
        cancelaHospedagem(answers["cpf"], answers["número do quarto"])
        print(f"Reserva do cliente com cpf {answers['cpf']} no quarto {answers['número do quarto']} removida com sucesso.")
        sleep(3)
        break

def edit_reserva_form():
    """Form to edit a reservation."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "cpf", "message": "Digite o cpf do cliente:"},
            {"type": "input", "name": "número do quarto", "message": "Digite o número do quarto:"},
            {"type": "input", "name": "data de inicio", "message": "Digite a data de início da reserva (deixe em branco para não editar):"},
            {"type": "input", "name": "data de fim", "message": "Digite a data de fim da reserva (deixe em branco para não editar):"},
            {"type": "list", "name": "cancelar", "message": "Deseja salvar ou cancelar?", "choices": ["Salvar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de reservas...")
            break

        updated_reserva = {key: value for key, value in answers.items() if value and key != 'cancelar'}

        clear_terminal()
        display_title()
        if ('cpf' and 'número do quarto') not in updated_reserva:
            show_spinner("Editando reserva...",erro=True)
            print("Erro: O CPF do cliente e o número do quarto é obrigatório para editar uma reserva.")
            sleep(3)
            continue
        show_spinner("Editando reserva...")
        cpf = updated_reserva.get('cpf',None)
        numero = updated_reserva.get('número do quarto',None)
        data_inicio = updated_reserva.get('data de inicio',None)
        data_fim = updated_reserva.get('data de fim',None)
        #edit_reserva(cpf,numero,data_inicio = data_inicio, data_fim = data_fim)
        print("Reserva editada com sucesso:")
        sleep(3)
        break

def listar_reserva_form():
    """Form to list a reservation."""
    while True:
        clear_terminal()
        display_title()

        questions = [
            {"type": "input", "name": "cpf", "message": "Digite o cpf do cliente:"},
            {"type": "list", "name": "cancelar", "message": "Deseja listar ou cancelar?", "choices": ["Listar", "Cancelar"]}
        ]

        answers = prompt_user(questions)

        if answers['cancelar'] == "Cancelar":
            handle_cancel("Operação cancelada. Retornando ao menu de reservas...")
            break

        clear_terminal()
        display_title()
        if not answers["cpf"]:
            show_spinner("Listando reserva...",erro=True)
            print("CPF do cliente é necessário para listar as suas reservas")
            sleep(3)
            continue
        show_spinner("Listando reserva...")
        exibeHistoricoHospedagemCPF(answers["cpf"])
        print(f"Reservas do cliente com cpf {answers['cpf']} listada com sucesso.")
        sleep(3)
        break

def main_menu():
    """Displays the main menu and handles user selection."""
    clear_terminal()
    display_title()
    descompactando_arquivos()
    while True:
        clear_terminal()
        display_title()

        menu_questions = [
            {
                'type': 'list',
                'name': 'option',
                'message': 'Selecione entre as opções do hotel:',
                'choices': ['Menu de clientes', 'Menu de quartos', 'Menu de reservas', 'Sair'],
            }
        ]

        answers = prompt_user(menu_questions)
        option = answers['option']

        if option == 'Menu de clientes':
            cliente_menu()
        elif option == 'Menu de quartos':
            quarto_menu()
        elif option == 'Menu de reservas':
            reserva_menu()
        elif option == 'Sair':
            clear_terminal()
            compactando_arquivos()
            print('Saindo...')
            sleep(2)
            clear_terminal()
            break

def cliente_menu():
    """Displays the client menu and handles user selection."""
    while True:
        clear_terminal()
        display_title()

        cliente_questions = [
            {
                'type': 'list',
                'name': 'option',
                'message': 'Selecione entre as opções de clientes:',
                'choices': ['Adicionar cliente', 'Remover cliente', 'Editar cliente', 'Listar cliente', 'Listar clientes', 'Voltar'],
            }
        ]

        answers = prompt_user(cliente_questions)
        option = answers['option']

        if option == 'Adicionar cliente':
            add_cliente_form()
        elif option == 'Remover cliente':
            remove_cliente_form()
        elif option == 'Editar cliente':
            edit_cliente_form()
        elif option == 'Listar cliente':
            listar_cliente_form()
        elif option == 'Listar clientes':
            clear_terminal()
            display_title()
            print('Você escolheu Listar clientes')
            exibeTodosClientes()
            sleep(2)
        elif option == 'Voltar':
            break

def quarto_menu():
    """Displays the room menu and handles user selection."""
    while True:
        clear_terminal()
        display_title()

        quarto_questions = [
            {
                'type': 'list',
                'name': 'option',
                'message': 'Selecione entre as opções de quartos:',
                'choices': ['Adicionar quarto', 'Remover quarto', 'Editar quarto', 'Listar quarto', 'Listar quartos', 'Voltar'],
            }
        ]

        answers = prompt_user(quarto_questions)
        option = answers['option']

        if option == 'Adicionar quarto':
            add_quarto_form()
        elif option == 'Remover quarto':
            remove_quarto_form()
        elif option == 'Editar quarto':
            edit_quarto_form()
        elif option == 'Listar quarto':
            listar_quarto_form()
        elif option == 'Listar quartos':
            clear_terminal()
            display_title()
            print('Você escolheu Listar quartos')
            exibeTodosQuartos()
            sleep(2)
        elif option == 'Voltar':
            break

def reserva_menu():
    """Displays the reservation menu and handles user selection."""
    while True:
        clear_terminal()
        display_title()

        reserva_questions = [
            {
                'type': 'list',
                'name': 'option',
                'message': 'Selecione entre as opções de reservas:',
                'choices': ['Adicionar reserva', 'Remover reserva', 'Editar reserva', 'Listar reserva', 'Listar reservas', 'Voltar'],
            }
        ]

        answers = prompt_user(reserva_questions)
        option = answers['option']

        if option == 'Adicionar reserva':
            add_reserva_form()
        elif option == 'Remover reserva':
            remove_reserva_form()
        elif option == 'Editar reserva':
            edit_reserva_form()
        elif option == 'Listar reserva':
            listar_reserva_form()
        elif option == 'Listar reservas':
            clear_terminal()
            display_title()
            print('Você escolheu Listar reservas')
            exibeTodasHospedagens()
            sleep(2)
        elif option == 'Voltar':
            break

if  __name__ == '__main__':
    main_menu()