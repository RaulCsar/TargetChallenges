def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

Ninformado = int(input("Digite um número: "))

if fibonacci(Ninformado):
    print("O número informado pertence à sequência de Fibonacci.")
else:
    print("O número informado NÃO pertence à sequência de Fibonacci.")