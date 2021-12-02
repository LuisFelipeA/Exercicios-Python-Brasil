# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input("Digite o tamanho do arquivo em MB: "))
internet = float(input("Digite a velocidade da internet em Mbps: "))

segundos = arquivo / internet

minutos_completos = segundos // 60

segundos_restantes = segundos % 60

print(f"Tempo aproximado de download: {minutos_completos:.0f} minutos e {segundos_restantes:.0f} segundos!!")