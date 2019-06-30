import sys
sys.path.append("/usr/home/mint/pdfminer")

import pyPdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from cStringIO import StringIO
from Speaker import speack

# path = "./SistemiDistribuiti.pdf"
path = "domande_tom.pdf"
pdf = pyPdf.PdfFileReader(open(path, "rb"))
fp = file(path, 'rb')
num_of_pages = pdf.getNumPages()
extract = ""
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
  if i >= 0: #i >= 69:
      for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
        text = retstr.getvalue()

        text = text.decode("utf-8","ignore")
        print('page ' + str(i))
        speack(text, 0)
    
