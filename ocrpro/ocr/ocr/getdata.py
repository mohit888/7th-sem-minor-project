def ImageView(request):
        if request.method == 'POST':
            form =  ImageForm(request.POST, request.FILES)
            if form.is_valid():
                image = request.FILES['image']
                print(image)
                loc = ("OCR.xlsx")          
                wb = xl.open_workbook(loc)             
                s1 = wb.sheet_by_index(0)                     
                s1.cell_value(0,0)                             
                row = s1.nrows + 1
                img = Image.open(image)
                text=pytesseract.image_to_string(img,lang="eng")  
                text=text.upper()      
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

                    if 'REGN . NO :' in text:
                        word='REGN . NO :'
                        put(row,col+1,word,text)
                    elif 'REGISTRATION NO.' in text:
                        word='REGISTRATION NO.'
                        put(row,col+1,word,text)

                    if 'CH. NO : ' in text:
                        word='CH. NO : '
                        put(row,col+2,word,text)
                    elif 'CH.NO :' in text:
                        word='CH.NO :'
                        put(row,col+2,word,text)
                    if 'REG. DT:' in text:
                        word='REG. DT:'
                        put(row,col+3,word,text)  
                    if 'ENO =:' in text:
                        word='ENO =:'
                        put(row,col+4,word,text)
                    
                except:
                    worksheet.write(row,col,'nil')
                    worksheet.write(row,col+1,'nil')
                    worksheet.write(row,col+2,'nil')
                    worksheet.write(row,col+3,'nil')
                    worksheet.write(row,col+4,'nil')
                    
                workbook.close()
                form = ImageForm()
                context = {'form': form,'image':image}
                return render(request, 'index3.html', context)
           
        else:
            form = ImageForm()
        return render(request, 'index3.html', {'form': form})