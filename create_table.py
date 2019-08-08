from tabulate import tabulate
from pdf2image import convert_from_path
import os

def createtable(data, headers):
    table = tabulate(data, headers, "latex")
    f = open("table.tex", "w+")
    f.write("\\documentclass[12pt]{beamer} \n")
    f.write("\\begin{document} \n")    
    f.write(table)
    f.write("\n \\end\{document\}")

    os.system("pdflatex table.tex")

    pages = convert_from_path("table.pdf")
    pages[1].save('table.png', 'PNG')

if __name__ =='__main__':
    data = [[1,2,3],[5,6,7]]
    headers = ["a","b", "c"]
    createtable(data, headers)