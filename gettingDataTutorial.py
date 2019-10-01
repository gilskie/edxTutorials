import requests


def main():
    sample_url = "https://en.wikipedia.org/wiki/main_page"
    search_string2 = "Did you know"
    search_string1 = "Did you kn0w"

    response = requests.get(sample_url)
    response.content.decode("utf-8")
    print(f"Info: Accessing '{sample_url}'")

    if response.status_code == 200:
        print(f"Info: Access confirmed! Checking for search string '{search_string1}'")
        # print(response.text.find(search_string))
        if response.text.find(search_string1) > 0:
            print(f"Info: Success! '{search_string1}' could be found at '{sample_url}'.")
        else:
            print(f"Error: Unable to find '{search_string1}'  at '{sample_url}'")
    else:
        print(f"Error: URL '{sample_url}' could not be found!")


main()