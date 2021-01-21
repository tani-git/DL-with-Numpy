import os
import shutil
import cv2
import pandas as pd

def get_correct_data(input_df, src_path, des_path):
	df = pd.read_csv(input_df)
	file = df.filename
	src_lis = []
	for i in file:
		src_lis.append(os.path.join(src_path, i))
	# src_lis = [os.path.join(src_path, i) for i in os.listdir(src_path)]
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
				

input_csv = "/home/code-ml/Desktop/SSD-TR/SSD-Mobilenet-Custom-Object-Detector-Model-using-Tensorflow-2/tensorflow_model/data/test_labels.csv"
src_path = "/home/code-ml/Desktop/SSD-TR/TESE/zip-buckle/test"
des_path = "/home/code-ml/Desktop/SSD-TR/TESE/zip-buckle/test_clean"

get_correct_data(input_csv,src_path, des_path)
