# Script for extracting a video frame at a specific timestamp given as
# hh:mm:ss and writing the output to a file as a PBM.
# Syntax: extract-frame.sh <video file path> <timestamp> <output file path>

input=$1
timestamp=$2
output=$3

ffmpeg -i $input -ss $timestamp -frames:v 1 -f image2pipe -vcodec pbm $output