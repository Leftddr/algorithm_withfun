from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

path = '../Desktop/example.pdf'

rsrcmgr = PDFResourceManager
retstr = StringIO()
codec = 'utf-8'
laparams = LAParams()

fp = open('./out.html', 'wb')
device = HTMLConverter(rsrcmgr, fp, codec = codec, laparams = laparams)

rp = open(path, 'wb')
interpreter = PDFPageInterpreter(rsrcmgr, device)
password = ''
maxpages = 0
caching = True
pagenos = set()
for page in PDFPage.get_pages(rp, pagenos, maxpages = maxpages, password = password,
caching = caching, check_extractable = True):
    interpreter.process_page(page)
rp.close()
device.close()
str = retstr.getvalue()
retstr.close()
fp.close()