from PyPDF2 import PdfReader, PdfWriter
import os

def split(path, name_of_split):
    pdf = PdfReader(path)
    for page in range(len(pdf.pages)):

        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page])

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
            
        file_size = os.path.getsize(output)
        file_size_kb = file_size / 1024
        print(f"Size of {output}: {file_size_kb:.2f} KB")



if __name__ == '__main__':
    path = 'certs.pdf'
    split(path, 'cert')