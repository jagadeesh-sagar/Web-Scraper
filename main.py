import time
import requests
import selectorlib
import sqlite3
from send_email import my_send_email


URL="https://programmer100.pythonanywhere.com/tours/"
HEADERS=HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:

    def scrape(self, URL):
        """scrap the page source from the URL"""
        response=requests.get(URL,headers=HEADERS)
        source=response.text
        return source

    def extract(self,source):
        extractor=selectorlib.Extractor.from_yaml_file("extract.yaml")
        value=extractor.extract(source)["tours"]
        return value

class Database:

    def __init__(self):
        self.connection = sqlite3.connect("data.db")

    def store(self,extracted):
        row=extracted.split(",")
        row=[item.strip() for item in row]
        band,city,date = row
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)",(band, city, date))
        connection.commit()

    def read(self,extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",(band,city,date))
        rows = cursor.fetchall()
        return rows

    def __del__(self):
        self.connection.close()


if __name__=="__main__":
    while True:
        event=Event()
        databases=Database()
        scraped=event.scrape(URL)
        extracted=event.extract(scraped).lower()
        print(extracted)
        if extracted != "no upcoming tours" :
            content = databases.read(extracted)
            if not content:
                databases.store(extracted)
                print("jaggu")
        time.sleep(2)




