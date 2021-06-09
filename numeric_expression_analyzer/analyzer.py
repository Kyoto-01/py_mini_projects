from re import sub


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


def validate_exp(exp: str) -> bool:
    valid = sub(r'[^\d\.\+\-\*\/$]', r'', exp, 0)  # Sem caracteres que não sejam +-*/.0123456789
    valid = sub(r'([^\.\+\-\*\/$])\1+', r'\1', valid, 0)  # Sem repetições de símbolos não numéricos

    # Se valid for igual a exp, exp está escrito em um formato correto pois não sofreu alterações
    return valid == exp


expresao = input('Expressão: ').split()
if validate_exp(''.join(expresao)):
    print(process_exp(expresao, '*/'))
    print(process_exp(expresao, '+-'))
else:
    print('Digite apenas números e operadores(+, -, *, /)')
