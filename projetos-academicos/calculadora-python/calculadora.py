def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

print("Calculadora simples")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha uma opção (1-4): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado:", somar(num1, num2))
elif opcao == '2':
    print("Resultado:", subtrair(num1, num2))
elif opcao == '3':
    print("Resultado:", multiplicar(num1, num2))
elif opcao == '4':
    print("Resultado:", dividir(num1, num2))
else:
    print("Opção inválida.")
