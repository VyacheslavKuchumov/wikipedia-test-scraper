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

money = tables[2]


moneyTableRows = money.find_next('tbody').find_all_next('tr')

for row in moneyTableRows:
    row = row.text.replace("\xa0", " ").split("\n")
    date = row[1]
    name = row[3]
    budget = row[5]
    revenue = row[11]
    data = {
        "date": date,
        "name": name,
        "budget": budget,
        "revenue": revenue
        }
    wiki_money_collection.insert_one(data)



# for table in tables:
#     print(table.text)
    # job = jobBlock.find_next('a', {'itemprop': 'url', 'data-marker':'item-title'})
    # blockLines = jobBlock.find_all_next('div',{'data-marker': "item-line"})
    #
    # if blockLines[0].text == "Компания":
    #     fieldOfExp = blockLines[1].text
    # else:
    #     fieldOfExp = blockLines[0].text
    #
    # salary = jobBlock.find_next('meta', {"itemprop": "price"})
    #
    # jobs_collection.insert_one({
    #     "jobName": job['title'],
    #     "jobUrl": job['href'],
    #     "fieldOfExp": fieldOfExp,
    #     "salary": int(salary['content'])
    # })










driver.quit()







