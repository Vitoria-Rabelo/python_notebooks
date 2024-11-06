print("\n******************* Calculadora em Python *******************");

print("selecione a operacao desejada:\n");
print("1 - Soma\n");
print("2 - Subtração\n");
print("3 - Multiplicação\n");
print("4 - Divisão\n");

op = int(input());
if(op == 1): 
    print("Digite o primeiro número: ");
    num1 = float(input());
    print("Digite o segundo número: ");
    num2 = float(input());
    resultado = num1 + num2;
    print("Resultado da Soma: ");
    print(resultado);

elif(op == 2):
    print("Digite o primeiro número: ");
    num1 = float(input());
    print("Digite o segundo número: ");
    num2 = float(input());
    resultado = num1 - num2;
    print("Resultado da Subtração: ");
    print(resultado);

elif(op == 3):
    print("Digite o primeiro número: ");
    num1 = float(input());
    print("Digite o segundo número: ");
    num2 = float(input());
    resultado = num1 * num2;
    print("Resultado da Multiplicação: ");
    print(resultado);

elif(op == 4):
    print("Digite o primeiro número: ");
    num1 = float(input());
    print("Digite o segundo número: ");
    num2 = float(input());
    resultado = num1 / num2;
    print("Resultado da Divisão: ");
    print(resultado);

else:
    print("Você digitou algo inválido, tente novamente\n");
