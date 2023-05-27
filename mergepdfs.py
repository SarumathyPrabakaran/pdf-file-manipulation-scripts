#MERGE ALL PDFS INTO SINGLE PDF

from PyPDF2 import PdfMerger
import os

merger  = PdfMerger()

name = "merged_pdf_file_name.pdf"

pdfs = ['file2.pdf','file3.pdf']

for pdf in pdfs:
    merger.append(pdf)


#merger.merge(1,"my_file1.pdf") 

merger.write(name)

file_size = os.path.getsize(name)
file_size_kb = file_size / 1024
print(f"Size of {name}: {file_size_kb:.2f} KB")

merger.close()


 
# merger.append(pdf, pages=(0, 3))    # first 3 pages
# merger.append(pdf, pages=(0, 6, 2)) # pages 1,3, 5
 #                        like range() 
