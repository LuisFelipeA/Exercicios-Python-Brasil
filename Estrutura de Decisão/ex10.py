#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

nome = input("Digite seu nome: ")
turno = input("Digite o turno que voce estuda: 'M' para matutino , 'V' para Vespertino ou 'N' para Noturno: ").upper()

if turno == "M":
    print(f"Bom dia, {nome}")
    
elif turno == "V":
    print(f"Boa tarde, {nome}")

elif turno == "N":
    print(f"Boa Noite, {nome}")

else:
    print("Valor Invalido")