from BaseIllusion import *
import numpy as np
import cv2 as cv

class Ebbinghaus(BaseIllusion):
    def __init__(self, size):
        super().__init__(size)

        self.question = f"Which inner circle looks bigger?"
        self.generate()

    def generate(self):
        color = [self.get_random_color() for _ in range(2)]

        r = 0.10
        r2 = 0.08
        r3 = 0.15

        self.draw_circle_relative(self.canvas[self.CORRECT], (0.5, 0.5), r, color[0], -1)
        distance = r + r2 + 0.01
        n = int(np.pi * distance / r2)
        angles = np.deg2rad(np.linspace(0, 360, n, False))
        for angle in angles:
            self.draw_circle_relative(self.canvas[self.CORRECT], (0.5 + (np.cos(angle) * distance), 0.5 + (np.sin(angle)) * distance), r2, color[1], -1)

        self.draw_circle_relative(self.canvas[self.WRONG], (0.5, 0.5), r, color[0], -1)
        distance = r + r3 + 0.01
        n = int(np.pi * distance / r3)
        angles = np.deg2rad(np.linspace(0, 360, n, False))
        for angle in angles:
            self.draw_circle_relative(self.canvas[self.WRONG], (0.5 + (np.cos(angle) * distance), 0.5 + (np.sin(angle)) * distance), r3, color[1], -1)


if __name__ == "__main__":
    illusion = Ebbinghaus((400, 400))
    illusion.show()