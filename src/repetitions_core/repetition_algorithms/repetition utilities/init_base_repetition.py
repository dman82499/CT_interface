'''A class for initializing the base of a repetition for pixels or sensors, without any other begining repetitions
Initializes with group repetitions'''
from typing import List

from repetitions_core.repetition_algorithms import group
#we should really define colors to be their own serperate atributes
#so techically there are two repetition objects here
''':returns a repetition object when given a pixel'''
@staticmethod
def initialize_from_pixel(pixel: List):
    #better: use wrapper constructor for memory here instead
    pixel_reptition = group.group_repetition()
    pixel_reptition.rl_language = "for_all: p"
    #fill p with the contents of the pixel

