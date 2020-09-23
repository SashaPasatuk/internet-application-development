from lab_pyton_oop.rectangle import rectangle

class square(rectangle):

    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, s):

        self.side = s
        super().__init__(color, self.side, self.side)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            square.get_figure_type(),
            self.colour.color,
            self.side,
            self.square()
        )
