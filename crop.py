import os, cv2

directory = "E:\\Hayden_Elza\\whi\\img2"
new_directory = "E:\\Hayden_Elza\\whi\\img3"
crop_amount = 200  # Amount in pixels to crop

if not os.path.isdir(new_directory): os.mkdir(new_directory)

for subdir,dirs,files in os.walk(directory):
	for file_name in os.listdir(subdir):
		file_path = os.path.join(subdir,file_name)
		if not os.path.isdir(file_path):
			img = cv2.imread(file_path)
			cropped_img = img[crop_amount:-crop_amount,crop_amount:-crop_amount] # [ystart:yend, xstart:xend]
			if file_name[-6:-4] == "_0": cv2.imwrite(os.path.join(new_directory,file_name),cropped_img)  # For images not in folders
			else:
				if not os.path.isdir(os.path.join(new_directory,subdir[-5:])): os.mkdir(os.path.join(new_directory,subdir[-5:]))
				cv2.imwrite(os.path.join(new_directory,subdir[-5:],file_name),cropped_img)  # For images in folders