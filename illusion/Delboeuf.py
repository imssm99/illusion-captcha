from BaseIllusion import *
import numpy as np
import cv2 as cv

class Delboeuf(BaseIllusion):
    def __init__(self, size, shape):
        super().__init__(size)

        self.question = f"Which inner {shape} looks bigger?"
        self.generate(shape)

    def generate(self, shape):
        color = [self.get_random_color() for _ in range(2)]

        self.draw_relative(shape, self.canvas[self.CORRECT], (0.5, 0.5), 0.15, color[0], -1)
        self.draw_relative(shape, self.canvas[self.CORRECT], (0.5, 0.5), 0.2, color[1], 0.01)

        self.draw_relative(shape, self.canvas[self.WRONG], (0.5, 0.5), 0.15, color[0], -1)
        self.draw_relative(shape, self.canvas[self.WRONG], (0.5, 0.5), 0.4, color[1], 0.01)

if __name__ == "__main__":
    illusion = Delboeuf((400, 400), Shape.CIRCLE)
    illusion.show()