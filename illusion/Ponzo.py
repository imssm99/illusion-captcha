from .BaseIllusion import *

class Ponzo(BaseIllusion):
    shapes = [Shape.LINE]

    def __init__(self, size, shape):
        super().__init__(size)

        assert shape in self.shapes
        self.question = f"Which {shape} looks longer?"
        self.generate()

    def generate(self):
        color = [self.get_random_color() for _ in range(2)]

        line1 = [(0.4, 0), (0.1, 1)]
        line2 = [(0.6, 0), (0.9, 1)]

        self.draw_line_relative(self.canvas[self.CORRECT], (0.35, 0.3), (0.65, 0.3), color[0], 0.01)
        self.draw_line_relative(self.canvas[self.CORRECT], line1[0], line1[1], color[1], 0.01)
        self.draw_line_relative(self.canvas[self.CORRECT], line2[0], line2[1], color[1], 0.01)

        self.draw_line_relative(self.canvas[self.WRONG], (0.35, 0.7), (0.65, 0.7), color[0], 0.01)
        self.draw_line_relative(self.canvas[self.WRONG], line1[0], line1[1], color[1], 0.01)
        self.draw_line_relative(self.canvas[self.WRONG], line2[0], line2[1], color[1], 0.01)

if __name__ == "__main__":
    illusion = Ponzo((400, 400))
    illusion.show()
