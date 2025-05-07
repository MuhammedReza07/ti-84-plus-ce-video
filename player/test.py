import random
import time
import os
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
def main():
    while True:
        os.system('clear')
        r = make_rnd(30,50)
        rpm = create_pixel_matrix(r)
        draw(rpm)
        time.sleep(0.5) # seconds between frames
if __name__=='__main__':
    main()