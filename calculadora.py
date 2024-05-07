# Importando bibliotecas
from rich.console import Console # Adicionando a função de console da biblioteca
console = Console()

# Função de conversão
def binary_to_decimal(binary_num:str): # Converte números binários em decimais
    decimal_num = int(binary_num, 2)
    return decimal_num

# Funções de cálculo
def binary_addition(bin1, bin2, length): # Adição
    # Declara as váriaveis relacionadas a quantia de bits
    length = int(float(length))
    original_length = length

    # Verifica se a quantidade de bits é menor ou igual a 0
    if length <= 0:
        raise ValueError("[ A quantidade de bits não pode ser menor que 1 bit! ]")

    # Verifica se todos os números são compostos de apenas zeros 
    if all(bit == '0' for bit in bin1) and all(bit == '0' for bit in bin2):
        return '0' * length

    # Verifica se o primeiro número é composto de apenas zeros
    if all(bit == '0' for bit in bin1):
        return bin2.zfill(length)

    # Verifica se o segundo número é composto de apenas zeros
    if all(bit == '0' for bit in bin2):
        return bin1.zfill(length)

    # Remove zeros à esquerda
    bin1 = bin1.lstrip('0')
    bin2 = bin2.lstrip('0')

    # Preenche os números binários com zeros a esquerda com base na quantia de bits definida
    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)

    # Declarando váriaveis de cálculo
    result = ''
    carry = 0

    # Itera os binários da direita para a esquerda
    for i in range(length - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])

        # Calcule a soma dos bits atuais junto com o "empréstimo"
        current_sum = bit1 + bit2 + carry

        # Anexa o resultado ao início do resultado anterior
        result = str(current_sum % 2) + result

        # Atualiza o "empréstimo" para a próxima iteração
        carry = current_sum // 2

    # Se sobrar um "empréstimo" após a iteração, anexe-o ao resultado
    if carry:
        result = '1' + result

    length = original_length # Re difinindo a quantia de bits

    # Verifique se o resultado excede a quantia de bits
    if len(result) > length:
        raise ValueError(f'[ O resultado excede {original_length} bits! ]')

    # Retorna o resultado e preenche com zeros à esquerda com base na quantia de bits definida
    return result.zfill(length)

def binary_subtraction(bin1, bin2, length): # Subtração
    # Declara as váriaveis relacionadas a quantia de bits
    length = int(float(length))
    original_length = length

    # Verifica se a quantidade de bits é menor ou igual a 0
    if length <= 0:
        raise ValueError("[ The length cannot be less than 1 bit! ]")

    # Verifica se todos os números são compostos de apenas zeros 
    if all(bit == '0' for bit in bin1) and all(bit == '0' for bit in bin2):
        return '0' * length

    # Converte números binários em inteiros para comparação
    int_bin1 = int(bin1, 2)
    int_bin2 = int(bin2, 2)
    
    # Verifica se o segundo número binário é maior que o primeiro
    if int_bin2 > int_bin1:
        raise ValueError('[ Resultado negativo! ]')

    # Verifica se o segundo número é composto de apenas zeros
    if all(bit == '0' for bit in bin2):
        return bin1.zfill(length)
    
    # Preenche os números binários com zeros a esquerda com base na quantia de bits definida
    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)
    
    # Declarando váriaveis de cálculo
    result = ''
    borrow = 0
    
    # Itera os binários da direita para a esquerda
    for i in range(length - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        
        # Subtrai os bits atuais junto com o "empréstimo"
        current_diff = bit1 - bit2 - borrow
        
        # Se a diferença for negativa, pegue "emprestado" do próximo bit de ordem superior
        if current_diff < 0:
            current_diff += 2
            borrow = 1
        else:
            borrow = 0
        
        # Anexa o resultado ao início do resultado anterior
        result = str(current_diff) + result
    
    length = original_length # Re difinindo a quantia de bits

    # Retorna o resultado e preenche com zeros à esquerda com base na quantia de bits definida
    return result.zfill(length)

def binary_multiplication(bin1, bin2, length): # Multiplicação
    # Declara as váriaveis relacionadas a quantia de bits
    length = int(float(length))
    original_length = length

    # Verifica se a quantidade de bits é menor ou igual a 0
    if length <= 0:
        raise ValueError("[ A quantidade de bits não pode ser menor que 1 bit! ]")

    # Função básica de adição binária
    def binary_add(a, b):
        result = []
        carry = 0
        for i in range(max(len(a), len(b))):
            bit_a = int(a[-1 - i]) if i < len(a) else 0
            bit_b = int(b[-1 - i]) if i < len(b) else 0
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])

    # Verifica se todos os números são compostos de apenas zeros 
    if all(bit == '0' for bit in bin1) and all(bit == '0' for bit in bin2):
        return '0' * length

    # Remove zeros à esquerda
    bin1 = bin1.lstrip('0')
    bin2 = bin2.lstrip('0')

    # Se depois de remover os zeros à esquerda, alguma das entradas estiver vazia, retorne "0"
    if not bin1 or not bin2:
        return '0' * length

    # Multiplique cada bit de bin1 por bin2 inteiro e mude o resultado
    result = "0"
    for i in range(len(bin1)):
        if bin1[-1 - i] == "1":
            temp = bin2 + "0" * i
            result = binary_add(result, temp)

    length = original_length # Re difinindo a quantia de bits

    # Verifique se o resultado excede a quantia de bits
    if len(result) > length:
        raise ValueError(f'[ O resultado excede {original_length} bits! ]')
    
    # Retorna o resultado e preenche com zeros à esquerda com base na quantia de bits definida
    return result.zfill(length)

