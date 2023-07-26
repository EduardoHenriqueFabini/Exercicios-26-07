def imprimir_tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    numero_informado = int(input("Digite um número para ver a sua tabuada de 1 a 10: \n"))
    imprimir_tabuada(numero_informado)
except ValueError:
    print("Por favor, digite um número válido.")