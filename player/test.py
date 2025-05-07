import random
from draw_matrix import *

# make random matrix
def make_rnd(r, c):
    matrix = []
    for r in range(r):
        matrix.append([])
        for _ in range(c):
            matrix[r].append(random.randint(0,1))
    return matrix

# run draw_matrix functions on the random matrix
r = make_rnd(10,10)
rpm = create_pixel_matrix(r)
draw(rpm)