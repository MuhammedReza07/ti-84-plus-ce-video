import time
import os
#from draw_matrix import *
import draw_matrix
from test import make_rnd

FPS = 6  # Frames per second (will probably be determined by video file later)

# TODO get full video matrix from the video file somehow
# until then, make some random frames :)
all_frames = []
nbr_of_frames = 100
for frame in range(nbr_of_frames):
    all_frames.append(draw_matrix.create_pixel_matrix(make_rnd(40,60)))


# play the frames at determined speed
for frame in all_frames:
    os.system('clear')
    #pixel_frame = draw_matrix.create_pixel_matrix(frame)
    draw_matrix.draw(frame)
    time.sleep(1/FPS)
print("End credits \nWe did this\nGo home now")