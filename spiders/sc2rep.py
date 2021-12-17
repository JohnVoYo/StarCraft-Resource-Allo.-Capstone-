
import bs4
import requests
import wget
import time


def get_downloads(links):
    downloads = []
    for link in links:
        href = link.get('href')
        if href.startswith('/down.'):
            downloads.append('https://sc2rep.ru' + href)

    for down in downloads:
        download_name = 'sc2rep_' + down.split('id=')[1] + '.SC2Replay'
        wget.download(url, '../data/sc2rep/' + download_name)


url = 'https://sc2rep.ru/index.php?gt=1&matchup1x1=4&page='


for a in range (880, 1940, 20):
    print('page -- ', a)
    response = requests.get(url + str(a))
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    links = soup.find_all('a')
    get_downloads(links)
    if a % 100 == 0:
        print('sleep')
        time.sleep(10)
