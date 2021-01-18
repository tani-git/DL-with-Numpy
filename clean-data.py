import os
import shutil
import cv2

def get_correct_data(src_path, des_path):
	src_lis = [os.path.join(src_path, i) for i in os.listdir(src_path)]
	count = 0
	for j in src_lis:
		print("Total: {}, Remaining: {}".format(len(src_lis), len(src_lis) - count))
		base = os.path.basename(j)
		if ".jpg" not in base:
			pass
		else:
			try:
				img = cv2.imread(j)
				print(j)
				shutil.copy(j, des_path)
				xml_file = j[:-4] + ".xml"
				shutil.copy(xml_file , des_path)
			except Exception:
				print("Invalid Image")
				continue
		count+=1
				

src_path = "/home/code-ml/Desktop/SSD-TR/TESE/zip-buckle/test"
des_path = "/home/code-ml/Desktop/SSD-TR/TESE/zip-buckle/test_clean"

get_correct_data(src_path, des_path)