import function
from os import system
from sys import argv

# Argumentos padrão para a função function.Function().generate_graph()
main_args = [-50, 50, -50, 50, .1, 'blue', 'white']

# Atualizando main_args com os valores passados pelo usuário
# são desconsiderados os 2 primeiros argumentos
for arg in argv[2:]:
    main_args[argv.index(arg) - 2] = arg

# tratando a função de entrada, que deve ser o primeiro argumento
if argv[1]:
    func_str = argv[1]
else:
    func_str = input('Enter a function: ')

# tratando os demais argumentos
x_range = int(main_args[0]), int(main_args[1])
y_range = int(main_args[2]), int(main_args[3])
x_increment = float(main_args[4])
point_color = main_args[5]
back_color = main_args[6]

# configurando terminal para renderizar cores
system('color')

''' Desenhando o gráfico da função no terminal '''
func = function.Function(func_str)

for pixel in func.generate_graph(
    x_range, y_range, x_increment, point_color, back_color
):
    print(pixel, end='')
