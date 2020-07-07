#! python3
# Downloads XKCD comics

import requests, os, bs4 as bs

url = str(input("What image would you like to download: "))
req = requests.get(url)

#8665642262
imageFile = open(os.path.join('pictures', os.path.basename(url)), 'wb')

for chunk in req.iter_content(100000):
    imageFile.write(chunk)

imageFile.close()
