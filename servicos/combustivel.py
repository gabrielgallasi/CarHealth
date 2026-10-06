def calcular_consumo():
    distancia = float(input("\nQuantos KM foram percorridos ?:"))
    
    combustivel_gasto = float(input("\nQuanto de combustivel foi gasto(Litros):"))

    preco_litro = float(input("\nQuanto custou o litro do combustivel: "))
    
    consumo = distancia / combustivel_gasto

    custo_viagem = combustivel_gasto * preco_litro

    print(f"\nO consumo do carro foi de {consumo:.2f} km/L")
    print(f"\nO custo de combustível da viagem foi de R$ {custo_viagem:.2f}")