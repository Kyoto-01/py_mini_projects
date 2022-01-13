class Color:

    ''' Classe para armazenar valores de cores

    métodos
    -------
    get_color(color_name, type_color)
        Recebe o nome de uma cor e retorna o seu valor ANSI
    '''

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

    def get_color(color_name: str, type_color: str = 'foreground'):
        color_name = color_name.upper()
        color_value = getattr(Color, color_name)

        if type_color == 'foreground':
            color_value = color_value.foreground
        else:
            color_value = color_value.background

        return color_value
