from .BaseIllusion import *
import numpy as np

class Ebbinghaus(BaseIllusion):
    shapes = [Shape.CIRCLE]

    def __init__(self, size, shape, n=2):
        super().__init__(size, n)

        assert shape in self.shapes
        self.question = f"Which inner {shape} looks {'larger' if self.n == 2 else 'largest'}?"
        self.generate()

    def generate(self):
        color = [self.get_random_color() for _ in range(2)]

        r = 0.10
        rd = 0.04
        rr = np.linspace(r - rd, r + rd, self.n)

        for i in range(self.n):
            self.generate_inner(self.canvas[i], r, rr[i], color)

        self.answer = 0
    
    def generate_inner(self, canvas, r, r2, color):
        self.draw_circle_relative(canvas, (0.5, 0.5), r, color[0], -1)
        distance = r + r2 + 0.01
        n = int(np.pi * distance / r2)
        angles = np.deg2rad(np.linspace(0, 360, n, False))
        for angle in angles:
            self.draw_circle_relative(canvas, (0.5 + (np.cos(angle) * distance), 0.5 + (np.sin(angle)) * distance), r2, color[1], -1)


if __name__ == "__main__":
    illusion = Ebbinghaus((300, 300), Shape.CIRCLE, n=6)
    illusion.show()
    