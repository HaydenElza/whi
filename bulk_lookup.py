import os, shutil

# User variables, should make into sysargv
dict_txt = "E:\\Hayden_Elza\\whi\\dict.txt"
directory = "\\\\GYMNOSPERM\Projects\\BordnerMaps_2014\\aerial_photos\\Wisconsin_historical_aerial_photos"
new_directory = "\\\\GYMNOSPERM\Projects\\BordnerMaps_2014\\aerial_photos\\Wisconsin_historical_aerial_photos2"

if not os.path.isdir(new_directory): os.mkdir(new_directory)

# Create dictionary
with open(dict_txt) as dict_file:
	name_dict = dict(line.strip().split() for line in dict_file)

for subdir,dirs,files in os.walk(directory):
	for filename in os.listdir(subdir):
		name, extension = os.path.splitext(filename)
		if name in name_dict:
			shutil.copyfile(os.path.join(subdir,filename),os.path.join(new_directory,name+"_"+name_dict[name]+extension))