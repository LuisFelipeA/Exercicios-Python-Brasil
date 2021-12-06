# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações.

valor_hora = float(input("Digite o valor da hora: "))
qtd_hora = int(input("Digite a quantidade de hora: "))

salario_bruto = valor_hora*qtd_hora
sindicato = salario_bruto*0.03
fgts = salario_bruto*0.11


if salario_bruto < 900 and salario_bruto > 0:
    print(f"""  Salario Bruto: R$ {salario_bruto:.2f}
    (-) Imposto de renda: R$0,00
    (-) sindicato: R${sindicato:.2f}
    FGTS: R${fgts:.2f}
    Total desconto: R${sindicato:.2f}
    Salario Liquido: R${(salario_bruto-sindicato):.2f}""")

elif salario_bruto >= 900 and salario_bruto < 1500:
    ir = salario_bruto*0.05
    print(f"""  Salario Bruto: R$ {salario_bruto:.2f}
    (-) Imposto de renda: R${ir:.2f}
    (-) sindicato: R${sindicato:.2f}
    FGTS: R${fgts:.2f}
    Total desconto: R${sindicato:.2f}
    Salario Liquido: R${(salario_bruto-sindicato-ir):.2f}""")

elif salario_bruto >=1500 and salario_bruto < 2500:    
    ir = salario_bruto*0.1
    print(f"""  Salario Bruto: R$ {salario_bruto:.2f}
    (-) Imposto de renda: R${ir:.2f}
    (-) sindicato: R${sindicato:.2f}
    FGTS: R${fgts:.2f}
    Total desconto: R${sindicato:.2f}
    Salario Liquido: R${(salario_bruto-sindicato-ir):.2f}""")

elif salario_bruto >= 2500:    
    ir = salario_bruto*0.2
    print(f"""  Salario Bruto: R$ {salario_bruto:.2f}
    (-) Imposto de renda: R${ir:.2f}
    (-) sindicato: R${sindicato:.2f}
    FGTS: R${fgts:.2f}
    Total desconto: R${sindicato:.2f}
    Salario Liquido: R${(salario_bruto-sindicato-ir):.2f}""")

else:
    print("Valor invalido")