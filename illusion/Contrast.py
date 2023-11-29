from BaseIllusion import *
import numpy as np
import colorsys

class Contrast(BaseIllusion):
    def __init__(self, size, shape):
        super().__init__(size)

        self.question = f"Which centered {shape} looks brighter?"
        self.generate(shape)

    def generate(self, shape):
        color_hsv = [np.random.rand() for _ in range(2)] + [0.5]

        color = [list(color_hsv) for _ in range(2)]
        color[0][2] = 0.3
        color[1][2] = 0.7

        self.canvas[self.CORRECT][:] = self.hsv_to_rgb(color[0])
        self.canvas[self.WRONG][:] = self.hsv_to_rgb(color[1])

        self.draw_relative(shape, self.canvas[self.CORRECT], (0.5, 0.5), 0.2, self.hsv_to_rgb(color_hsv), -1)
        self.draw_relative(shape, self.canvas[self.WRONG], (0.5, 0.5), 0.2, self.hsv_to_rgb(color_hsv), -1)

    def hsv_to_rgb(self, color_hsv):
        return (np.array(colorsys.hsv_to_rgb(*color_hsv)) * 255).tolist()

if __name__ == "__main__":
    illusion = Contrast((400, 400), Shape.CIRCLE)
    illusion.show()
    