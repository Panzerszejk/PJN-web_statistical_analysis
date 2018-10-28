from bs4 import BeautifulSoup
import ssl
from urllib.request import Request, urlopen


def get_post_content():
    req = Request('https://zaufanatrzeciastrona.pl/post/praca-czeka-na-czlowieka-ciekawa-firma-zaprasza/', headers={'User-Agent': 'Mozilla/5.0'})
    context = ssl._create_unverified_context()
    webpage = urlopen(req, context=context).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    for post in soup.find_all('div'):
        if 'class' in post.attrs:
            if 'postcontent' in post['class']:
                for child in post.children:
                    print(child)


def get_posts(start, end):
    for pageNumber in range(start, end+1):
        req = Request('https://zaufanatrzeciastrona.pl/page/' + str(pageNumber), headers={'User-Agent': 'Mozilla/5.0'})
        context = ssl._create_unverified_context()
        webpage = urlopen(req, context=context).read()
        soup = BeautifulSoup(webpage, 'html.parser')
        posts = []
        for post in soup.find_all('div'):
            if 'class' in post.attrs:
                if 'thumbnail-wrap' in post['class']:
                    #print(post.a['href'])
                    posts.append(post.a['href'])
        return posts


#print(get_posts(1, 1))
get_post_content()