import os, shutil

# User variables, should make into sysargv
directory = "\\\\GYMNOSPERM\Projects\\BordnerMaps_2014\\aerial_photos\\Wisconsin_historical_aerial_photos2"
#directory = "E:\\Hayden_Elza\\whi\\img2"

for file_name in os.listdir(directory):
	if len(file_name)<23: continue
	subdir = os.path.join(directory,file_name[12:17])
	if not os.path.isdir(subdir): os.mkdir(subdir)
	shutil.move(os.path.join(directory,file_name),os.path.join(subdir,file_name))