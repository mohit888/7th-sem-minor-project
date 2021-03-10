import pytesseract
from PIL import Image
import xlsxwriter 
from os import listdir
from os.path import isfile, join
#this logic can processes any ammount of 
data_path="RC\\"        
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
        
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    img = Image.open(image_path)
    text=pytesseract.image_to_string(img,lang="eng")
    text=text.upper()
    print(text)
    print("============================")