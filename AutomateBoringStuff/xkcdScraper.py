#! python3
# downloadXkcd.py downloads every single XKCD comic.

import requests, os, bs4 as bs

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok = True) # If the folder exists, throw no error

while not url.endswith('#'):
    print('Downloading image from: %s.' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000): # I usually see this as 1024
            imageFile.write(chunk)

        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
