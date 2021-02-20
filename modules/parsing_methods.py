import fake_useragent, requests
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
session = requests.Session()


def rhymes(word):
    link = f'https://rifme.net/r/{word.lower()}/1'
    headers = header
    try:
        response = session.get(link, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        find_text = soup.find('div', id='rhy').get_text()

        answer = find_text.replace('»', '»\n\n', 1).replace('https://rifme.net/', '').title()
        return answer
    except:
        return "РИФМ НЕТУ"


def epithets(word):
    link = f'https://gufo.me/dict/epithets/{word.lower()}'
    headers = header
    try:
        response = session.get(link, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        find_text = soup.find('article').get_text()

        answer = find_text[0:str(find_text).rindex('Источник:')].strip()
        return answer
    except:
        return "ЭПИТЕТОФ НЕМА"


def synonym(word):
    link = f'https://sinonim.org/s/{word.lower()}'
    headers = header
    answer = []

    try:
        response = session.get(link, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        block = soup.find('table')
        synonyms_with_trash = block.find_all('a', class_="")
        for syn in synonyms_with_trash:
            answer.append(syn.text)
        answer = f"Синонимы слова «{word.upper()}»\r\n{', '.join(answer).title()}"
        return answer
    except:
        return "СИНОНИМОВ НЕТУ"
