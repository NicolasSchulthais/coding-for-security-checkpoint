def defidor_de_idade(idade_em_anos: int, idade_em_meses: int = 0):
     
    if idade_em_meses < 0 or idade_em_meses >= 12:
        return "Mês inválido"
    if idade_em_anos < 0 or idade_em_anos > 120:
        return "Idade inválida"
    elif idade_em_anos < 15 or (idade_em_anos == 15 and idade_em_meses == 0):
        return "Criança"
    elif idade_em_anos < 25 or (idade_em_anos == 25 and idade_em_meses == 0):
        return "Adolescente"
    elif idade_em_anos < 70 or (idade_em_anos == 70 and idade_em_meses == 0):
        return "Adulto"
    else:
        return "Idoso"
 
 
idade_em_anos = int(input("qual a idade em anos?"))
idade_em_meses = int(input("qual a idade em meses?"))


resultado = defidor_de_idade(idade_em_anos, idade_em_meses)

print(resultado)