''' showcasing how everything in Python is a "first-class" object '''

import math


objects = [abs, math, ValueError]
print(objects)

great_number: int = -420
abs_res: int = objects[0](great_number)
print(abs_res)

it_takes: int = 2
famous_number: float = objects[1].sqrt(it_takes)
print(famous_number)

try:
    # pylint: disable=invalid-name
    x = int("obvo not an integer")
    # pylint: enable=invalid-name
except objects[2] as ve:
    print(ve)
