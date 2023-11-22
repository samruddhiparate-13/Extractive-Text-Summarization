from bs4 import BeautifulSoup
import requests

def getData(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all(['h1', 'p'])


    text = [result.text for result in results]
    article = ' '.join(text)
    print(article)
    return article