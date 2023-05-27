from PyPDF2 import PdfReader, PdfWriter
import os

def split(path, name_of_split):
    pdf = PdfReader(path)

    # Split PDF into two parts: 2 pages and 1 page
    pdf_part1 = PdfWriter()
    for page in range(2):
        pdf_part1.add_page(pdf.pages[page])

    pdf_part2 = PdfWriter()
    pdf_part2.add_page(pdf.pages[2])

    # Write the split PDFs to separate files
    output1 = f'{name_of_split}_part1.pdf'
    with open(output1, 'wb') as output_pdf1:
        pdf_part1.write(output_pdf1)

    output2 = f'{name_of_split}_part2.pdf'
    with open(output2, 'wb') as output_pdf2:
        pdf_part2.write(output_pdf2)
    
    # Determine the sizes of the split PDF files
    file_size1 = os.path.getsize(output1)
    file_size_kb1 = file_size1 / 1024
    print(f"Size of {output1}: {file_size_kb1:.2f} KB")

    file_size2 = os.path.getsize(output2)
    file_size_kb2 = file_size2 / 1024
    print(f"Size of {output2}: {file_size_kb2:.2f} KB")

if __name__ == '__main__':
    path = 'merged_pdf_file_name.pdf'
    name_of_split = "any_name"
    split(path, name_of_split)