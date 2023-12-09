from .BaseIllusion import *

class Delboeuf(BaseIllusion):
    shapes = [Shape.CIRCLE, Shape.RECTANGLE]

    def __init__(self, size, shape, n=2):
        super().__init__(size, n)

        assert shape in self.shapes
        self.question = f"Which inner {shape} looks bigger?"
        self.generate(shape)

    def generate(self, shape):
        color = [self.get_random_color() for _ in range(2)]

        r = 0.15
        rd = 0.05
        rr = np.linspace(r + rd, r + rd*4, self.n)

        for i in range(self.n):
            self.generate_inner(shape, self.canvas[i], r, rr[i], color)
        
        self.answer = 0

    def generate_inner(self, shape, canvas, r1, r2, color):
        self.draw_relative(shape, canvas, (0.5, 0.5), r1, color[0], -1)
        self.draw_relative(shape, canvas, (0.5, 0.5), r2, color[1], 0.01)

if __name__ == "__main__":
    illusion = Delboeuf((400, 400), Shape.CIRCLE, 4)
    illusion.show()
    