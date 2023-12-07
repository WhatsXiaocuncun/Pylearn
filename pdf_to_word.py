import os
from pdf2docx import Converter
def pdf_docx():
    file_path=r'C:\Users\xiaocuncun\Desktop\pdf_path'
    for file in os.listdir(file_path):
        suff_name=os.path.splitext(file)[1]
        if suff_name !='.pdf':
            continue
        file_name=os.path.splitext(file)[0]
        pdf_name=file_path+'\\'+file
        docx_name=file_path+'\\'+file_name+'.docx'
        cv=Converter(pdf_name)
        cv.convert(docx_name)
        cv.close()

if __name__=='__main__':
    pdf_docx()
