from .BaseIllusion import *
import numpy as np
import colorsys

class Contrast(BaseIllusion):
    shapes = [Shape.CIRCLE, Shape.RECTANGLE]

    def __init__(self, size, shape, n=2):
        if n % 2:
            n -= 1
        super().__init__(size, n)

        assert shape in self.shapes
        self.question = f"Which centered {shape} looks {'darker' if self.n == 2 else 'darkest'}?"
        self.generate(shape)

    def generate(self, shape):
        color_hsv = [np.random.rand() for _ in range(2)] + [0.5]

        color = [list(color_hsv) for _ in range(self.n)]

        r = 0.5
        rd = 0.3
        rr = np.linspace(r - rd, r + rd, self.n)

        for i in range(self.n):
            color[i][2] = rr[i]
            self.canvas[i][:] = self.hsv_to_rgb(color[i])
            self.draw_relative(shape, self.canvas[i], (0.5, 0.5), 0.2, self.hsv_to_rgb(color_hsv), -1)

        self.answer = self.n - 1

    def hsv_to_rgb(self, color_hsv):
        return (np.array(colorsys.hsv_to_rgb(*color_hsv)) * 255).tolist()

if __name__ == "__main__":
    illusion = Contrast((400, 400), Shape.CIRCLE, n=4)
    illusion.show()
    