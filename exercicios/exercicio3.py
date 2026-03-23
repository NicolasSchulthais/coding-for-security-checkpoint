dolar = 5.15
euro = 5.55
libra = 6.45



def real_Dolar(real):
    return real / dolar

def real_Euro(real):
    return real / euro


def real_Libra(real):
    return real / libra
    

conversor = input("[1] Real → Dólar\n[2] Real → Euro\n[3] Real → Libra\nEscolha o Tipo da conversão:")


while conversor not in["1","2","3"]:
    print("Opção inválida!")
    conversor = input("Escolha somente entre: [1] [2] [3]")
    
while True:
        real = float(input("Qual o Valor em real?"))
        if real >= 0:
            break
        print("Digite apenas numeros positivos")


if conversor == "1":
    print(f'R$ {real:.2f} = US$ {real_Dolar(real):.2f}')

elif conversor == "2":
    print(f'R$ {real:.2f} = € {real_Euro(real):.2f}')
    
elif conversor == "3":
    print(f'R$ {real:.2f} = £ {real_Libra(real):.2f}')
