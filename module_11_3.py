import math
import inspect

class Аrea:

    def __init__(self, radius):
        self.radius = radius

    def circle(self):
        area1 = math.ceil(math.pi * (self.radius ** 2))
        print(f'Площадь окружности с радиусом {self.radius} равна {area1}')

    def introspection_info(obj):
        print(type(math.pi))
        print(dir(math.pi))
        print(dir(math))
        print(isinstance(math.pi, Аrea))
        print(inspect.isclass(Аrea))
        pi_module = inspect.getmodule(math.pi)
        print(type(pi_module), inspect.getmodule(math.pi))



Ar = Аrea(4)
Ar.circle()
Ar.introspection_info()