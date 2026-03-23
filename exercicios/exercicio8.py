def calcular_horas(entrada, saida):
    if saida >= entrada:
        horas = saida - entrada
    else:
        horas = (24 - entrada) + saida

    if horas == 0:
        horas = 1

    return horas


def calcular_valor(horas):
    if horas == 1:
        return 10
    else:
        return 10 + (horas - 1) * 5


def verificar_add_noturno(entrada, saida):
    if entrada >= 22 or saida <= 6 or entrada > saida:
        return True
    return False


def calcular_desconto(total, placa, dia):
    if dia == "segunda" and placa % 2 == 0:
        return total * 0.1
    return 0


entrada = int(input("Hora de entrada: "))
saida = int(input("Hora de saída: "))
placa = int(input("Último número da placa: "))
dia = input("Dia da semana: ")

horas = calcular_horas(entrada, saida)
valor = calcular_valor(horas)

noturno = verificar_add_noturno(entrada, saida)

if noturno:
    adicional = valor * 0.5
else:
    adicional = 0

total = valor + adicional

desconto = calcular_desconto(total, placa, dia)

total_final = total - desconto

print("\n=== Estacionamento ===")
print("Entrada:", entrada, "Saída:", saida)
print("Tempo:", horas, "horas")
print("Valor base: R$", valor)

if adicional > 0:
    print("Adicional noturno: R$", adicional)

if desconto > 0:
    print("Desconto: R$", desconto)

print("Total a pagar: R$", total_final)