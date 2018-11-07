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

def get_post_content2(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    context = ssl._create_unverified_context()
    webpage = urlopen(req, context=context).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    text = ""

    while True:
        for article in soup.find_all('article', {'class': 'word-txt'}):
            for paragraph in article.find_all("p",recursive=False):
                text += "\n" + paragraph.getText()

        btn = soup.find('div', {'class': 'np-right'})
        if btn:
            nextpage=btn.a['href']
            nexturl= url.split('?') # strony wystepuja 2 odmianach więc na sztywno nie przypisze a link zawiera tylko końcowkę zaczynając od '?'
            req = Request(nexturl[0]+nextpage, headers={'User-Agent': 'Mozilla/5.0'})
            print('     '+nexturl[0]+nextpage)
            context = ssl._create_unverified_context()
            webpage = urlopen(req, context=context).read()
            soup = BeautifulSoup(webpage, 'html.parser')
        else:
            break

    return text


def get_posts(start, end, page, divname):
    posts = []
    for pageNumber in range(start, end+1):
        print(pageNumber)
        req = Request(page + str(pageNumber), headers={'User-Agent': 'Mozilla/5.0'})
        context = ssl._create_unverified_context()
        webpage = urlopen(req, context=context).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for div in soup.find_all("div", {'class': divname}):
            for box in div.find_all("div", {'class': 'box'}):
                posts.append('https://www.gry-online.pl' + box.a['href'])
    return posts

#print(get_posts(1, 1))
#print(get_post_content("https://www.gry-online.pl/gry/soulcalibur-vi/zc50dc"))
for post in get_posts(1, 854, 'https://www.gry-online.pl/gry/22-','lista-gry'): #854 ostatnia strona
    print(post)
    if not Path('posts/' + post.split('/')[4] + '.txt').exists():
        with open('posts/' + post.split('/')[4] + '.txt', 'w') as f:
            f.write(get_post_content(post))

for post in get_posts(1, 121, 'https://www.gry-online.pl/recenzje-gier.asp?STR=','lista'): #121 ostatnia strona
    print(post)
    if not Path('posts/' + post.split('/')[3] + '.txt').exists():
        with open('posts/' + post.split('/')[3] + '.txt', 'w') as f:
            f.write(get_post_content2(post))

# for post in get_posts(1, 5, 'https://www.gry-online.pl/gry-przed-premiera.asp?STR=','lista'): #5 ostatnia strona, Płatny content
#     print(post)
#     if not Path('posts/' + post.split('/')[3] + '.txt').exists():
#         with open('posts/' + post.split('/')[3] + '.txt', 'w') as f:
#             f.write(get_post_content2(post))

for post in get_posts(2014, 2018, 'https://www.gry-online.pl/S017.asp?ROK=','lista'): #2014-2018 ostatnia strona
    print(post)
    if not Path('posts/' + post.split('/')[3] + '.txt').exists():
        with open('posts/' + post.split('/')[3] + '.txt', 'w') as f:
            f.write(get_post_content2(post))




#print(get_post_content2('https://www.gry-online.pl/S020.asp?ID=13040 '))
#print(get_post_content2('https://www.gry-online.pl/S020.asp?ID=1366')) #bez stron
#print(get_post_content('https://www.gry-online.pl/gry/red-dead-redemption-ii/zb4a0f'))
