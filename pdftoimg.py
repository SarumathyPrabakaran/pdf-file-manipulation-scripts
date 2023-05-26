from pdf2image import convert_from_path
import os

pages = convert_from_path('certs.pdf', 500)

i=1
for page in pages:
    page.save(f'out{i}.jpg', 'JPEG')
    
    file_size = os.path.getsize(f'out{i}.jpg')
    file_size_kb = file_size / 1024
    print(f"Size of {f'out{i}.jpg'}: {file_size_kb:.2f} KB")
    i+=1






