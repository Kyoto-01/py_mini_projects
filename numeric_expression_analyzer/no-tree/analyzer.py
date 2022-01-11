from re import sub


def format_exp(exp: str) -> str:
    formated = sub(r'[^\d\.\+\-\*\/$]', r'', exp, 0)  # Sem caracteres que não sejam +-*/.0123456789
    formated = sub(r'([\.\+\-\*\/])\1+', r'\1', formated, 0)  # Sem repetições de símbolos não numéricos

    return formated


def segment_exp(exp: str) -> list[str]:
    segmented_exp = ''
    for char in exp:
        if char.isdigit() or char == '.':
            segmented_exp += char
        else:
            segmented_exp += f' {char} '

    return segmented_exp.split()


def process_exp(exp: list, operators: str) -> str:
    while any(o in operators for o in exp):  # enquanto houver algum operador do parâmetro operators na expressão
        for i in range(len(exp)):  # então percorra a expressão até encontrar o primeiro desses operadores
            if exp[i] in operators:
                n1, n2 = float(exp[i - 1]), float(exp[i + 1])
                result = 0

                if exp[i] == '*':
                    result = n1 * n2
                elif exp[i] == '/':
                    result = n1 / n2
                elif exp[i] == '+':
                    result = n1 + n2
                elif exp[i] == '-':
                    result = n1 - n2

                del exp[i - 1:i + 2]
                exp.insert(i - 1, str(result))
                break
    return ' '.join(exp)


expression = input('Expressão: ')
expression = format_exp(expression)
expression = segment_exp(expression)

print(''.join(expression))
print(process_exp(expression, '*/'))
print(process_exp(expression, '+-'))
