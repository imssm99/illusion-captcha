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

    if illusion_class in [Contrast, Delboeuf, Ebbinghaus]:
        illusion = illusion_class(size, shape, random.randint(2, 4))
        illusion.shuffle_canvas()
        return illusion
    
    illusion = illusion_class(size, shape)
    illusion.shuffle_canvas()
    return illusion

if __name__ == "__main__":
    illusion = getRandomIllusion((300, 300))
    print(illusion.check_answer(1))