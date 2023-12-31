from .BaseIllusion import *

class MullerLyer(BaseIllusion):
    shapes = [Shape.LINE]

    def __init__(self, size, shape):
        super().__init__(size)

        assert shape in self.shapes
        self.question = f"Which {shape} looks longer?"
        self.generate()

    def generate(self):
        color = [self.get_random_color() for _ in range(2)]

        pt1 = (0.3, 0.5)
        pt2 = (0.7, 0.5)

        self.answer = 0

        self.draw_line_relative(self.canvas[0], pt1, pt2, color[0], 0.01)
        self.draw_line_relative(self.canvas[0], pt1, (pt1[0] - 0.1, pt1[1] + 0.1), color[1], 0.01)
        self.draw_line_relative(self.canvas[0], pt1, (pt1[0] - 0.1, pt1[1] - 0.1), color[1], 0.01)
        self.draw_line_relative(self.canvas[0], pt2, (pt2[0] + 0.1, pt2[1] + 0.1), color[1], 0.01)
        self.draw_line_relative(self.canvas[0], pt2, (pt2[0] + 0.1, pt2[1] - 0.1), color[1], 0.01)

        self.draw_line_relative(self.canvas[1], pt1, pt2, color[0], 0.01)
        self.draw_line_relative(self.canvas[1], pt1, (pt1[0] + 0.1, pt1[1] + 0.1), color[1], 0.01)
        self.draw_line_relative(self.canvas[1], pt1, (pt1[0] + 0.1, pt1[1] - 0.1), color[1], 0.01)
        self.draw_line_relative(self.canvas[1], pt2, (pt2[0] - 0.1, pt2[1] + 0.1), color[1], 0.01)
        self.draw_line_relative(self.canvas[1], pt2, (pt2[0] - 0.1, pt2[1] - 0.1), color[1], 0.01)

if __name__ == "__main__":
    illusion = MullerLyer((400, 400))
    illusion.show()
    