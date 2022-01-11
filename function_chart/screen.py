class Color:

    ''' Classe para armazenar valores de cores '''

    class ColorValue:

        ''' Classe interna para armazenar o valor foreground e background de uma
        cor específica '''

        def __init__(self, foreground: str, background: str):
            self.foreground = foreground
            self.background = background

    BLACK = ColorValue('\033[1;30m', '\033[1;40m')
    RED = ColorValue('\033[1;41m', '\033[1;41m')
    GREEN = ColorValue('\033[1;32m', '\033[1;42m')
    YELLOW = ColorValue('\033[1;33m', '\033[1;43m')
    BLUE = ColorValue('\033[1;34m', '\033[1;44m')
    MAGENTA = ColorValue('\033[1;35m', '\033[1;45m')
    CYAN = ColorValue('\033[1;36m', '\033[1;46m')
    GRAY_LIGHT = ColorValue('\033[1;37m', '\033[1;47m')
    GRAY_DARK = ColorValue('\033[1;90m', '\033[1;100m')
    RED_LIGHT = ColorValue('\033[1;91m', '\033[1;101m')
    GREEN_LIGHT = ColorValue('\033[1;92m', '\033[1;102m')
    YELLOW_LIGHT = ColorValue('\033[1;93m', '\033[1;103m')
    BLUE_LIGHT = ColorValue('\033[1;94m', '\033[1;104m')
    MAGENTA_LIGHT = ColorValue('\033[1;95m', '\033[1;105m')
    CYAN_LIGHT = ColorValue('\033[1;96m', '\033[1;106m')
    WHITE = ColorValue('\033[1;97m', '\033[1;107m')
    RESET = '\033[0;0m'


class MapPoint:

    ''' Os objetos desta classe representam pontos em um 'ScreenMap' '''

    def __init__(self, x, y, fill_color='WHITE'):

        '''
        atributos
        ---------
        x
            Posição x no ScreenMap
        y
            Posição y no ScreenMap
        fill_color
            Cor de preenchimento do ponto no ScreenMap
        '''

        self.__x = x
        self.__y = y
        self.__fill_color = getattr(Color, f'{fill_color}').background

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def fill_color(self):
        return self.__fill_color


class ScreenMap:

    '''
    Classe para representar a estrutura de um gráfico no console

    ...

    atributos:
    --------------------
    DISPLAY_FILL:str
        um caractere para representar campos preenchidos no mapa
    DISPLAY_VOID:str
        um caractere para representar campos vazios no mapa

    métodos
    ----------------------
    fill(filled_fields)
        função para preencher o __map
    show()
        Função para mostrar o conteúdo do map formatado
    '''

    DISPLAY_FILL = ' '
    DISPLAY_VOID = '-'

    def __init__(self, x_len: int, y_len: int):
        self.__x_len = x_len
        self.__y_len = y_len
        self.__map = [[None] * x_len for i in range(y_len)]

    def fill(self, filled_fields: 'tuple(MapPoint)'):

        ''' função para preencher o __map '''

        for mp in filled_fields:
            x = mp.x
            y = mp.y
            self.__map[y][x] = mp

    def show(self):

        ''' Função para mostrar o conteúdo do map formatado '''

        for y in self.__map:
            for x in y:
                # x -> Valores do tipo 'MapPoint' ou 'None'
                if x:
                    print(
                        x.fill_color,
                        self.__class__.DISPLAY_FILL,
                        sep='', end=''
                    )
                else:
                    print(self.__class__.DISPLAY_VOID, end='')

                print(Color.RESET, end='')
            print()


if __name__ == '__main__':

    ''' Testando o módulo '''

    screen = ScreenMap(32, 32)
    color = 'RED'
    draw = (
        MapPoint(2, 0, color),
        MapPoint(3, 0, color),
        MapPoint(1, 1, color),
        MapPoint(2, 1, color),
        MapPoint(3, 1, color),
        MapPoint(4, 1, color),
        MapPoint(1, 2, color),
        MapPoint(2, 2, color),
        MapPoint(4, 2, color),
        MapPoint(1, 3, color),
        MapPoint(2, 3, color),
        MapPoint(3, 3, color),
        MapPoint(4, 3, color),
        MapPoint(1, 4, color),
        MapPoint(2, 4, color),
        MapPoint(1, 5, color),
        MapPoint(2, 5, color),
        MapPoint(3, 5, color),
        MapPoint(4, 5, color)
    )

    screen.fill(draw)
    screen.show()
