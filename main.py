def calculadora ():
    #loop com try e except para validar se é um número
    while True:
        try:
            num1 = int(input('informe o primeiro número: '))
            num2 = int(input('informe o segundo número: '))
            break
        except ValueError:
            print('erro ao ler o número, digite novamente;')

    op = str(input('qual o tipo de operação? (+, - , * , / )'))

    #casos de if e elif para decidir qual operação será feita
    if op == '+':
        #adicao
        soma = num1+num2
        print(f"{num1} + {num2} = {soma}")

    elif op == '-':
        #subtraçao
        subt = num1-num2
        print(f"{num1} - {num2} = {subt}")

    elif op == '*':
        #multiplicaçao
        mult = num1*num2
        print(f"{num1} * {num2} = {mult}")

    elif op == '/':
        #verificador se denominador for 0, caso inválido
        if num2 == 0:
            print('não é possivel dividir por 0')
        else:
            #divisao
            div = num1/num2
            print(f"{num1} / {num2} = {div}")
    else:
        #caso o operador seja diferente dos apresentados, encerra a operação
        print('falha ao ler operador, tente novamente.')

    #input para rodar a funçao de novo ou encerrar
    dnv = input('voce quer realizar outro calculo? (s/n)')
    if dnv == 's':
        calculadora()
    else :
        print('obrigado por usar')
#chama a função
calculadora()