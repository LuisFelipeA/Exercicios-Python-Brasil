# #https://wiki.python.org.br/EstruturaSequencial

#1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Hello World")

#2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
n = float(input("Digite um numero: "))
print(f"O numero informado foi {n}")

#3 Faça um Programa que peça dois números e imprima a soma.
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
soma = n1 + n2
print(f"A soma entre os dois numeros informados é {soma}")

#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
soma_nota = 0
contador = 0
qtd_nota = 1
while contador <4:
    nota = float(input(f"Digite a nota {qtd_nota}: "))
    soma_nota = soma_nota + nota
    contador += 1
    qtd_nota += 1 

media = soma_nota/contador
print(f"A média das notas é {media:.2f}")

#5 Faça um Programa que converta metros para centímetros.

m = float(input("Digite a medida em Metros: "))
cm = m*100
print(f"{m} metros equivalem a {cm} centimetros. ")

#6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("Digite o raio do circulo: "))
area = 3.14159265359*raio**2
print(f"A area do circulo é {area}")

#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite a medida de um dos lados (em centimetros): "))
area = lado**2
print(f"A area do quadrado é {area}cm e o dobro desta area é {area*2}cm ")


#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Digite quanto voce ganha por hora: "))
horas_trabalhadas = float(input("Digite quantas horas voce trabalhou este mes: "))
salario = horas_trabalhadas*ganho_hora
print(f"O salario desse mes foi R${salario:.2f}")

#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
f = float(input("Digite a temperatura em graus Fahrenheit: "))
c = 5 * ((f-32) / 9)
print(f"A temperatura de {f}° Fahrenheit equivalem a {c:.1f}° Celsius.")

#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# f = c * 9/5 + 32
c = float(input("Digite a temperatura em graus Celsius: "))
f = c * 9/5 + 32
print(f"A temperatura de {c}° Celsius equivalem a {f}° Fahrenheit.")