#This code is developed by Priyansh Gupta
#git hub: https://github.com/priyansh-gupta
#linkden: https://www.linkedin.com/in/priyansh-gupta-59b989172/

#i have used tesseract api for OCR of a given image
import pytesseract   
from PIL import Image
import xlsxwriter    #this librabry is used to convert any text into xlsx type using python
from os import listdir
from os.path import isfile, join

workbook = xlsxwriter.Workbook('OCR.xlsx') #name of xlsx file 
worksheet = workbook.add_worksheet()

#specify the ocaton of training dataset
data_path="RC\\"        
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

#function to input data to xlsx file
#using python concepts to get required data
def put(row,col,word,text):
        end='\n'
        content= (text.split(word))[1].split(end)[0]
        worksheet.write(row,col,content)

#specifying the column name of xlsx file
worksheet.write(0,0,'NAME')
worksheet.write(0,1,'REGN.NO')
worksheet.write(0,2,'CHASIS.NO')
worksheet.write(0,3,'REGN.DATE')
worksheet.write(0,4,'ENO')
row=1
col=0
#python logic to load every image from the given dataset 
#thus code will load any no of images given to the dataset
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    img = Image.open(image_path)
    #perform OCR of image and get output of type string                )
    text=pytesseract.image_to_string(img,lang="eng")  
    text=text.upper()  #convert to uppercase so as to avoid confusion b/w Name and NAME        
    try:
        if 'NAME :' in text:           
            word= 'NAME :'
            put(row,col,word,text)
        elif "OWNER'S NAME" in text:
            word="OWNER'S NAME"
            put(row,col,word,text)
        elif 'NAME _:' in text:   
            word='NAME _:'
            put(row,col,word,text)
        ########################
        if 'REGN . NO :' in text:
            word='REGN . NO :'
            put(row,col+1,word,text)
        elif 'REGISTRATION NO.' in text:
            word='REGISTRATION NO.'
            put(row,col+1,word,text)
        #######################
        if 'CH. NO : ' in text:
            word='CH. NO : '
            put(row,col+2,word,text)
        elif 'CH.NO :' in text:
            word='CH.NO :'
            put(row,col+2,word,text)
        ############################
        if 'REG. DT:' in text:
            word='REG. DT:'
            put(row,col+3,word,text)
        #############################    
        if 'ENO =:' in text:
            word='ENO =:'
            put(row,col+4,word,text)
        
    except:
        worksheet.write(row,col,'nil')
        worksheet.write(row,col+1,'nil')
        worksheet.write(row,col+2,'nil')
        worksheet.write(row,col+3,'nil')
        worksheet.write(row,col+4,'nil')
        
    row+=1  
workbook.close()
#we have to close the xlsx file after writing                     
    

    
