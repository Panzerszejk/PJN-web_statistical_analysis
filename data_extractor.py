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
            btn_a = btn.find('a')
            if btn_a:
                nextpage = btn.a['href']
                nexturl= url.split('?') # strony wystepuja 2 odmianach więc na sztywno nie przypisze a link zawiera tylko końcowkę zaczynając od '?'
                req = Request(nexturl[0]+nextpage, headers={'User-Agent': 'Mozilla/5.0'})
                print('     '+nexturl[0]+nextpage)
                context = ssl._create_unverified_context()
                webpage = urlopen(req, context=context).read()
                soup = BeautifulSoup(webpage, 'html.parser')
            else:
                break
        else:
            break
    return text

def get_post_content3(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    context = ssl._create_unverified_context()
    webpage = urlopen(req, context=context).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    text = ""

    while True:
        for article in soup.find_all('article', {'class': 'word-txt'}):
            for paragraph in article.find_all("p",recursive=False):
                text += "\n" + paragraph.getText()

        btn = soup.find('nav', {'class': 'guide16-next-prev'})
        if btn:
            btn_a = btn.find('a', {'class': 'g16np-right'})
            if btn_a:
                nextpage = btn.a['href'].split('&')
                req = Request(url+'&'+nextpage[1], headers={'User-Agent': 'Mozilla/5.0'})
                print('     '+url+'&'+nextpage[1])
                context = ssl._create_unverified_context()
                webpage = urlopen(req, context=context).read()
                soup = BeautifulSoup(webpage, 'html.parser')
            else:
                break
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
                post = []
                if box.a['href'][0] == '/': #czasami linki zaczynaja sie od / a czasami nie
                    post.append('https://www.gry-online.pl' + box.a['href'])
                else:
                    post.append('https://www.gry-online.pl/' + box.a['href'])
                header = box.find('h5')
                shortHeader= header.string.split('–')[0]
                post.append(shortHeader)
                posts.append(post)
    return posts


def get_posts_guide(start, end, page):
    posts = []
    for pageNumber in range(start, end+1):
        print(pageNumber)
        req = Request(page + str(pageNumber), headers={'User-Agent': 'Mozilla/5.0'})
        context = ssl._create_unverified_context()
        webpage = urlopen(req, context=context).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for div in soup.find_all("div", {'class': 'gp-main16-list c-size'}):
            for box in div.find_all("a", {'class': 'gp16-box-2'}):
                post = []
                post.append('https://www.gry-online.pl' + box['href'])
                header = box.h4.string
                post.append(header)
                posts.append(post)
    return posts


# for post in get_posts(1, 1, 'https://www.gry-online.pl/gry/22-','lista-gry'): #854 ostatnia strona
#     print(post[1])
#     print(post[0])
#     if not Path('posts/' + post[1] + '.txt').exists():
#         with open('posts/' + post[1] + '.txt', 'w') as f:
#             f.write(get_post_content(post[0]))
# #
# for post in get_posts(1, 1, 'https://www.gry-online.pl/recenzje-gier.asp?STR=','lista'): #121 ostatnia strona
#     print(post[1])
#     print(post[0])
#     if not Path('posts/' + post[1] + '.txt').exists():
#         with open('posts/' + post[1] + '.txt', 'w') as f:
#             f.write(get_post_content2(post[0]))
#
# for post in get_posts(1, 1, 'https://www.gry-online.pl/gry-przed-premiera.asp?STR=','lista'): #5 ostatnia strona
#     print(post[1])
#     print(post[0])
#     if not Path('posts/' + post[1] + '.txt').exists():
#         with open('posts/' + post[1] + '.txt', 'w') as f:
#             f.write(get_post_content2(post[0]))

# for post in get_posts(2014, 2014, 'https://www.gry-online.pl/S017.asp?ROK=','lista'): #2014-2018 ostatnia strona
#         print(post[1])
#         print(post[0])
#         if not Path('posts/' + post[1] + '.txt').exists():
#             with open('posts/' + post[1] + '.txt', 'w') as f:
#                 f.write(get_post_content2(post[0]))

for post in get_posts_guide(1,1,'https://www.gry-online.pl/poradniki-do-gier.asp?SOR=1&STR='): #83 ostatnia strona
        print(post[1])
        print(post[0])
        if not Path('posts/' + post[1] + '.txt').exists():
            with open('posts/' + post[1] + '.txt', 'w') as f:
                f.write(get_post_content3(post[0]))



# print(get_posts_guide(4,4,'https://www.gry-online.pl/poradniki-do-gier.asp?SOR=1&STR='))
# print(get_post_content3('https://www.gry-online.pl/S024.asp?ID=1907'))
#print(get_post_content2('https://www.gry-online.pl/S020.asp?ID=13040 '))
#print(get_post_content2('https://www.gry-online.pl/S020.asp?ID=1366')) #bez stron
#print(get_post_content('https://www.gry-online.pl/gry/red-dead-redemption-ii/zb4a0f'))
