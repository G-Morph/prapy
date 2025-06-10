# bounce.py
''' Exercise 1.5 '''


def rebound(initial_height: float | int) -> float:
    ''' return the rebound height based on initial height '''
    gravity: float = 3.0 / 5.0
    return initial_height * gravity

height: float = 100
for bounce in range(1, 11):
    height = round(rebound(height), 4)
    print(bounce, height)
