import PyPDF2

pdf_fileObj = open('transactions.pdf', 'rb')
pdf_fileReader = PyPDF2.PdfReader(pdf_fileObj)
numberofPages = pdf_fileReader.numPages
page_no = 0

while page_no < numberofPages:
    parsed_Page = [((pdf_fileReader.getPage(page_no)).extractText()).split('\n')]
    with open('parsedresult.txt', 'a') as res:
        for line in parsed_Page:
            res.writelines('\n'.join(line))
    page_no += 1
pdf_fileObj.close()
