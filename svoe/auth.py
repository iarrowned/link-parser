import fake_useragent
user = fake_useragent.UserAgent().random
header = {'user-agent': user}
def auth(session):
    URL ='https://login.mirea.ru/login/'
    csrf_token = session.get(URL).cookies['csrftoken']  # -- Получаем csrf-token      # --
    data = {
        'csrfmiddlewaretoken': csrf_token,
        'login': 'kuznetsov.k.a@edu.mirea.ru',
        'password': 'poiLkJmnb098'
    }
    session.post(URL, data=data, headers=header) # --Происходит авторизация