import random

def lancar_dados():
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    
    return dado_1 + dado_2

resultado = lancar_dados()
print(f'O resultado do lançamento dos dados é: {resultado}')