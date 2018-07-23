from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                print("Request OK")
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

## Probamos el simple_get

#raw_html = simple_get('https://realpython.com/blog/')
#print(len(raw_html))

#no_html = simple_get('https://realpython.com/blog/nope-not-gonna-find-it')
#if no_html is None:
#    print("True")

## Prueba 2: parseo de html

#html_pelado = open('iamthewalrus.html').read()
#html = BeautifulSoup(html_pelado, 'html.parser')
#for p in html.select('p'):
#    if p['id'] == 'walrus':
#        print(p.text)

mathmen = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(mathmen, 'html.parser')
for i, li in enumerate(html.select('li')):
    print(i, li.text)
