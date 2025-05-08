import time
import os
import argparse
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


# until then, make some random frames :)
def fake_file():
    all_frames = []
    nbr_of_frames = 6562
    h = 40
    w = 60
    progress =range(0,nbr_of_frames,math.ceil(nbr_of_frames/10))
    for frame in range(nbr_of_frames):
        if frame in progress:
            print(f"Loading: {math.floor(frame/nbr_of_frames * 100)}%")
        all_frames.append(draw_matrix.create_pixel_matrix(make_rnd(h,w)))
    return all_frames



# take encoded string segment (one frame), build binary matrix and convert to pixels
def make_frame(encoded_string):
    binary_matrix = []

    # TODO: whatever black magic is necessary to build the binary matrix

    return draw_matrix.create_pixel_matrix(binary_matrix)

# load file and read content to string
def load_file(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
    all_frames = []

    #print(file_content)

    # TODO: convert file content to pixel_matrices, read and save correct FPS
    #       - add frames to all_frames and return instead of fake_file()

    # for each encoded string segment:
    #   all_frames.append(make_frame(string_segment))

    FPS = 30  # ignored for now, TODO: fix if relevant metadata works

    # get and return file matrix
    return [fake_file(), FPS] # TODO: change fake_file() to all_frames when fixed

# play the frames at determined speed
def play_video(all_frames, FPS):
    for frame in all_frames:
        os.system('clear')
        #pixel_frame = draw_matrix.create_pixel_matrix(frame)
        draw_matrix.draw(frame)
        time.sleep(1/FPS)
    print("End credits \n\nWe did this\nGo home now\n\nSpecial Thanks:\nMy Cats\nFor the Creme Fraishe boys")
 
# confirm that the file exists (TODO: and is a valid video file of correct format?)
def check_file_name(file_name):
    print(f"{file_name} should probably be tested more")
    #print("test1", ".waw" in "filename.waw")
    #print(file_name)
    return os.path.isfile("videos/" + file_name)


# ----- MAIN --------------
def main(file_name, fps):
    if check_file_name(file_name):
        [file_frames, FPS] = load_file("videos/" + file_name) # TODO: change to fps if relevant
        play_video(file_frames, fps)
    else:
        print(f"{file_name} is not a valid file name")

if __name__=="__main__":
    #file_name = sys.argv[1]
    parser = argparse.ArgumentParser(
        description="Script that plays video in terminal from file"
    )
    parser.add_argument("-f", required=True, type=str)
    parser.add_argument("-fps", required=False, type=int)
    args = parser.parse_args()
    file_name = args.f
    fps = args.fps
    if fps is None:
        fps = 30
    main(file_name, fps)
