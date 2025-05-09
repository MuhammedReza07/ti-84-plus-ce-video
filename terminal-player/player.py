import time
import os
import argparse
import math
#from draw_matrix import *
import draw_matrix
from test import make_rnd
import time


# TODO get full video matrix from the video file somehow
# - load chosen file
# - determine any meta data (eg. fps)
# - build the raw binary matrix
# - get number of frames
# - build pixel matrix
#   - progress bar ?
# - print all


def u32_from_le_bytes(le_bytes):
    return le_bytes[0] + (le_bytes[1] << 8) + (le_bytes[2] << 16) + (le_bytes[3] << 24)


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
def make_frame(frame_bytes, columns, rows):
    frame = [[0 for _ in range(columns)] for _ in range(rows)]

    frame_columns = columns // 8

    for i in range(frame_columns):
        column_bytes = frame_bytes[(i * rows):((i + 1) * rows)]
        for j in range(rows):
            frame[j][(i * 8):((i + 1) * 8)] = [(column_bytes[j] & (1 << k)) >> k for k in range(7, -1, -1)]

    return draw_matrix.create_pixel_matrix(frame)

# play the frames at determined speed
def play_video(file_name, fps):
    # Load the entire video file in RAM. (?)
    video_file = open(file_name, "rb")
    frames = video_file.read()

    # Read metadata.
    columns = u32_from_le_bytes(frames[0:4])
    frame_columns = columns // 8
    rows = u32_from_le_bytes(frames[4:8])
    frame_size = rows * frame_columns
    
    # Note that the frame data starts with an offset of 8 bytes.
    bottom = 8
    top = 8 + frame_size

    # Render frames.
    while top != len(frames):
        render_start = time.time()
        os.system('clear')
        frame = make_frame(frames[bottom:top], columns, rows)
        draw_matrix.draw(frame)
        bottom = top
        top += frame_size
        render_end = time.time()
        delay = (1/fps) - (render_end - render_start)
        if delay > 0:
            time.sleep(delay)

    print("End credits \n\nWe did this\nGo home now\n\nSpecial Thanks:\nMy Cats\nFor the Creme Fraishe boys")
 
# confirm that the file exists (TODO: and is a valid video file of correct format?)
def check_file_name(file_name):
    # print(f"{file_name} should probably be tested more") <--- This is a bit confusing...
    #print("test1", ".waw" in "filename.waw")
    #print(file_name)
    return os.path.isfile("videos/" + file_name)


# ----- MAIN --------------
def main(file_name, fps):
    if check_file_name(file_name):
        play_video("videos/" + file_name, fps)
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
