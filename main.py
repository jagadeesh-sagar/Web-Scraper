import requests
import selectorlib
from send_email import my_send_email


URL="https://programmer100.pythonanywhere.com/tours/"
HEADERS=HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrap(URL):
    """scrap the page source from the URL"""
    response=requests.get(URL,headers=HEADERS)
    source=response.text
    return source


def extract(source):
    extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
    value=extractor.extract(source)["tours"]
    return value

def store(extracted):
    with open("data.txt","a") as file:
        file.write(extracted+"\n")


if __name__=="__main__":
    while True:
        scraped=scrap(URL)
        extracted=extract(scraped).lower()
        print(extracted)

        if extracted != "no upcoming tours" and extracted not in open("data.txt").read():
            store(extracted)
            my_send_email(extracted)




