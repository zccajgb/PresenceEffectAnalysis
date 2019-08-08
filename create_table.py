from tabulate import tabulate
from pdf2image import convert_from_path
from pylatex import Document, NoEscape
import subprocess

def create_table(data, headers):
    table = tabulate(data, headers, "latex")
    
    doc = Document()

    doc.append(NoEscape(table))

    doc.generate_pdf()

    pages = convert_from_path("table.pdf")
    pages[1].save('table.png', 'PNG')

if __name__ =='__main__':
    data = [[1,2,3],[5,6,7]]
    headers = ["a","b", "c"]
    createtable(data, headers)