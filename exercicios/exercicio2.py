def IMC(altura: int, peso: int):
    
    imc = peso / (altura * altura)
    
    if imc <= 18.5:
        return "Abaixo do peso"
    elif imc <= 24.9:
        return "Peso normal"
    elif imc <= 29.9:
        return "Acima do peso"
    else:
        return "Sobrepeso"
    

altura = float(input("Qual a sua altura?"))
peso = float(input("Qual o seu peso?"))

resultado = IMC(altura, peso) 

print(resultado)