# Função de cálculo com base na escolha do usuário
def binary_calculation_BA(first_b_num:str, second_b_num:str, choice, length):
    match choice:
        case 1: # Adição
            try:
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Decimal ]: [purple]{binary_to_decimal(first_b_num)}[/][/] + [purple]{binary_to_decimal(second_b_num)}[/] = [purple]{binary_to_decimal(binary_addition(first_b_num, second_b_num, length))}[/][/]')
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Binário ]: [green]{first_b_num}[/][/] + [green]{second_b_num}[/] = [green]{binary_addition(first_b_num, second_b_num, length)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| 😕 ERRO -> [orange1][underline]{e}[/][/][/]\n')
        case 2: # Subtração
            try:
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Decimal ]: [purple]{binary_to_decimal(first_b_num)}[/][/] - [purple]{binary_to_decimal(second_b_num)}[/] = [purple]{binary_to_decimal(binary_subtraction(first_b_num, second_b_num, length))}[/][/]')
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Binário ]: [green]{first_b_num}[/][/] - [green]{second_b_num}[/] = [green]{binary_subtraction(first_b_num, second_b_num, length)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| 😕 ERRO -> [orange1][underline]{e}[/][/][/]\n')
        case 3: # Multiplicação
            try:
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Decimal ]: [purple]{binary_to_decimal(first_b_num)}[/][/] * [purple]{binary_to_decimal(second_b_num)}[/] = [purple]{binary_to_decimal(binary_multiplication(first_b_num, second_b_num, length))}[/][/]')
                console.print(f'\n[bold][orange1][cyan]| 😎 [ Resultado Binário ]: [green]{first_b_num}[/][/] * [green]{second_b_num}[/] = [green]{binary_multiplication(first_b_num, second_b_num, length)}[/][/]\n')
            except ValueError as e:
                console.print(f'\n[bold][red]| 😕 ERRO -> [orange1][underline]{e}[/][/][/]\n')

# Funções
def bit_length_check(length): # Verifica a quantidade de bits escolhida
    if not length or length == " " :
        return True

    if not length.replace('.', '', 1).isdigit():
        return True

    length = int(float(length))
    
    if length == 0 or length <= 0:
        return True
    else:    
        return False

def multiple_choice_logic(choice): # Verifica a opção de multipla escolha feita pelo usuário
    if choice != '1' and choice != '2' and choice != '3':
        return True
    else:
        return False

def multiple_choice_YN(choice): # Verifica a opção de escolha sim/não feita pelo usuário
    if choice != 'S' and choice != 'N':
        return True
    else:
        return False
    
def is_binary(input_str): # Verifica se os números digitados pelo usuário são válidos
    if input_str == "" or input_str == " ":
        return False
        
    for char in input_str:
        if char not in '01':
            return False
    return True

# Importando scripts
import scripts.calc_functions  as CF # Funções de cálculo
import scripts.basic_functions as BF # Funções basicas

# Importando bibliotecas
from rich.console import Console # Adicionando a função de console da biblioteca
console = Console()

from rich.traceback import install # Adicionando uma melhor menssagem de erro pela biblioteca
install()

from rich.markdown import Markdown # Adicionando suporte a Markdown pela biblioteca

