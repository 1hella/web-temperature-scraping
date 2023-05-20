import requests
import selectorlib
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36'
}

connection = sqlite3.connect("data.db")


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['temperature']
    return value


def store(timestamp, temp):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures values (?,?)", (timestamp, temp))
    connection.commit()


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        temp = extract(scraped)
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        print(timestamp, temp)
        store(timestamp, temp)
        time.sleep(2)
