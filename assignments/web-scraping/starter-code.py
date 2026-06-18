import requests
from bs4 import BeautifulSoup

def fetch(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = [t.get_text(strip=True) for t in soup.select('h1, h2, h3')]
    return titles

if __name__ == '__main__':
    sample = fetch('https://example.com')
    print(parse(sample))
