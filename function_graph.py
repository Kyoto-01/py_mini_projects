from abc import ABC, abstractmethod


class BadRangeException(Exception):
    
    def __init__(self, msg='The range is invalid!'):
        super().__init__(msg)
        

class Function(ABC):
    
    def __init__(self, x: float):
        self.__x = x
        
    @property
    def x(self):
        return self.__x
        
    @x.setter
    def x(self, value: float):
        self.__x = value
    
    @abstractmethod
    def calc(self) -> float:
        pass
    
    
class Polynomial(Function):
    
    def __init__(self, x: float, degree: int):
        super().__init__(x)
        self.__degree = degree
        
    def calc(self):
        res = 0
        for i in range(self.__degree + 1):
            res += self.x ** i
            
        return res
        
        
class Rational(Function):
    
    def __init__(self, x: float):
        super().__init__(x)
        
    def calc(self):
        try:
            p2: float = Polynomial(self.x, 2).calc()
            print('p2', p2)
            p3: float = Polynomial(self.x, 3).calc()
            print('p3', p3)
            res = p2 / p3
            print('res', res)
            
        except ZeroDivisionError:
            res = 0
        
        return res
    

class FunctionGraph:
    
    GRAPH_SIMBOL = '@'
    
    def __init__(self, x_start: float, x_end: float, func_cod: int):
        if x_start > x_end:
            raise BadRangeException('O ponto inicial do intervalo não pode ser maior do que o ponto final!')
        
        self.__x_start = x_start
        self.__x_end = x_end
        self.__domain_len = int(x_end - x_start + 1)
        self.__func_cod = func_cod
        self.__map = [[0] * self.__domain_len for i in range(self.__domain_len)]
        
    def draw_graph(self):
        funcs = [
            Polynomial(0, 1),
            Polynomial(0, 2),
            Polynomial(0, 3),
            Polynomial(0, 4),
            Rational(0)
        ]
        func = funcs[self.__func_cod]
        
        for x in range(self.__x_start, self.__x_end + 1):
            func.x = x
            y = int(func.calc())
            if 0 <= y < self.__domain_len:
                self.__map[y][x + abs(self.__x_start)] = 1
    
    def show_graph(self):
        for i in range(len(self.__map) - 1, -1, -1):
            for j in self.__map[i]:
                print(f'{self.__class__.GRAPH_SIMBOL if j == 1 else "-"}', end='')
            print()

        
if __name__ == '__main__':
    
    x_start, x_end = -10, 10
    '''
    quad_func_graph = FunctionGraph(x_start, x_end, 0)
    quad_func_graph.draw_graph()
    quad_func_graph.show_graph()
    print(0)
    
    quad_func_graph = FunctionGraph(x_start, x_end, 1)
    quad_func_graph.draw_graph()
    quad_func_graph.show_graph()
    print(1)

    quad_func_graph = FunctionGraph(x_start, x_end, 2)
    quad_func_graph.draw_graph()
    quad_func_graph.show_graph()
    print(2)
    
    quad_func_graph = FunctionGraph(x_start, x_end, 3)
    quad_func_graph.draw_graph()
    quad_func_graph.show_graph()
    print(3)
    '''
    quad_func_graph = FunctionGraph(x_start, x_end, 4)
    quad_func_graph.draw_graph()
    quad_func_graph.show_graph()
    print(4)
