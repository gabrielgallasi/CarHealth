from banco.conexao import conectar

def analisar_pressao(pressao_atual, pressao_recomendada):


    if pressao_atual < pressao_recomendada - 2:
        return "PRESSÃO BAIXA"

    elif pressao_atual > pressao_recomendada + 2:
        return "PRESSÃO ALTA"

    else:
        return "PRESSÃO ADEQUADA"


def verificar_pneus():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, modelo, ano, placa,
               pressao_dianteira, pressao_traseira
        FROM veiculos
    """)

    veiculos = cursor.fetchall()

    if len(veiculos) == 0:
        print("\nNenhum veículo cadastrado.")
        conexao.close()
        return

    print("\n=== VEÍCULOS CADASTRADOS ===")

    for veiculo in veiculos:
        print(
            f"ID: {veiculo[0]} | "
            f"{veiculo[1]} {veiculo[2]} | "
            f"Placa: {veiculo[3]}"
        )

    id_veiculo = int(
        input("\nDigite o ID do veículo que deseja analisar: ")
    )

    cursor.execute("""
        SELECT modelo, ano,
               pressao_dianteira, pressao_traseira
        FROM veiculos
        WHERE id = ?
    """, (id_veiculo,))

    veiculo = cursor.fetchone()

    conexao.close()

    if veiculo is None:
        print("\nVeículo não encontrado.")
        return

    modelo = veiculo[0]
    ano = veiculo[1]
    pressao_dianteira = veiculo[2]
    pressao_traseira = veiculo[3]

    if pressao_dianteira is None or pressao_traseira is None:
        print("\nEste veículo não possui pressão recomendada cadastrada.")
        return 


    conexao.close()

    if veiculo is None:
        print("\nVeículo não encontrado.")
        return

    if pressao_dianteira is None or pressao_traseira is None:
        print("\nEste veículo não possui pressão recomendada cadastrada.")
        return

    print(f"\n=== ANÁLISE DOS PNEUS - {modelo} {ano} ===")

    print(
        f"Pressão recomendada dianteira: "
        f"{pressao_dianteira} PSI")

    print(
        f"Pressão recomendada traseira: "
        f"{pressao_traseira} PSI")

    dianteiro_esquerdo = float(
        input("\nPressão do pneu dianteiro esquerdo: "))

    dianteiro_direito = float(
        input("Pressão do pneu dianteiro direito: "))

    traseiro_esquerdo = float(
        input("Pressão do pneu traseiro esquerdo: "))

    traseiro_direito = float(
        input("Pressão do pneu traseiro direito: "))

    print("\n=== RESULTADO ===")

    print(
        f"Dianteiro esquerdo: {dianteiro_esquerdo} PSI - "
        f"{analisar_pressao(dianteiro_esquerdo, pressao_dianteira)}"
    )

    print(
        f"Dianteiro direito: {dianteiro_direito} PSI - "
        f"{analisar_pressao(dianteiro_direito, pressao_dianteira)}"
    )

    print(
        f"Traseiro esquerdo: {traseiro_esquerdo} PSI - "
        f"{analisar_pressao(traseiro_esquerdo, pressao_traseira)}"
    )

    print(
        f"Traseiro direito: {traseiro_direito} PSI - "
        f"{analisar_pressao(traseiro_direito, pressao_traseira)}"
    )