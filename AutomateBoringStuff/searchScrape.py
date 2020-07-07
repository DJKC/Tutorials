#! python3
# searchScrape.py - Opens the first x number of search results from a query passed in through the command line

import bs4
import requests
import sys
import webbrowser

# Yandex.fi was chosen because the html is more simple to parse.
# Google, DuckduckGo and Yahoo should be added for an extra challenge

print("Number args: ", len(sys.argv))
# len(sys.argv) returns 0 for 1 arg, returns 1 for 2 args etc
if len(sys.argv) > 1:  # using terminal arguments for search terms
    searchUrl = "https://yandex.fi/search/?text=" + "%20".join(sys.argv[1:])

    # Shows arguemtns used to run program iteration
    count = 0
    for arg in sys.argv:
        print("Arg[" + str(count) + "]: ", sys.argv[count])
        count += 1

elif len(sys.argv) == 1:
    # If user runs from terminal then search terms are chosen for user
    searchUrl = "https://yandex.fi/search/?text=Why%20can%27t%20you%20follow%20instructions%3F&lr=10493"

else:  # Running from the IDE
    searchTerms = str(input("What would you like to search online:")).split(' ')
    searchUrl = "https://yandex.fi/search/?text=" + "%20".join(searchTerms)

try:
    numberTabs = int(input("How many tabs would you like to open: "))
except Exception:
    numberTabs = 3

print("Loading results...")
# Gets the source for the page
req = requests.get(searchUrl)

# Checks to see if the page source was successfully obtained, else exits
if req.status_code != 200:
    raise Exception("Site not reached, now exiting")

# Makes soup from url containing search terms
soup = bs4.BeautifulSoup(req.text, "html.parser")
# The urls we want to choose have the below class attributes
# classList = ["link", "", "", ""]
anchors = soup.find_all("a", {"class": "link" and "i-bem" and "link" and "link_js_inited" and "path__item" and "link_theme_outer"})

# In case user enters many tabs, the amount is limited to amount returned by page
print("The results from:", searchUrl)
if numberTabs > len(anchors):
    numberTabs = len(anchors)

# Prints out page opened and opens with default web browser
# Should add ability to choose browser for an extra challenge
for i in range(numberTabs):
    print('Opening', anchors[i].get("href"))
    webbrowser.open(anchors[i].get("href"))

