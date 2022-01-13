import screen


class Function:

    ''' Classe para representar uma função matemática com uma incógnita x

    métodos
    -------
    findImage(x) -> float
        calcula a imagem de um ponto x na função especificada no
        atributo __function
    generate_graph(x_range, y_len, color)
        Gera e retorna o gráfico da função
    '''

    def __init__(self, function: str):

        '''
        atributos
        ---------
        __function
            função com um incógnita x
        '''

        self.__function = function

    def findImage(self, x: float) -> float:

        ''' calcula a imagem de um ponto x na função especificada no
        atributo __function '''

        image = eval(self.__function)
        return image

    def generate_graph(
        self,
        x_range: 'tuple(int, int)' = (-50, 50),
        y_range: 'tuple(int, int)' = (-50, 50),
        x_increment: float = 0.1,
        fore_color: str = 'WHITE',
        back_color: str = 'BLACK'
    ):

        ''' Gera e retorna o gráfico da função 

        parâmetros
        ----------
        x_range: 'tuple(int, int)'
            range dos valores de x no mapa cartesiano
        y_range: 'tuple(int, int)'
            range dos valores de y no mapa cartesiano
        x_increment: int
            quantidade em que o valor x será incrementado a cada ponto
        fore_color: str
            cor da representação de um ponto preenchido no mapa
        back_color: str
            cor da representação de um ponto vazio no mapa

        variáveis locais e constantes
        -----------------------------
        X_LEN: int
            tamanho do eixo x
        Y_LEN: int
            tamanho do eixo y
        cartesian_map: ScreenMap
            'ScreenMap' para representar um plano cartesiano
        points: list
            conjunto de pontos do plano cartesiano
        '''

        X_LEN = x_range[1] - x_range[0]
        Y_LEN = y_range[1] - y_range[0]

        cartesian_map = screen.ScreenMap(
            X_LEN, Y_LEN, default_color=back_color
        )
        points: 'screen.CartesianMapPoint' = []

        x = x_range[0]
        while x <= x_range[1]:

            y = self.findImage(x)
            point = screen.CartesianMapPoint(cartesian_map, x, y, fore_color)

            points.append(point)
            x += x_increment

        cartesian_map.fill(points)

        for point in cartesian_map.render():
            yield point


if __name__ == '__main__':

    quadratic = Function('x**2')

    for pixel in quadratic.generate_graph(
        (-25, 25), (-25, 25), 0.1, fore_color='red', back_color='white'
    ):
        print(pixel, end='')

    input()
