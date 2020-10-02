import generator_main
import generator_gui
from webbrowser import *


"""f = open("generator.html", "w")
f.write("<html>\n <body> \n<h1> Stay tuned for our amazing summer sale! </h1>\n </body> \n</html>")
f.close()

f = open("generator.html", "r")
print(f.read())

webbrowser.open_new_tab("generator.html")
"""

def entry(self):
    htmlFile = open("user.html", "w")
    customEntry = self.txt_one.get()
    htmlFormat = "<html>\n<body>\n<p>" + customEntry + "</p>\n</body>\n</html>"
    htmlFile.write(htmlFormat)
    htmlFile.close()
    webbrowser.open_new_tab("user.html")
    

