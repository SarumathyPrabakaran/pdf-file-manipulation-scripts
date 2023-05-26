#images are converted to a single pdf.

import os
import img2pdf

name = "name.pdf"

with open(name,"wb") as f:
    f.write(img2pdf.convert(["Screenshot from 2023-04-07 11-45-27.png","Screenshot from 2023-05-16 12-45-38.png","aadhar-SarumathyP.jpg"]))


file_size = os.path.getsize(name)
file_size_kb = file_size / 1024
print(f"Size of {name}: {file_size_kb:.2f} KB")
