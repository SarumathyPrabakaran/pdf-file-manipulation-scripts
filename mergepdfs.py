
#MERGE ALL PDFS INTO SINGLE PDF




from PyPDF2 import PdfMerger
import os

merger  = PdfMerger()

pdfs = ['Coursera azure.pdf','Coursera Github.pdf','Coursera Docker.pdf']

for pdf in pdfs:
    merger.append(pdf)

merger.write('certs.pdf')


file_size = os.path.getsize(f'certs.pdf')
file_size_kb = file_size / 1024
print(f"Size of {f'certs.pdf'}: {file_size_kb:.2f} KB")


merger.close()


# merger.merge(2,pdf)  ==> instead of append
# merger.append(pdf, pages=(0, 3))    # first 3 pages
# merger.append(pdf, pages=(0, 6, 2)) # pages 1,3, 5
 #                        like range() 
