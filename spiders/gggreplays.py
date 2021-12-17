
import time
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_downloads(links):
    downloads = []
    for tag in links:
        link = tag.get_attribute('href')
        if 'gggreplays.com/matches/' in link:
            downloads.append(link)
    downloads = list(set(downloads))
    for down in downloads:
        download_name = 'gggtracker_' + down.split('/')[4] + '.SC2Replay'
        wget.download(url + '/replay', '../data/gggreplays/' + download_name)


url = 'https://gggreplays.com/matches#?game_type=1v1&race=protoss&vs_race=protoss&page='

for a in range(0, 2482): # current last page is 2481
    driver = webdriver.Safari()
    driver.get(url + str(a))
    tags = driver.find_elements(By.TAG_NAME, 'a')
    get_downloads(tags)
    driver.quit()
    if a % 10 == 0:
        time.sleep(10)

