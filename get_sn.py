
# importing required modules
import PyPDF2
import re
import os

path = "C:/py/WBB QR/03-09/"
dir_list = os.listdir(path)
 
print("")

for pdf in dir_list:
    print(pdf)
    print("-------------------------------------")
    # creating a pdf file object
    pdfFileObj = open(path+pdf, 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    
    # printing number of pages in pdf file

    for i in range(len(pdfReader.pages)):
        # creating a page object
        pageObj = pdfReader.pages[i]
        
        # extracting text from page
        text = pageObj.extract_text()
        for m in re.finditer('5-1-06', text):
            print(text[m.start():m.start()+19])
    
    # closing the pdf file object
    pdfFileObj.close()
    print("")