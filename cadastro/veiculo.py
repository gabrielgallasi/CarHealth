from banco.conexao import conectar


def cadastrar_veiculo():
    print("\n=== CADASTRO DE VEÍCULO ===")

    modelo = input("Digite o modelo do veículo: ")
    ano = int(input("Digite o ano do veículo: "))
    placa = input("Digite a placa do veículo: ").upper()
    
    pressao_dianteira = float(input("Digite a pressão recomendada dos pneus dianteiros(PSI): "))
    
    pressao_traseira = float(input("Digite a pressão recomendada dos pneus traseiros(PSI): "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO veiculos (modelo, ano, placa, pressao_dianteira, pressao_traseira)
        VALUES (?, ?, ?, ?, ?)
    """, (modelo, ano, placa, pressao_dianteira, pressao_traseira))

    conexao.commit()
    conexao.close()

    print("\nVeículo cadastrado com sucesso!")


def listar_veiculos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, modelo, ano, placa, pressao_dianteira, pressao_traseira
        FROM veiculos
    """)

    veiculos = cursor.fetchall()

    conexao.close()

    print("\n=== VEÍCULOS CADASTRADOS ===")

    if len(veiculos) == 0:
        print("Nenhum veículo cadastrado.")
        return

    for veiculo in veiculos:
        print(
        f"ID: {veiculo[0]} | "
        f"Modelo: {veiculo[1]} | "
        f"Ano: {veiculo[2]} | "
        f"Placa: {veiculo[3]} | "
        f"Dianteiros: {veiculo[4]} PSI | "
        f"Traseiros: {veiculo[5]} PSI | ")

def excluir_veiculo():
    conexao = conectar()
    cursor = conexao.cursor()

    id_veiculo = int(input("Digite o ID do veículo que deseja excluir: "))

    cursor.execute("""
        DELETE FROM veiculos
        WHERE id = ?
    """, (id_veiculo,))

    conexao.commit()
    conexao.close()

    print("Veículo excluído com sucesso!")

def excluir_todos_veiculos():
    confirmacao = input(
        "Tem certeza que deseja excluir TODOS os veículos? (s/n): "
    ).lower()

    if confirmacao != "s":
        print("Operação cancelada.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM veiculos")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='veiculos'")

    conexao.commit()
    conexao.close()

    print("Todos os veículos foram excluídos!")



    