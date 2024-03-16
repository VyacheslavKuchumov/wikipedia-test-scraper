import random
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from dbConnection import wiki_money_collection, wiki_review_collection




# enable headless mode in Selenium
options = Options()
#options.add_argument('--headless=new')

driver = webdriver.Chrome(
    options=options,
    # other properties...
)

print("Getting the page...")

driver.get('https://en.wikipedia.org/wiki/List_of_Pixar_films')

# scraping logic...

soup = BeautifulSoup(driver.page_source, 'lxml')

print("Scraping...")

tables = soup.find_all('table', {'class':'wikitable plainrowheaders sortable jquery-tablesorter'})


reviews = tables[3]

reviewsTableRows = reviews.find_next('tbody').find_all_next('tr')




for row in reviewsTableRows:
    row = row.text.replace("\xa0", " ").split("\n")
    name = row[1]
    rottenTomatoes = row[3].split("[")[0]
    metacritic = row[5].split("[")[0]
    cinemaScore = row[7].split("[")[0]
    data = {
        "name": name,
        "rottenTomatoes": rottenTomatoes,
        "metacritic": metacritic,
        "cinemaScore": cinemaScore
        }
    wiki_review_collection.insert_one(data)

driver.quit()







