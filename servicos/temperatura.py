def verificar_temperatura():
    print("\n=== TEMPERATURA DO MOTOR ===")

    temperatura = float(input("Digite a temperatura do motor em °C: "))

    if temperatura < 70:
        print("\nMotor ainda está frio")

    elif temperatura <= 100:
        print("\nTemperatura dentro da faixa definida como normal.")

    else:
        print("\nMotor com Temperatura elevada!")

