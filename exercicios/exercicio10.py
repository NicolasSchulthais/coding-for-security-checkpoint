def calcular_inss(salario):
    salario = min(salario, 8157.41)
    inss = 0

    faixa1 = min(salario, 1518.00)
    inss += round(faixa1 * 0.075, 2)

    if salario > 1518.00:
        faixa2 = min(salario, 2793.88) - 1518.00
        inss += round(faixa2 * 0.09, 2)

    if salario > 2793.88:
        faixa3 = min(salario, 4190.83) - 2793.88
        inss += round(faixa3 * 0.12, 2)

    if salario > 4190.83:
        faixa4 = min(salario, 8157.41) - 4190.83
        inss += round(faixa4 * 0.14, 2)

    return round(inss, 2)


def calcular_ir(base):
    ir = 0

    faixa1 = max(0, min(base, 2826.65) - 2259.20)
    ir += round(faixa1 * 0.075, 2)

    faixa2 = max(0, min(base, 3751.05) - 2826.65)
    ir += round(faixa2 * 0.15, 2)

    faixa3 = max(0, min(base, 4664.68) - 3751.05)
    ir += round(faixa3 * 0.225, 2)

    if base > 4664.68:
        faixa4 = base - 4664.68
        ir += round(faixa4 * 0.275, 2)

    return round(ir, 2)



salario = float(input("Salário bruto: R$ "))
dependentes = int(input("Número de dependentes: "))
pensao = float(input("Valor da pensão: R$ "))
idoso = input("Tem 65 anos ou mais? (s/n): ").lower()


inss = calcular_inss(salario)


desc_dependentes = dependentes * 189.59
desc_idoso = 1903.98 if idoso == "s" else 0


base_ir = salario - inss - desc_dependentes - pensao - desc_idoso

if base_ir < 0:
    base_ir = 0


ir = calcular_ir(base_ir)


salario_liquido = salario - inss - ir



print("\n====================================")
print("CONTRACHEQUE — Cálculo de IR Mensal")
print("====================================")
print(f"Salário bruto:       R$ {salario:.2f}\n")

print(f"(-) INSS:            R$ {inss:.2f}")
print(f"(-) Dependentes:     R$ {desc_dependentes:.2f}")
print(f"(-) Pensão:          R$ {pensao:.2f}")
print(f"(-) Isenção 65+:     R$ {desc_idoso:.2f}\n")

print(f"Base de cálculo IR:  R$ {base_ir:.2f}\n")

print(f"(-) IR:              R$ {ir:.2f}\n")

print("====================================")
print(f"Salário líquido:     R$ {salario_liquido:.2f}")
print("====================================")