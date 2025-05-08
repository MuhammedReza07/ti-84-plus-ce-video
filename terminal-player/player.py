import time
import os
import math
#from draw_matrix import *
import draw_matrix
from test import make_rnd


# TODO get full video matrix from the video file somehow
# - load chosen file
# - determine any meta data (eg. fps)
# - build the raw binary matrix
# - get number of frames
# - build pixel matrix
#   - progress bar ?
# - print all


# load file
def load_file():
    FPS = 30  # Frames per second (will probably be determined by video file later)
    # get and return file matrix
    return [fake_file(), FPS]

# until then, make some random frames :)
def fake_file():
    all_frames = []
    nbr_of_frames = 6562
    progress =range(0,nbr_of_frames,math.ceil(nbr_of_frames/10))
    for frame in range(nbr_of_frames):
        if frame in progress:
            print(f"Loading: {math.floor(frame/nbr_of_frames * 100)}%")
        all_frames.append(draw_matrix.create_pixel_matrix(make_rnd(40,60)))
    return all_frames


# play the frames at determined speed
def play_video(all_frames, FPS):
    for frame in all_frames:
        os.system('clear')
        #pixel_frame = draw_matrix.create_pixel_matrix(frame)
        draw_matrix.draw(frame)
        time.sleep(1/FPS)
    print("End credits \n\nWe did this\nGo home now\n\nSpecial Thanks:\nMy Cats\nFor the Creme Fraishe boys")


# ----- MAIN --------------
def main():
    [file_frames, FPS] = load_file()
    play_video(file_frames, FPS)

if __name__=="__main__":
    main()