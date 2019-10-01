import json
import urllib.parse
import requests


def main():
    data_string = '[{"b": [2, 4], "c": 3.0, "a": "A"}]'
    # data_string = "[{'b': [2, 4], 'c': 3.0, 'a': 'A'}]"
    python_data = json.loads(data_string)
    print(f"{data_string}, {type(python_data)}")
    print(f"{python_data[0]['c']}")


def json_google_api():
    google_api_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    input_text = "Cebu City"
    google_api_key = "AIzaSyAK5ViUMNz9x1lV6M2lcWAs-2gbLG6SOEw"
    input_text = google_api_url + "input=" + urllib.parse.quote(input_text, safe='') + "&inputtype=textquery" + "&key=" + google_api_key
    response = requests.get(input_text).json()
    print(f"response:{response}, {type(response)}")
    print(f"response:{response['candidates']}, {type(response['candidates'])}")
    print(f"response:{response['candidates'][0]}, {type(response['candidates'][0])}")
    print(f"response:{response['candidates'][0]['place_id']}, {type(response['candidates'][0]['place_id'])}")


json_google_api()
# main()