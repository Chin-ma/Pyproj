import PyPDF2

pdfFileObj = open('22319 - DBMS_FC.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages 
116
pageObj = pdfReader.getPage(0)
pageObj.extractText()