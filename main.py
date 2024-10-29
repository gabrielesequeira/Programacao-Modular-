import compacta
import cliente
import quartos
import reservas

def carregar_dados():
    # Carregar dados de clientes
    try:
        with open("clientes.bin", "rb") as arquivo:
            resultado, dados = compacta.descompactar_lista(arquivo)
            if resultado == compacta.CODES["SUCESSO"]:
                cliente.clientes_registrados = dados
            else:
                print(f"Erro ao descompactar clientes: Código {resultado}")
                cliente.carregar_clientes_txt()  # Carrega dados do TXT se o BIN falhar
    except FileNotFoundError:
        print("Arquivo clientes.bin não encontrado. Carregando de clientes.txt...")
        cliente.carregar_clientes_txt()  # Carrega dados do TXT se o BIN não existir

    # Carregar dados de quartos
    try:
        with open("quartos.bin", "rb") as arquivo:
            resultado, dados = compacta.descompactar_lista(arquivo)
            if resultado == compacta.CODES["SUCESSO"]:
                quartos.quartos_disponiveis = dados
            else:
                print(f"Erro ao descompactar quartos: Código {resultado}")
                quartos.carregar_quartos_txt()  # Carrega dados do TXT se o BIN falhar
    except FileNotFoundError:
        print("Arquivo quartos.bin não encontrado. Carregando de quartos.txt...")
        quartos.carregar_quartos_txt()  # Carrega dados do TXT se o BIN não existir

    # Carregar dados de reservas
    try:
        with open("reservas.bin", "rb") as arquivo:
            resultado, dados = compacta.descompactar_lista(arquivo)
            if resultado == compacta.CODES["SUCESSO"]:
                reservas.reservas = dados
            else:
                print(f"Erro ao descompactar reservas: Código {resultado}")
                reservas.carregar_reservas_txt()  # Carrega dados do TXT se o BIN falhar
    except FileNotFoundError:
        print("Arquivo reservas.bin não encontrado. Carregando de reservas.txt...")
        reservas.carregar_reservas_txt()  # Carrega dados do TXT se o BIN não existir

def salvar_dados():
    # Salvar dados em TXT
    cliente.salvar_clientes_txt()
    quartos.salvar_quartos_txt()
    reservas.salvar_reservas_txt()

    # Compactar e salvar dados de clientes em BIN
    try:
        with open("clientes.bin", "wb") as arquivo:
            resultado = compacta.compactar_lista(cliente.clientes_registrados, arquivo)
            if resultado != compacta.CODES["SUCESSO"]:
                print(f"Erro ao compactar clientes: Código {resultado}")
    except Exception as e:
        print(f"Erro ao salvar clientes.bin: {e}")

    # Compactar e salvar dados de quartos em BIN
    try:
        with open("quartos.bin", "wb") as arquivo:
            resultado = compacta.compactar_lista(quartos.quartos_disponiveis, arquivo)
            if resultado != compacta.CODES["SUCESSO"]:
                print(f"Erro ao compactar quartos: Código {resultado}")
    except Exception as e:
        print(f"Erro ao salvar quartos.bin: {e}")

    # Compactar e salvar dados de reservas em BIN
    try:
        with open("reservas.bin", "wb") as arquivo:
            resultado = compacta.compactar_lista(reservas.reservas, arquivo)
            if resultado != compacta.CODES["SUCESSO"]:
                print(f"Erro ao compactar reservas: Código {resultado}")
    except Exception as e:
        print(f"Erro ao salvar reservas.bin: {e}")

def menu_principal():
    """
    Exibe o menu principal para interagir com o sistema.
    Aqui você pode adicionar lógica de interface para o usuário.
    """
    print("Bem-vindo ao Sistema de Hospedagem")
    # Exemplo de um loop de menu básico para interações
    while True:
        print("\nOpções:")
        print("1. Registrar Cliente")
        print("2. Criar Quarto")
        print("3. Realizar Reserva")
        print("4. Exibir Todos os Clientes")
        print("5. Exibir Todos os Quartos")
        print("6. Exibir Todas as Hospedagens")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do Cliente: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            senha = input("Senha: ")
            resultado = cliente.criaCliente(nome, cpf, endereco, telefone, email, senha)
            if resultado == 0:
                print("Cliente registrado com sucesso!")
            else:
                print(f"Erro ao registrar cliente: Código {resultado}")

        elif opcao == "2":
            numero_quarto = int(input("Número do Quarto: "))
            descricao = input("Descrição do Quarto: ")
            preco_diaria = float(input("Preço da Diária: "))
            qt_camas = int(input("Quantidade de Camas: "))
            andar = int(input("Andar: "))
            resultado = quartos.criaQuarto(numero_quarto, descricao, preco_diaria, qt_camas, andar)
            if resultado == 0:
                print("Quarto criado com sucesso!")
            else:
                print(f"Erro ao criar quarto: Código {resultado}")

        elif opcao == "3":
            cpf = input("CPF do Cliente: ")
            data_inicio = input("Data de Início (dd/mm/yyyy): ")
            data_fim = input("Data de Fim (dd/mm/yyyy): ")
            numero_quarto = int(input("Número do Quarto: "))
            resultado = reservas.hospedaCliente(cpf, data_inicio, data_fim, numero_quarto)
            if resultado == 0:
                print("Reserva realizada com sucesso!")
            else:
                print(f"Erro ao realizar reserva: Código {resultado}")

        elif opcao == "4":
            lista_clientes = cliente.exibeTodosClientes()
            print("Clientes Registrados:")
            for c in lista_clientes:
                print(c)

        elif opcao == "5":
            lista_quartos = quartos.exibeTodosQuartos()  # Mudança para lista_quartos
            print("Quartos Cadastrados:")
            for q in lista_quartos:
                print(q)

        elif opcao == "6":
            hospedagens = reservas.exibeTodasHospedagens()
            print("Hospedagens Registradas:")
            print(hospedagens)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

def main():
    # Carregar dados compactados ao iniciar o programa
    carregar_dados()

    # Menu principal
    menu_principal()

    # Salvar dados compactados ao sair do programa
    salvar_dados()

if __name__ == "__main__":
    main()
