#pdf to images

from pdf2image import convert_from_path
import os

name = 'your_pdf_name.pdf'
pages = convert_from_path(name, 200)

i=1
for page in pages:
    page.save(f'output_image{i}.jpg', 'JPEG')
    
    file_size = os.path.getsize(f'out{i}.jpg')
    file_size_kb = file_size / 1024
    print(f"Size of {f'output_image{i}.jpg'}: {file_size_kb:.2f} KB")
    i+=1






