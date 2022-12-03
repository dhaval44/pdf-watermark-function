import PyPDF2
import sys

# Combine PDF
input = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('combine.pdf')
        
pdf_combiner(input)

# PDF Function
#with open('./pdf/dummy.pdf','rb') as file:
    #reader = PyPDF2.PdfFileReader(file)
    #print(reader.getPage(0))
    
    #page = reader.getPage(0)
    #page.rotateCounterClockwise(90)
    
    #writer = PyPDF2.PdfFileWriter()
    #writer.addPage(page)
    #with open('dummy_rotate.pdf','wb') as new_file:
        #writer.write(new_file)