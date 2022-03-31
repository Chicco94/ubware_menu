import cv2 
import pytesseract
from config import file_result_path

def convert(filepath)->bool:
	'''Convert an image into a text file containing all the readable text'''
	try:
		img = cv2.imread(filepath)
		text_readed = pytesseract.image_to_string(img)
		with open(file_result_path,"w") as res_file:
			res_file.write(text_readed)
		return True
	except Exception as e:
		print(e)
		return False

if __name__ == '__main__':
	convert('images/2022-03-26.jpg')