from bs4 import BeautifulSoup
import ssl
from urllib.request import Request, urlopen

pageNumber = 1
req = Request('https://zaufanatrzeciastrona.pl/page/' + str(pageNumber), headers={'User-Agent': 'Mozilla/5.0'})
context = ssl._create_unverified_context()
webpage = urlopen(req, context=context).read()
soup = BeautifulSoup(webpage, 'html.parser')

for post in soup.find_all('div'):
    if 'class' in post.attrs:
        if 'thumbnail-wrap' in post['class']:
            print(post.a['href'])
            #get_post_content(post.a['href'])

