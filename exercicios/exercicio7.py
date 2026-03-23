def valida_valor(valor):
    if valor <= 0:
        return False
    if valor % 10 != 0:
        return False
    return True


def calcular_cedulas(valor):
    notas = [200, 100, 50, 20, 10]
    resultado = {}

    for cedula in notas:
        quantidade = valor // cedula
        resultado[cedula] = quantidade
        valor = valor % cedula

    return resultado


valor = int(input("Digite o valor do saque: R$ "))

if not valida_valor(valor):
    print("Valor inválido")
else:
    cedulas = calcular_cedulas(valor)

    print(f"\n=== Saque: R$ {valor} ===")

    total_cedulas = 0

    for cedula, quantidade in cedulas.items():
        print(f"R$ {cedula}: {quantidade} cédula(s)")
        total_cedulas += quantidade

    print(f"Total de cédulas: {total_cedulas}")