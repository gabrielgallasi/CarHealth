def verificar_bateria():
    print("\n=== MEDIÇÃO DA BATERIA ===")

    print("1. Motor desligado")
    print("2. Motor ligado")

    estado_motor = int(input("\nEscolha a opção: "))
    tensao = float(input("Digite a tensão da bateria: "))

    if estado_motor == 1:
        
        if tensao < 12.0:
            print("\nALERTA: bateria com a tensão baixa.")
        
        elif tensao < 12.4:
            print("\nBateria com carga baixa.")
        
        elif tensao <= 12.8:
            print("\nBateria com tensão adequada")
        

        else:
            print("\nTensão acima da faixa esperada com o motor desligado")

    elif estado_motor == 2:

        if tensao < 13.5:
            print("\nALERTA: tensão baixa com o motor ligado.")

        if tensao <= 14.8:
            print("\n Sistema de carga funcionando dentro da faixa esperada")

        else:
            print("\nALERTA: tensão elevada no sistema de carga.")

    else:
        print("\nOpção inválida")

        




