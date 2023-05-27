#images are converted to a single pdf.

import os
import img2pdf

name = "your_pdf_name.pdf"
images = ["out1.jpg","out2.jpg", "out3.jpg"]

with open(name,"wb") as f:
    f.write(img2pdf.convert(images))

file_size = os.path.getsize(name)
file_size_kb = file_size / 1024
print(f"Size of {name}: {file_size_kb:.2f} KB")

