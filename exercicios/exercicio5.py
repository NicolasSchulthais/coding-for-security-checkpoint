def calcula_desconto(valor):
    if valor <= 100:
        porcentagem = 0
    elif valor <= 300:
        porcentagem = 10
    elif valor <= 500:
        porcentagem = 15
    else:
        porcentagem = 20
        

    desconto = valor * (porcentagem  / 100)
    return desconto, porcentagem


def calculo_vip(valor, VIP):
    if VIP == "sim":
        return valor * 0.05
    return 0


valor = float(input("Digite o valor da compra: R$ "))
vip = input("Cliente VIP? (sim/nao): ").lower()

desconto, porcentagem = calcula_desconto(valor)
desconto_vip = calculo_vip(valor, vip)

desconto_total = desconto + desconto_vip
valor_fim = valor - desconto_total

print("\n=== Resumo da Compra ===")
print(f"Valor original: R$ {valor:.2f}")
print(f"Desconto ({porcentagem}%): R$ {desconto:.2f}")

if desconto_vip > 0:
    print(f"Desconto VIP (5%): R$ {desconto_vip:.2f}")

print(f"Valor final: R$ {valor_fim:.2f}")
