import sys
sys.path.append("/usr/home/mint/pdfminer")

import pyPdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from cStringIO import StringIO
import os

def speack(string, language):
    if language == 1:
        uno = 'espeak -v it "'
    else:
        uno = '../main/simple-google-tts/simple_google_tts it "'
    due = string
    tre = '"'

    discorso = uno + due + tre
    discorso = discorso

    os.system(discorso)

def speack_from_pdf(path, language):
    pdf = pyPdf.PdfFileReader(open(path, "rb"))
    fp = file(path, 'rb')
    num_of_pages = pdf.getNumPages()
    for i in range(num_of_pages):
        inside = [i]
        pagenos=set(inside)
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        text = ""
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
            text = retstr.getvalue()

            text = text.decode("utf-8","ignore")
            print('page ' + str(i))
            speack(text, language)

path = "../test.pdf"
speack_from_pdf(path, 0)
    
