#!/bin/bash

# This is a preprocessing script used to resize and resample a video.
# Syntax: preprocess-video <input file path> <width>x<height> <fps> <output file path>
# To convert a video to the format required by the conversion utility, use the following command.
# preprocess-video <input file path> 320x240 15 <output file path>
# Note that the frame rate may be modified to ensure that the video fits on the calculator.

input=$1
size=$2
fps=$3
output=$4

ffmpeg -i $input -s $size -r $fps $output