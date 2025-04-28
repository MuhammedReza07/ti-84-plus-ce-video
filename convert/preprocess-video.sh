#!/bin/bash

# This is a preprocessing script used to resize and resample a video.
# Syntax: preprocess-video.sh <input file path> <width>x<height> <fps> <output file path>
#
# To convert the video such that its dimensions are compatible with the TI-84 Plus CE LCD display,
# the following command may be used.
# preprocess-video.sh <input file path> 320x240 <fps> <output file path>
#
# Note that the frame rate must be set such that the video fits on the calculator if the video
# is going to be played on the TI-84 Plus CE.

input=$1
size=$2
fps=$3
output=$4

ffmpeg -i $input -s $size -r $fps $output