import requests
import WebServerClass
from bs4 import BeautifulSoup


def main():
    wikipedia_login_page = 'https://en.wikipedia.org/w/index.php?title=Special:UserLogin'
    username = 'Gilskie1989'
    password = '201127@Gil'

    user_details = [WebServerClass.login_info(username, password)]

    # accessing a variable from class!
    # user_details[0].__dict__['wpName1'] etc...

    get_login_token(user_details, wikipedia_login_page,
                                 user_details[0].__dict__['wpName'],
                                 user_details[0].__dict__['wpPassword'])

    # print(f"token: {user_details[0].__dict__['wpLoginToken']}")
    create_request_session(user_details, wikipedia_login_page)


def create_request_session(user_details, login_page):
    wikipedia_watchlist = 'https://en.wikipedia.org/wiki/Special:Watchlist'

    with requests.session() as session:
        response = session.get(login_page)
        # print(f"response:{response}")
        # breakpoint()
        response_post = session.post(login_page, data=user_details[0].__dict__)

        watchlist_response = session.get(wikipedia_watchlist)
        print(watchlist_response.content.decode('utf-8'))



def get_login_token(user_details, url_page, username, password):
    response = requests.get(url_page)
    response.content.decode('utf-8')

    if response.status_code == 200:
        page_soup = BeautifulSoup(response.content, 'lxml')
        user_details[0].__dict__['wpLoginToken'] = page_soup.find('input', {'name':'wpLoginToken'}).get('value')


main()