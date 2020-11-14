import requests
from bs4 import BeautifulSoup

def post_parser(session, header, course_urls):
    page_info = session.get(course_urls, headers=header).text
    cookies_dict = [
        {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
        for key in session.cookies
    ]

    session2 = requests.Session()
    for cookies in cookies_dict:
        session2.cookies.set(**cookies)

    resp = session2.get(course_urls, headers=header).text
    #print(resp)

    soup = BeautifulSoup(resp, 'lxml')
    datas = []
    script = soup.find_all('script')
    for item in script:
        datas.append(item)
    if len(datas)>12:
        need_script = str(datas[12])
        idelement = need_script[119:130]
        cls = idelement.find("'")
        idelement_finally = idelement[:cls]
        #print(idelement_finally)
    else:
        print('Проверь ссылки')
    return idelement_finally
