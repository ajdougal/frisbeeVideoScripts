import os
from os import listdir
from os.path import isfile, join

# The purpose of this script is to take a folder with small video files
# 	all from the same game and concatenate them together, without encoding,
#	and then also produce an encoded mp4 video file from the raw concatenated
#   file. The final 2 files will be created within the folders that contained the
#   raw video files

# The workflow that is meant to be used with this script is as follows:
#	1) Show up to fields, film game(s) and STOP AND STOP between points. Potentially
#	you will film multiple games.
#   2) Come home, move files off of SD card, and put video clips into separate folders
#	for each game. Riverside Classic 2022 -> Game1, Riverside Classic 2022 -> Game2, etc...
#   3) Change path in script to be containing folder (D:\riverside.classic.2022\Game1\)
#   4) Run the script for each game folder you have 


# Path to containing folder
mypath = "D:\\riverside.classic.2022\\Game1\\"

# Tag to be used to name the files
tag = "2022.riverside.classic.game1"


# Disgusting Python Syntax that effectively gets a list of all filenames in a folder
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


# Loop through the file names, in alphabetical order (numerical order), and write the list to a text file
with open("{}mylist.txt".format(mypath), "w") as t:
	for f in onlyfiles:	
		t.write("file '{}{}'\n".format(mypath, f))


# FFMPEG the list to produce the concatenated file - Note the MP4 filetype, you may need to change to
# 	MOV or MTS or MKV or whatever it is that your camera records
os.system("ffmpeg -f concat -safe 0 -i {}mylist.txt -c:v copy {}{}.concat.MP4".format(mypath, mypath, tag))

# FFMPEG The concantenated file to encode it to mp4 
#	(reducing file size by 8x or so, and making it easier to upload on bad internet)

# Note the MP4 file type again - If you changed the above line to MOV/MTS/MKV
#	then you need to change it here too
os.system("ffmpeg -i {}{}.concat.MP4 {}{}.encoded.mp4".format(mypath, tag, mypath, tag))