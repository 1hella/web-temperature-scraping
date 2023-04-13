import requests
import selectorlib
import time

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36'
}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['temperature']
    return value


def store(data):
    with open("data.txt", "a") as file:
        file.write(data + "\n")


def read():
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        temp = extract(scraped)
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        formatted = f"{timestamp},{temp}"
        print(formatted)
        store(formatted)
        time.sleep(2)

# assume data.txt exists with headers and there's no data in it, or if there is, append data to it.
