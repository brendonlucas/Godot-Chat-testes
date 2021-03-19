import requests


def main():
    # get_profiles_posts()
    # get_um_profile_posts()
    # get_comentarios_do_post()
    # get_um_comentario_do_post()
    # get_posts_comentarios()
    # get_um_post_comentarios()
    # get_informacoes()
    # get_profiles()
    # get_um_profile()
    # get_users()
    # get_um_user()
    # get_posts()
    # get_um_post()
    # pegar_token()
    # postar()
    print()


def get_informacoes():
    url = 'http://127.0.0.1:8000/info/'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        for i in range(len(json)):
            print(json[i])


def get_comentarios_do_post():
    url = 'http://127.0.0.1:8000/posts/3/comments/'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        for i in range(len(json['comments'])):
            print(json['comments'][i])


def get_um_comentario_do_post():
    url = 'http://127.0.0.1:8000/posts/3/comments/3'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        print(json)


def get_profiles_posts():
    url = 'http://127.0.0.1:8000/profile-post/'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        for i in range(len(json)):
            print(json[i])


def get_um_profile_posts():
    url = 'http://127.0.0.1:8000/profile-post/5'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        print(json)


def get_posts_comentarios():
    url = 'http://127.0.0.1:8000/posts-comments/'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        for i in range(len(json)):
            print(json[i])


def get_um_post_comentarios():
    url = 'http://127.0.0.1:8000/posts-comments/1'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        print(json)


def get_profiles():
    url = 'http://127.0.0.1:8000/profile/'
    headers = {'Authorization': 'Token 5a7fcb328f79d9fd53461d040d1a2c41890eef6f'}
    r = requests.get(url, headers=headers)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        for i in range(len(json)):
            print(json[i])


def get_um_profile():
    url = 'http://127.0.0.1:8000/profile/1'
    headers = {'Authorization': 'Token 5a7fcb328f79d9fd53461d040d1a2c41890eef6f'}
    r = requests.get(url, headers=headers)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        print(json)


def get_users():
    url = 'http://127.0.0.1:8000/users/'
    headers = {'Authorization': 'Token 5a7fcb328f79d9fd53461d040d1a2c41890eef6f'}
    r = requests.get(url, headers=headers)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        for i in range(len(json)):
            print(json[i])


def get_um_user():
    url = 'http://127.0.0.1:8000/users/3'
    headers = {'Authorization': 'Token 5a7fcb328f79d9fd53461d040d1a2c41890eef6f'}
    r = requests.get(url, headers=headers)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        print(json)


def get_posts():
    url = 'http://127.0.0.1:8000/posts/'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        for i in range(len(json)):
            print(json[i])


def get_um_post():
    url = 'http://127.0.0.1:8000/posts/5'
    r = requests.get(url)
    print('status code: ', r.status_code)
    if r.status_code == 200:
        json = r.json()
        print(json)


def pegar_token():
    # Pegar token
    body = {"username": "Bret", "password": "123456789"}
    r = requests.post("http://127.0.0.1:8000/api-token-auth/", json=body)
    print(r.json())
    print(r.status_code)


def deletar_cometario():
    # deletar Comentario
    headers = {'Authorization': 'Token 5a7fcb328f79d9fd53461d040d1a2c41890eef6f'}
    r = requests.delete('http://127.0.0.1:8000/posts/3/comments/6/', headers=headers)
    print(r.json())
    print(r.status_code)


def postar():
    # fazer postagem
    body = {
        "title": "Titulo do comentario",
        "body": "corpo do comentario",
    }
    url = 'http://127.0.0.1:8000/posts/'
    headers = {'Authorization': 'Token 5a7fcb328f79d9fd53461d040d1a2c41890eef6f'}
    r = requests.post(url, headers=headers, json=body)
    print(r.json())
    print(r.status_code)


def comentar():
    # fazer postagem de comentario
    body = {
        "name": "Comentario t1",
        "email": "Veronica_Goodwin@timmothy.net",
        "body": "blanditiis quia ut vel ut maiores ea"
    }
    url = 'http://127.0.0.1:8000/posts/3/comments/'
    headers = {'Authorization': 'Token 5a7fcb328f79d9fd53461d040d1a2c41890eef6f'}
    r = requests.post(url, headers=headers, json=body)
    print(r.json())
    print(r.status_code)


if __name__ == '__main__':
    main()
