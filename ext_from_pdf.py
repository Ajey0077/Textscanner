from PyPDF2 import PdfFileReader,PdfFileWriter


#pdf location
a=input("enter pdf location with type : ")

pdf=PdfFileReader(a)

with open("lec.txt","w") as f:
    for page_num in range(pdf.numPages):
        print(f"page : {page_num}")
        pageobj=pdf.getPage(page_num)

        try:
            txt= pageobj.extractText()           # extracting text from single page
            print(''.center(100,"-"))     
        except:
            pass
        else:
            f.write(f"page {page_num+1}\n")               # page indexing
            f.write("".center(100,"-"))    
            f.write(txt)
    f.close()