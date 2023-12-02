from .BaseIllusion import Shape
from .Contrast import Contrast
from .Delboeuf import Delboeuf
from .Ebbinghaus import Ebbinghaus
from .MullerLyer import MullerLyer
from .Ponzo import Ponzo
import random

def getRandomIllusion(size):
    illusion_class = random.choice([Contrast, Delboeuf, Ebbinghaus, MullerLyer, Ponzo])
    shape = random.choice(illusion_class.shapes)
    return illusion_class(size, shape)

if __name__ == "__main__":
    illusion = getRandomIllusion((300, 300))
    print(illusion.check_answer(1))