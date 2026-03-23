def verificador_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def verificador_mes(mes, ano):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    elif mes in [4, 6, 9, 11]:
        return 30

    elif mes == 2:
        if verificador_bissexto(ano):
            return 29
        else:
            return 28
    else:
        return None

def validar_data(dia, mes, ano):

    print(f'Data: {dia:02d}/{mes:02d}/{ano:02d}')

    if verificador_bissexto(ano):
        print("Ano bissexto: Sim.")
    else: 
        print("Ano bissexto: Não.")

    if mes < 1 or mes > 12:
        print("Esse mês não existe.")
        return

    dias = verificador_mes(mes, ano)

    if dia < 1:
        print("Esse dia não existe.")
        return

    if dia > dias:
        print(f'data invalida, esse mês possui apenas {dias} dias')
        return
        
    print("data Válida!")
    
        

dia = int(input("Digite o dia:"))
mes = int(input("Digite o mês:"))
ano = int(input("Digite o ano:"))

validar_data(dia, mes, ano)