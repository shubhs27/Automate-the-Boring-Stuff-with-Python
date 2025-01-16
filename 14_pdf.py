import pypdf

pdfFile= open('meetingminutes1.pdf', 'rb')
reader= pypdf.PdfReader(pdfFile)
print(reader.get_num_pages())

page= reader.get_page(0)
print(page.extract_text())

for i in range(reader.get_num_pages()):
    print(reader.get_page(i).extract_text())
pdfFile.close()


pdf1File= open('meetingminutes1.pdf', 'rb')
pdf2File= open('meetingminutes2.pdf', 'rb')
reader1= pypdf.PdfReader(pdf1File)
reader2= pypdf.PdfReader(pdf2File)

writer= pypdf.PdfWriter()
for i in range (reader1.get_num_pages()):
    page= reader1.get_page(i)
    writer.add_page(page)

for i in range (reader2.get_num_pages()):
    page= reader2.get_page(i)
    writer.add_page(page)

outputFile= open('combinedminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
