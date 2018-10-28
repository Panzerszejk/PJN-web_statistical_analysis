from bs4 import BeautifulSoup
import ssl
from urllib.request import Request, urlopen


def get_post_content(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    context = ssl._create_unverified_context()
    webpage = urlopen(req, context=context).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    text = ""
    for post in soup.find_all('div'):
        if 'class' in post.attrs:
            if 'postcontent' in post['class']:
                for child in post.children:
                    if child.name is not None:
                        if child.name in 'div' and 'class' in child.attrs and 'dolna-ramka' in child['class']:
                            pass
                        elif child.name in 'div' and 'class' in child.attrs and 'thumbnail-wrap' in child['class']:
                            pass
                        elif child.name in 'div' and 'class' in child.attrs and 'wp-caption' in child['class']:
                            pass
                        elif len(child.getText().strip()) == 0:
                            pass
                        else:
                            #print(child)
                            #print(" ".join(child.getText().split()))
                            #text += child.getText().strip()
                            text += " ".join(child.getText().split())
    return text


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


for post in get_posts(1,1):
    with open('posts/'+ post.split('/')[4] + '.txt', 'w') as f:
        f.write(get_post_content(post))
