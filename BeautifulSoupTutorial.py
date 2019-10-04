import requests
from bs4 import BeautifulSoup


def main():
    search_text = "egg"
    url = ['https://www.epicurus.com/epicurus-com-search-results/?cx=partner-pub-8686155461235202%3A8524571559&cof=FORID%3A10&ie=UTF-8&q='
        , '&sa=Search&siteurl=www.epicurus.com%2F&ref=www.google.com%2F&ss=192j36864j2']
    new_site = url[0] + search_text + url[1]

    response = requests.get(url[0] + search_text + url[1])
    page_soup = BeautifulSoup(response.content, 'lxml')

    # print(page_soup.prettify())
    style = page_soup.find('li', {'id':'custom_html-13'})
    # print(style)
    children = style.findChildren("div", recursive=False)

    # get_a_tags = page_soup.find_all('a')
    get_a_tags_href_attribute = page_soup.find('a').get('href')
    # print(get_a_tags)
    print(get_a_tags_href_attribute)

    get_div_tags = page_soup.find('div', class_='epicft2').get_text()
    # get_div_tags_2 = page_soup.find('div', {'class':'epicft2'})
    # print(get_div_tags)
    # print(get_div_tags_2)

    # for child in children:
    #     print(child)


main()