#!/bin/bash

# This script converts a video processed by preprocess-video.sh to a RLEMV encoded video.
# Syntax: rlemv.sh <input file path> <fps> <output file path>.
#
# Note that the frame rate of the RLEMV encoded video must be the same as the original video
# for the video to play as intended.

input=$1
fps=$2
output=$3

# Preliminary form, dumps frames as PBM to $output.
ffmpeg -i $input -f image2pipe -vcodec pbm pipe:1 >> $output