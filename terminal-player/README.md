This should definitely have an epilepsy warning for now, this is it! You are warned :)

# Terminal Video Player

As it turns out, the terminal is pretty strictly character based and not very friendly with any kind of direct pixel manipulations. So for the video player to look as nice as possible while still being relatively simple we will be using sets of ASCII half blocks in strings to simulate pixels. Two rows of pixels are combined into one string of characters with full blocks █, upper/lower half blocks ▀/▄ or empty. These strings are printed to the terminal for each frame.

# Usage

In terminal: `python3 player.py -f <file_name>`

# Potential issues

This way of printing the video to the terminal makes the possible resolution smaller than the originally intended 320x240 (unless you happen to have *incredible* screen resolution). This solution also introduces some new possible issues like screen flickering due to clearing the terminal and printing the new string array for each frame, and resulting in some potentially huge loading times and memory loads when constructing all the string arrays.
