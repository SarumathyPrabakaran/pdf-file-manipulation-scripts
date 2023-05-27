from PyPDF2 import PdfMerger,PdfReader,PdfWriter
from img2pdf import convert
from pdf2image import convert_from_path
import os
import datetime

POPPLER_PATH = os.path.join(os.getcwd(),r"dependencies\poppler\Library\bin")

def getpdfs():
    file_path = os.path.join(os.getcwd(),"files")
    files = [os.path.join(file_path,file) for file in os.listdir(file_path) if file.endswith(".pdf")]
    return files
def getimgs():
    file_path = os.path.join(os.getcwd(),"files")
    files = [os.path.join(file_path,file) for file in os.listdir(file_path) if (file.endswith(".png") or file.endswith(".jpg"))]
    return files


def merge(out_file=None,in_files=None):
    if not in_files: in_files = getpdfs()
    if not in_files: return 0,"No pdfs to Merge."
    if not out_file:
        d = datetime.datetime.now()
        out_file = f"merged_file_{d.date()}_{d.hour}-{d.minute}-{d.second}.pdf"
        out_file = os.path.join(os.getcwd(),"output",out_file)

    try:
        merger = PdfMerger()
        for pdf in in_files:
            merger.append(pdf)
        merger.write(out_file)
    except Exception as e:
        #print(e)
        return 0,"Unable to Merge."

    return 1,"Files Merged Successfully."

def split(out_file=None,in_file=None,splits=None):
    if not in_file:
        in_file = getpdfs()
        if in_file: in_file = in_file[0]
    if not in_file: return 0,"No PDF to Split."

    if not out_file:
        d = datetime.datetime.now()
        out_file = f"split_pdf_file_{d.date()}_{d.hour}-{d.minute}-{d.second}"
        out_file = os.path.join(os.getcwd(),"output",out_file)
    
    try:
        pdf = PdfReader(in_file)
        if splits:
            #[[1,3],[2,4]]
            for i,split in enumerate(splits):
                pdf_writer = PdfWriter()
                for page_no in split:
                    pdf_writer.add_page(pdf.pages[page_no])
                with open(f"{out_file}_{i}.pdf","wb") as output_pdf:
                    pdf_writer.write(output_pdf)
        else:
            for i,page in enumerate(pdf.pages):
                pdf_writer = PdfWriter()
                pdf_writer.add_page(page)

                with open(f"{out_file}_{i}.pdf","wb") as output_pdf:
                    pdf_writer.write(output_pdf)

    except Exception as e:
        #print(e)
        return 0,"Unable to Split."

    return 1,"PDF Splitted Successfully."

def imgTopdf(out_file=None,in_files=None):
    if not in_files: in_files = getimgs()
    if not in_files: return 0,"No images to convert"
    if not out_file:
        d = datetime.datetime.now()
        out_file = f"converted_imgtopdf_file_{d.date()}_{d.hour}-{d.minute}-{d.second}.pdf"
        out_file = os.path.join(os.getcwd(),"output",out_file)

    try:
        with open(out_file,"wb") as f:
            f.write(convert(in_files))
    except Exception as e:
        #print(e)
        return 0,"Unable to Convert."

    return 1,"Images Converted Successfully."

def pdfToimg(out_file=None,in_file=None):
    if not in_file:
        in_file = getpdfs()
        if in_file: in_file = in_file[0]
    if not in_file: return 0,"No PDF to Convert."

    if not out_file:
        d = datetime.datetime.now()
        out_file = f"converted_pdftoimg_file_{d.date()}_{d.hour}-{d.minute}-{d.second}"
        out_file = os.path.join(os.getcwd(),"output",out_file)
    try:
        pages = convert_from_path(in_file,poppler_path = POPPLER_PATH)
        for i,page in enumerate(pages):
            page.save(f"{out_file}_{i}.jpg","JPEG")
    except Exception as e:
        #print(e)
        return 0,"Unable to Convert."

    return 1,"PDF Converted Successfully."

if __name__ == "__main__":
    print(getpdfs())
    print(getimgs())