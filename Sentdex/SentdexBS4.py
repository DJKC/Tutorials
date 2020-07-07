import bs4 as bs
import urllib.request
import pandas as pd
import requests

# He used urllib but I used requests as seen below
# req = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
# soup = bs.BeautifulSoup(req, "lxml")
req = requests.get("https://pythonprogramming.net/parsememcparseface/")
soup = bs.BeautifulSoup(req.text, "html.parser")

# Prints the anchor tag href attribute for tags captured
for url in soup.find('a'):
    print(url.get("href"))

###################################################

# table = soup.table # same result as soup.find("table")
table = soup.find("table")
table_rows = table.find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text for i in td]
    print("row: ", row)

###################################################

# The same results can be accomplished with the pandas library
# Sets the header to the first row
dfs = pd.read_html("https://pythonprogramming.net/parsememcparseface/", header = 0)

for df in dfs:
    print(df)

###################################################

# XML parsing now, gets url from sitemap
req = requests.get("https://pythonprogramming.net/sitemap.xml")
soup = bs.BeautifulSoup(req.text, "xml")

# sitemap urls are in loc tags
for url in soup.find_all("loc"):
    print(url.text)

###################################################
# Credit goes to StackOverflow user Ayanda Khanyile for the below functioning code.
# https://stackoverflow.com/questions/42147601/pyqt4-to-pyqt5-mainframe-deprecated-need-fix-to-load-web-pages
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self.on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print("Load finished")

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

def main():
    page = Page("https://pythonprogramming.net/parsememcparseface/")
    soup = bs.BeautifulSoup(page.html, "html.parser")
    js_test = soup.find('p', {"class": "jstest"})
    print(js_test.text)

if __name__ == "__main__" : main()

# url = "https://pythonprogramming.net/parsememcparseface/"
# client_response = Client(url)
# sauce = client_response.mainFrame().toHtml()
#
# # Javascript parsing
# req = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/")
# soup = bs.BeautifulSoup(req, "lxml")
# js_test = soup.find('p', {"class": "jstest"})
# print(js_test.text)
