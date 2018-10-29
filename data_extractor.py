from bs4 import BeautifulSoup
import ssl
from urllib.request import Request, urlopen
from pathlib import Path

def get_post_content(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    context = ssl._create_unverified_context()
    webpage = urlopen(req, context=context).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    for div in soup.find_all("div", {'class': 'dolna-ramka'}):
        div.decompose()
    for div in soup.find_all("div", {'class': 'sidebar-box-wrap'}):
        div.decompose()
    for div in soup.find_all("div", {'id': 'comment-wrap'}):
        div.decompose()
    for div in soup.find_all("div", {'class': 'breadcrumbs'}):
        div.decompose()
    for div in soup.find_all("div", {'id': 'copyright'}):
        div.decompose()
    for div in soup.find_all("ul", {'class': 'breadcrumbs'}):
        div.decompose()
    text = ""
    for line in soup.select('#wrap')[0].getText().splitlines():
        if line is not '':
            text += "\n" + line
    return text


def get_posts(start, end):
    posts = []
    for pageNumber in range(start, end+1):
        req = Request('https://zaufanatrzeciastrona.pl/page/' + str(pageNumber), headers={'User-Agent': 'Mozilla/5.0'})
        context = ssl._create_unverified_context()
        webpage = urlopen(req, context=context).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for post in soup.find_all('div'):
            if 'class' in post.attrs:
                if 'thumbnail-wrap' in post['class']:
                    posts.append(post.a['href'])
        print(pageNumber)
    return posts


#print(get_post_content("https://zaufanatrzeciastrona.pl/post/przed-nami-advanced-threat-summit-2018-a-dla-was-kod-rabatowy/"))
for post in get_posts(1, 20):
    print(post)
    if not Path('posts/' + post.split('/')[4] + '.txt').exists():
        print("file don't exist")
        with open('posts/' + post.split('/')[4] + '.txt', 'w') as f:
            f.write(get_post_content(post))
    else:
        print("file exist")
