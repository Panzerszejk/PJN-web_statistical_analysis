from bs4 import BeautifulSoup
import ssl
from urllib.request import Request, urlopen
from pathlib import Path

def get_post_content(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    context = ssl._create_unverified_context()
    webpage = urlopen(req, context=context).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    text = ""
    for article in soup.find_all('article'):
        for description in article.find_all("p", {'itemprop': 'description'}):
            text += description.getText()
        for descriptioncnt in article.find_all("div", {'id': 'game-description-cnt'}):
            for paragraph in descriptioncnt.find_all("p"):
                text += "\n" + paragraph.getText()
    #for line in soup.select('#wrap')[0].getText().splitlines():
    #    if line is not '':
    #        text += "\n" + line
    return text


def get_posts(start, end):
    posts = []
    for pageNumber in range(start, end+1):
        print(pageNumber)
        req = Request('https://www.gry-online.pl/gry/22-' + str(pageNumber), headers={'User-Agent': 'Mozilla/5.0'})
        context = ssl._create_unverified_context()
        webpage = urlopen(req, context=context).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for div in soup.find_all("div", {'class': 'lista-gry'}):
            for box in div.find_all("div", {'class': 'box'}):
                posts.append('https://www.gry-online.pl' + box.a['href'])
    return posts


#print(get_posts(1, 1))
#print(get_post_content("https://www.gry-online.pl/gry/soulcalibur-vi/zc50dc"))
for post in get_posts(1, 854):
    print(post)
    if not Path('posts/' + post.split('/')[4] + '.txt').exists():
        with open('posts/' + post.split('/')[4] + '.txt', 'w') as f:
            f.write(get_post_content(post))
