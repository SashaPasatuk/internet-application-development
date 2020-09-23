from lab_pyton_oop.geom_figur import geom_figur
from lab_pyton_oop.color import color
import math

class circle(geom_figur):
    r = 0
    _square_ = 0
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self,  color_param, r,):
        self.r = r
        self.colour = color(color_param)

    def square(self):
        return float(math.pi) * self.r * self.r

    def __repr__(self):
        return '{} {} цвета радиусом {} и площадью {}.'.format(
            circle.get_figure_type(),
            self.colour.color,
            self.r,
            self.square()
        )
