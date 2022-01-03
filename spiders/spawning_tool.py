
import bs4
import requests
import wget
import time


def get_downloads(links):
    downloads = []
    for link in links:
        href = link.get('href')
        if href.endswith('/download/'):
            downloads.append('https://lotv.spawningtool.com' + href)

    for down in downloads:
        download_name = 'spawningtool_' + down.split('/')[3] + '.SC2Replay'
        wget.download(url, '../data/spawning_tool/' + download_name)


url = 'https://lotv.spawningtool.com/replays/?before_played_on=&order_by=&before_time=&query=&after_played_on=&after_time=&coop=&tag=9&tag=17&patch=&p='

for a in range(1, 211): #current last page is 210
    response = requests.get(url + str(a))
    soup = bs4.BeautifulSoup(response.content, 'lxml')
    links = soup.find_all('a')
    get_downloads(links)
    if a % 10 == 0:
        print('sleep')
        time.sleep(10)

