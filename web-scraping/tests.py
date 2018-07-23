from web-scraping import simple_get

## Probamos el simple_get

raw_html = simple_get('https://realpython.com/blog/')
print(len(raw_html))

no_html = simple_get('https://realpython.com/blog/nope-not-gonna-find-it')
if no_html is None:
    print("True")

## Prueba 2: parseo de html

html_pelado = open('iamthewalrus.html').read()
html = BeautifulSoup(html_pelado, 'html.parser')
for p in html.select('p'):
    if p['id'] == 'walrus':
        print(p.text)

## Probamos parseo de listas:
mathmen = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(mathmen, 'html.parser')
for i, li in enumerate(html.select('li')):
    print(i, li.text)
