from lab_pyton_oop.geom_figur import geom_figur
from lab_pyton_oop.color import color

class rectangle(geom_figur):
    square = 0
    w = 0
    h = 0
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, w_param, h_param):

        self.w = w_param
        self.h = h_param
        self.colour= color(color_param)

    def square(self):

        return self.w*self.h

    def __repr__(self):
        return '{} {} цвета шириной {} , высотой {} и площадью {}.'.format(
            rectangle.get_figure_type(),
            self.colour.color,
            self.w,
            self.h,
            self.square()
        )
