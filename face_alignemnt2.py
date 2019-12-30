import imutils
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from PIL import Image
import argparse
import dlib
import cv2, glob
variables = ["Neutral"]
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

def get_files(variable):
	files = glob.glob("./fer2013_neutral/%s/*" %variable)
	return files
i=1
for variable in variables:
	invariable = get_files(variable)
	for item in invariable:
		image = cv2.imread(item)
		image = imutils.resize(image,width=256)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		a = variable
		cv2.imwrite('./resized_fer2013_neutral/'+a+'/stargan_%i.jpg' %i, image)
		i+=1
