# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    # Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    # Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = float(input("""Saque caixa eletronico:
    Valor minimo R$10
    Valor Maximo R$600 
Digite o valor de saque: """))

if valor <= 600 and valor >= 10:
    notas_cem = valor//100
    resto_cem = valor%100
    notas_cinquenta = resto_cem//50
    resto_cinquenta = resto_cem%50
    notas_dez = resto_cinquenta//10
    resto_dez = resto_cinquenta%10
    notas_cinco = resto_dez//5
    notas_um = resto_dez%5
    
    if valor < 100:
        if valor < 10:
            print(f"Para sacar {valor:.2f} reais, o programa fornece {notas_cinco:.0f} notas de cinco e {notas_um:.0f} de notas de um")

        else:
            print(f"Para sacar {valor:.2f} reais, o programa fornece {notas_dez:.0f} notas de dez, {notas_cinco:.0f} notas de cinco e {notas_um:.0f} de notas de um")
    
    else:
        print(f"Para sacar {valor:.2f} reais, o programa fornece {notas_cem:.0f} notas de 100, {notas_cinquenta:.0f} notas de 50, {notas_dez:.0f} notas de dez, {notas_cinco:.0f} notas de cinco e {notas_um:.0f} de notas de um")

else:
    print("Valor invalido")