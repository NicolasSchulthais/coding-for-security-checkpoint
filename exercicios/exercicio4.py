def validadndo_triangulo(A, B, C):
    if A <= 0 or B <= 0 or C <= 0:
        return False

    if A + B > C and A + C > B and B + C > A:
        return True
    
    return False

def classificador_triangulo(A, B, C):
    if A == B == C:
        return "Equilátero"
    elif A == B or A == C or B == C:
        return "Isósceles"
    else:
        return "Escaleno"
    
    

A = float(input("Qual o Valor do primeiro lado? "))
B = float(input("Qual o Valor do segundo lado? "))
C = float(input("Qual o Valor do terceiro lado? "))

if validadndo_triangulo(A, B, C):
    Validacao = classificador_triangulo(A, B, C)
    print(f'Os lados são: {A}, {B}, {C}')
    print(f'Seu triangulo é: {Validacao}')
else:
    print(f'Os lados do seu triângulo são: {A}, {B}, {C}')
    print(f'Infelizmente seu forma é tudo menos um triangulo')