# Construindo título e rodapé do programa usando Markdown
title = '# 🔥 CALCULADORA BINÁRIA 🔥'
mdtitle = Markdown(title)

footer = '# 🔥 FIM DO PROGRAMA 🔥'
mdfooter = Markdown(footer)

# Função principal
def app():
    # Opção de definição de quantidade de bits pelo usuário
    console.print(f'\n[bold][cyan]| 🤓 Quantos bits você deseja usar para o cálculo? [italic][orange1](O valor padrão é 8 bits)[/][/][/]')
    bit_length = console.input((f'\n[bold][cyan]| : [/][/]'))

    bit_length = bit_length if bit_length else "8"
    bit_lenght_logic_value = BF.bit_length_check(bit_length)

    if bit_lenght_logic_value: # Valida se a quantidade de bits escolhida
        while bit_lenght_logic_value:
            console.print(f'\n[bold][red]| 😕 [underline]Quantidade de bits inválida! Por favor, digite outro valor.[/][/][/]')
            bit_length = console.input((f'\n[bold][cyan]| : [/][/]'))

            bit_length = bit_length if bit_length else "8"
            bit_lenght_logic_value = BF.bit_length_check(bit_length)

    # Opção de multipla escolha entre os tipos de cálculos
    console.print(f'\n[bold][cyan]| 🤓 Qual o tipo de cálculo você deseja? [italic][orange1](Digite o número correspondente a opção desejada)[/][/][/]')
    choice = console.input((f'\n[bold][cyan][orange1]| 1. Adição\n| 2. Subtração\n| 3. Multiplicação\n\n[/]| : [/][/]'))

    mult_ch_logic_value = BF.multiple_choice_logic(choice)

    if mult_ch_logic_value: # Valida a opção de escolha do usuário
        while mult_ch_logic_value:
            console.print(f'\n[bold][red]| 😕 [underline]Escolha inválida! Por favor, tente novamente.[/][/][/]')
            choice = console.input((f'\n[bold][cyan][orange1]| 1. Adição\n| 2. Subtração\n| 3. Multiplicação\n\n[/]| : [/][/]'))
            mult_ch_logic_value = BF.multiple_choice_logic(choice)

    choice = int(choice)
    msg = ['Adição', 'Subtração', 'Multiplicação'] # Mensagem da opção escolhida

    console.print(f'\n[bold][orange1]| [ {msg[choice - 1]} ][/][/]') # Escolha da mensagem com base na escolha do usuário

    # Lendo os números obtidos pelo usuário
    first_num = console.input(f'\n[bold][cyan]| Digite o primeiro número: [/][/]')
    second_num = console.input(f'\n[bold][cyan]| Digite o segundo número: [/][/]')

    # Verifica se os números são válidos
    if not BF.is_binary(first_num) or not BF.is_binary(second_num):
        while not BF.is_binary(first_num) or not BF.is_binary(second_num):
            console.print(f'\n[bold][red]| 😕 [underline]Número inválido! Por favor, digite outro número.[/][/][/]')
            first_num = console.input(f'\n[bold][cyan]| Digite o primeiro número: [/][/]')
            second_num = console.input(f'\n[bold][cyan]| Digite o segundo número: [/][/]')

    # Lógica de escolha do tipo de cálculo
    match choice:
        case 1:
            CF.binary_calculation_BA(first_num, second_num, 1, bit_length)
        case 2:
            CF.binary_calculation_BA(first_num, second_num, 2, bit_length)
        case 3:
            CF.binary_calculation_BA(first_num, second_num, 3, bit_length)

# Início do programa
if _name_ == "_main_":
    # Título do programa
    console.print(mdtitle, '\n')

    choice = "S" # Declarando variável de escolha
    
    while choice == "S": # Laço de repetição do programa
        app()

        choice = console.input(f"[bold][cyan]| 🤔 Gostaria de realizar outro cálculo? [italic][orange1](S/N)\n\n[/][/]| : ").upper()
        controller = BF.multiple_choice_YN(choice)

        if controller: # Valida se a opção escolhida pelo usuário
            while controller:
                console.print(f'\n[bold][red]| 😕 [underline]Escolha inválida! Por favor, tente novamente.[/][/][/]')
                choice = console.input(f"\n[bold][cyan]| 🤔 Gostaria de realizar outro cálculo? [italic][orange1](S/N)\n\n[/][/]| : ").upper()
                controller = BF.multiple_choice_YN(choice)
                
    # Program footer
    console.print('\n', mdfooter)