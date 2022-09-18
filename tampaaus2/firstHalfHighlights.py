import pandas
import os
import math

csv_file = pandas.read_csv("C:\\Users\\DoogleSports\\pythonScripts\\tampaaus2\\top50FirstHalf.csv", delimiter=",", skipinitialspace=True)
input_file_path_stem = "D:\\TampaAus02\\Top50\\"
output_file_path_stem = "D:\\TampaAus02\\Highlights\\"
input_file_path = input_file_path_stem + "Clip0005.MXF"

# Iterate through DataFrame (2-d table) row by row to make clips

iterator = 00

iterator_tag = "tampaaus2"

def shift_timestamp(input_time, delta_timestamp):
	input_time_seconds = convert_to_seconds(input_time)
	input_time_seconds += convert_to_seconds(delta_timestamp)
	return convert_to_string_timestamp(input_time_seconds)

def convert_to_seconds(input_time):
	split_time = input_time.split(":")
	total_seconds = int(split_time[0])*3600 + int(split_time[1])*60 + int(split_time[2])
	return int(total_seconds)

def convert_to_string_timestamp(time_in_seconds):
	return "%02d" % math.floor(time_in_seconds/3600) + ":" + "%02d" % math.floor((time_in_seconds%3600)/60) + ":" + "%02d" % math.floor((time_in_seconds%3600)%60)

# No clue what index does but it needs to be there... row is the variable that has data in it
for index, row in csv_file.iterrows():

	# Fancy string integer stuff - Makes it so that the number at start of clip is always triple digits
	# You have to do this so that the clips stay in alphabetical order - 1.name > 10.name in alphabetical order
	# However, 001.name < 010.name < 100.name
	string_iterator = "%03d" % iterator
	#start = shift_timestamp(row['start'], "01:30:25")
	start = row['start']
	#end = shift_timestamp(row['end'], "01:30:31")
	end = row['end']
	name = row['name']
	os.system("ffmpeg -i {} -vcodec copy -ss {} -to {} {}{}.{}.t50.{}.MP4".format(input_file_path, start, end, output_file_path_stem, iterator_tag, string_iterator, name))
	iterator += 1