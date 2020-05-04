import PyPDF2
import re
import json

student_data = {
    "1. first name" : "lee bong won",
    "2. grade" : "a+, a+, b+",
    "3. age " : "26",
    "4. course" :[
        {
            "major" : "computer system",
            "classes" : [
                "probability",
                "generalized linear model",
                "categorical data analysic"
            ]
        },
        {
            "minor" : "economic"
        }
    ]
}

with open("student_file.json", "w") as json_file:
    json.dump(student_data, json_file)

st_json = json.dumps(student_data, indent = 4)

print(st_json)


pdf_file = open('/home/kernel/Desktop/poster2.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
page_word_list = re.split(' ', page_content)

page_word = []
for word in page_word_list:
    page_word.append(re.split('\n', word))
print(page_word)
print(number_of_pages)