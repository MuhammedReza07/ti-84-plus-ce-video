#!/bin/bash

# This is the "conversion utility" that takes a file preprocessed by ./preprocess-video.sh
# and converts it to a sequence of TI-84 Application Variables (.8xv files) containing
# Run-length encoded frames.
#
# Preliminary version syntax: convert.sh <input file path> <width> <height> <output file path>

input=$1
width=$2
height=$3
output=$4

ffmpeg -i $input -f image2pipe -vcodec pbm pipe:1 >> $output