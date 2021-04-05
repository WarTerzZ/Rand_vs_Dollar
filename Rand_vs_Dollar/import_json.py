from bs4 import BeautifulSoup
from html.parser import HTMLParser
import urllib, json
from urllib.request import urlopen

#url = "https://www.exchangerates.org.uk/USD-ZAR-exchange-rate-history.html"

#response = urllib.request.urlopen(url).read().decode()

## data = json.loads(response)

#print('\n' + response)


#url = "https://engineering.buffalo.edu/"
#url = url + "computer-science-engineering.html"
#response = urllib.request.urlopen(url)
#content = response.read().decode()
#print(content)

url = "https://www.exchangerates.org.uk/USD-ZAR-exchange-rate-history.html"
response = urllib.request.urlopen(url)
content = response.read().decode()
print(content)

Html_file= open("./content.html","w")
Html_file.write(content)
Html_file.close()

# <tr class="colone"><td>Sunday 21 March 2021</td><td>1 USD = 14.825 ZAR</td><td><a href="/USD-ZAR-21_03_2021-exchange-rate-history.html">USD ZAR rate for 21/03/2021</a></td></tr>

def find_tr_tags():
    tr_tags = soup.find('tr', class_='colone')
    return tr_tags

def find_tr_tags_1():
    tr_tags = soup.find('tr', class_='coltwo')
    return tr_tags

def find_td_tags():
    td_tags = tr_tags.find_all('td')
    return td_tags

def find_td_tags_1():
    td_tags = tr_tags.find_all('td')
    return td_tags

with open('./content.html') as fp:
    soup = BeautifulSoup(fp, "html.parser")
    titl = soup.head.title
    div_result = soup.find(id="hd-maintable")
    print(div_result.prettify())
    h2_class_block = soup.find('h2', class_='block')
    print(h2_class_block.prettify())
    
    td_tags = []
    tr_tags = ''

    tr_tags = find_tr_tags()
    print(tr_tags)
    print('\n')

    td_tags = find_td_tags()
    print(td_tags)
    print('\n')

    td_tags = find_td_tags()
    print(td_tags[1])
    print(type(td_tags[1]))
    print('\n')

    RnD_Val = []
    paragraph = []
    RnD_Date = []

    for x in td_tags[1]:
        paragraph.append(str(x))
        print(paragraph)
        print('\n')

    RnD_Val = paragraph[0][8:14]
    print(RnD_Val)

    for x in td_tags[0]:
        paragraph.append(str(x))

    RnD_Date = paragraph[1][8:23]
    print(RnD_Date)
