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

# make file
def make_file(h, w, frames):
    all_frames = []
    progress =range(0,frames,math.ceil(frames/10))
    for frame in range(frames):
        # maybe? show progress for the slow loading
        if frame in progress:
            print(f"Loading: {math.floor(frame/frames * 100)}%")
        all_frames.append(create_pixel_matrix(make_rnd(h,w)))
    return all_frames

# run draw_matrix functions on the random matrix
def main():
    # make a random simulated file
    fps = 30
    height = 40
    width = 60
    nbr_of_frames = 6503
    file = make_file(height,width,nbr_of_frames)

    # run video loop
    for frame in file:
        os.system('clear')
        #r = make_rnd(height,width)
        #rpm = create_pixel_matrix(r)
        draw(frame)
        time.sleep(1/fps) # seconds between frames
if __name__=='__main__':
    main()