import numpy as np
import cv2 as cv

class Shape:
    RECTANGLE = "rectangle"
    CIRCLE = "circle"
    LINE = "line"

class BaseIllusion:
    question = ""
    WRONG = 0
    CORRECT = 1

    def __init__(self, size, random=True):
        self.size = size
        if random:
            self.WRONG, self.CORRECT = np.random.choice([0, 1], 2, False)
        self.canvas = [np.full((size[0], size[1], 3), 255, dtype=np.uint8) for _ in range(2)]

    def filter(self):
        pass

    def generate(self):
        pass

    def get_coord(self, coord_rel):
        """
        get real coord from relative coord
        :coord_rel: relative coord
        :return: real coord
        """
        return (int(self.size[0] * coord_rel[0]), int(self.size[1] * coord_rel[1]))

    def get_thickness(self, thickness_rel, radius_rel):
        """
        get real thickness from relative thickness
        :thickness_rel: relative thickness
        :thickness_rel: relative radius
        :return: real thickness
        """
        if thickness_rel > 0:
            radius_rel -= thickness_rel / 2
            thickness = self.convert_relative(thickness_rel)
        else:
            thickness = -1
        return thickness

    def convert_relative(self, value_rel):
        """
        get real value from relative value
        :value_rel: relative value (0, 1)
        :return: real value
        """
        return int(np.mean(self.size) * value_rel)

    def draw_circle_relative(self, canvas, coord_rel, radius_rel, color, thickness_rel, **kwargs):
        radius = self.convert_relative(radius_rel)
        cv.circle(canvas, self.get_coord(coord_rel), radius, color, self.get_thickness(thickness_rel, radius_rel), **kwargs)

    def draw_rectangle_relative(self, canvas, coord_rel, radius_rel, color, thickness_rel, **kwargs):
        coord = self.get_coord(coord_rel)
        radius = self.convert_relative(radius_rel)
        pt1 = (coord[0] - radius, coord[1] - radius)
        pt2 = (coord[0] + radius, coord[1] + radius)
        cv.rectangle(canvas, pt1, pt2, color, self.get_thickness(thickness_rel, radius_rel), **kwargs)

    def draw_line_relative(self, canvas, coord_rel1, coord_rel2, color, thickness_rel, **kwargs):
        cv.line(canvas, self.get_coord(coord_rel1), self.get_coord(coord_rel2), color, self.convert_relative(thickness_rel), **kwargs)

    def draw_relative(self, shape, *args):
        match shape:
            case Shape.CIRCLE:
                self.draw_circle_relative(*args)
            case Shape.RECTANGLE:
                self.draw_rectangle_relative(*args)
            case Shape.LINE:
                self.draw_line_relative(*args)

    def check_answer(self, answer):
        return answer == self.CORRECT

    def get_random_color(self):
        return [np.random.randint(0, 256) for _ in range(3)]

    def show(self):
        print(self.question)
        print(self.CORRECT)
        cv.imshow("Debug", cv.hconcat([self.canvas[0], self.canvas[1]]))
        cv.waitKey(0)
