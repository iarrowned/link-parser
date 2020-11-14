import requests
from bs4 import BeautifulSoup
from auth import auth, header
from urls import *
from post_parse import post_parser
from myself import parse_page
from urls import links

session = requests.Session()
auth(session)

for i in range(len(links)):
    course_urls.append(parse_page(session, links[i], header))
print(course_urls)
course_urls.append('https://online-edu.mirea.ru/mod/webinars/view.php?id=120592')
#course_urls.append('https://online-edu.mirea.ru/mod/webinars/view.php?id=124872')  -- test раскомментироовать в urls
for j in range(len(course_urls)):
    course_table_ids.append(post_parser(session,header,course_urls[j]))
print(course_table_ids)


def parse(course_url, course_table_id):
    session.get(course_url, headers=header)
    spisok = 'https://online-edu.mirea.ru/mod/webinars/studentTable.php'
    data_table = {
        'idelement': course_table_id
    }
    table = session.post(spisok, data=data_table, headers=header)
    soup = BeautifulSoup(table.text, 'lxml')
    links = []
    for a in soup.find_all('a', href=True):
        links.append(a['href'])

    if len(links)>0:
        return links[0]
        print(links[0])
    else:
        print('Ссылок нет')

lections = []
for i in range(len(course_table_ids)):
    lections.append(str(parse(course_urls[i], course_table_ids[i])))
print(lections)

f = open('output.txt', 'w')
for i in range(len(lections)):
    f.write('{} {} \n'.format(names[i], lections[i]))
f.close()






