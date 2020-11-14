import requests
from bs4 import BeautifulSoup

def parse_page(session, page_url, header):
    page_info = session.get(page_url, headers=header).text
    cookies_dict = [
        {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
        for key in session.cookies
    ]

    session2 = requests.Session()
    for cookies in cookies_dict:
        session2.cookies.set(**cookies)

    resp = session2.get(page_url, headers=header).text
    #print(resp)
    soup = BeautifulSoup(resp, 'lxml')
    block = soup.find('li', id='section-1')
    links = []
    #print(block)
    for a in block.find_all('a', href=True):
        links.append(a['href'])
    #print(links[-1])
    return links[-1]














