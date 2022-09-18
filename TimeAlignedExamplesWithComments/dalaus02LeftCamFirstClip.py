import pandas
import os

# The purpose of this script is to be used by video producers with multiple, synced camera angles
# 	By defining all the file locations, and aligning the videos, we can produce highlight clips from all
# 	camera angles without having to redo the timestamps for each angle.
# Effectively, you can watch the main production angle, say "Oh hey highlight from 12:30 to 12:50, called Joey.Wylie.Layout.D.5"
# 	and with these scripts you can use that timestamp to cut video clips from the left/right/field cams as well

# This script assumes all video files have already been time aligned - There is another script that will handle the
# 	time delta for each video file and change the timestamps accordingly

# CSV File Location with timestamps of clips in comma separated format
csv_file = pandas.read_csv("C:\\Users\\DoogleSports\\pythonScripts\\dalaus02\\dalaus02LeftCamFirstClip.csv", delimiter=",", skipinitialspace=True)

# Single video file folder location (file name comes in 2 lines down)
input_file_path_stem = "D:\\dalaus2\\LeftCamRaw\\"

# Output folder for highlight clips
output_file_path_stem = "D:\\dalaus2\\Highlights\\"

# Full file path for singular input file
input_file_path = input_file_path_stem + "C0001.MP4"


# Iterate through DataFrame (2-d table) row by row to make clips
iterator = 01

iterator_tag = "dalaus02lc"
# No clue what index does but it needs to be there... row is the variable that has data in it
for index, row in csv_file.iterrows():

	# Fancy string integer stuff - Makes it so that the number at start of clip is always triple digits
	# You have to do this so that the clips stay in alphabetical order - 1.name > 10.name in alphabetical order
	# However, 001.name < 010.name < 100.name
	string_iterator = "%03d" % iterator
	start = row['start']
	end = row['end']
	name = row['name']
	os.system("ffmpeg -i {} -vcodec copy -ss {} -to {} {}{}{}.{}.MP4".format(input_file_path, start, end, output_file_path_stem, iterator_tag, string_iterator, name))
	iterator += 1