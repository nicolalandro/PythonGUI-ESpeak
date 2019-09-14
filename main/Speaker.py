import pyPdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from cStringIO import StringIO
import os


def speack(string, speaker, lang='it'):
    if speaker == 1:
        uno = 'espeak -v %s "' % lang
    else:
        uno = './simple-google-tts/simple_google_tts %s "' % lang
    due = string
    tre = '"'

    discorso = uno + due + tre
    discorso = discorso

    os.system(discorso)


def speack_from_file(string, speaker, lang='it'):
    if speaker == 1:
        uno = 'espeak -v %s -f "' % lang
        tre = '"'
    else:
        uno = './simple-google-tts/simple_google_tts %s ' % lang
        tre = ''
    due = string

    discorso = uno + due + tre
    discorso = discorso

    os.system(discorso)

def speack_from_pdf(path, speaker, lang, print_function):
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

            text = text.decode("ascii","ignore")
            print_function('page ' + str(i))
            speack(text, speaker, lang)
        
