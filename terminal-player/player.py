import time
import os
import math
#from draw_matrix import *
import draw_matrix
from test import make_rnd

FPS = 30  # Frames per second (will probably be determined by video file later)

# TODO get full video matrix from the video file somehow
# - load chosen file
# - determine any meta data (eg. fps)
# - build the raw binary matrix
# - get number of frames
# - build pixel matrix
#   - progress bar ?
# - print all


# until then, make some random frames :)
all_frames = []
nbr_of_frames = 6562
progress =range(0,nbr_of_frames,math.ceil(nbr_of_frames/10))
for frame in range(nbr_of_frames):
    if frame in progress:
            print(f"Loading: {math.floor(frame/nbr_of_frames * 100)}%")
    all_frames.append(draw_matrix.create_pixel_matrix(make_rnd(40,60)))


# play the frames at determined speed
for frame in all_frames:
    os.system('clear')
    #pixel_frame = draw_matrix.create_pixel_matrix(frame)
    draw_matrix.draw(frame)
    time.sleep(1/FPS)
print("End credits \nWe did this\nGo home now")