def imprimir_tabuada(numero):
    for i in range(tamanho_tabuada1, tamanho_tabuada2+1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    tamanho_tabuada1 = int(input("Digite até aonde deseja que sua tabuada começe\n"))
    tamanho_tabuada2 = int(input("Digite até aonde deseja que sua tabuada termine\n"))
    numero_informado = int(input("Digite um número para ver a sua tabuada \n"))
    imprimir_tabuada(numero_informado)
except ValueError:
    print("Por favor, digite um número válido.")