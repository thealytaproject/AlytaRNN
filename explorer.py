from urlparse import urljoin
from bs4 import BeautifulSoup
import requests

BASE_URL = "http://" +raw_input("Enter website domain, such as genius.com: ")

#artist_name = raw_input("Enter Arist name")
#artist_url = "http://genius.com/artists/" + artist_name



response = requests.get(BASE_URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

soup = BeautifulSoup(response.text, "lxml")
for song_link in soup.select('ul.characters_index_list > li > a'):
    link = urljoin(BASE_URL, song_link['href'])
    response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
    soup2 = BeautifulSoup(response.text, "lxml")
    for artist_link in soup2.select('ul.artists_index_list > li > a'):
        link2 = artist_link['href']
        response = requests.get(link2, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        soup3 = BeautifulSoup(response.text, "lxml")
        for artist_name in soup3.select('h1.artist'):
            print artist_name

        #for song_link in soup.select('ul.song_list > li > a'):
        #    link = urljoin(BASE_URL, song_link['href'])
        #    print link
            #response = requests.get(link)
            #soup = BeautifulSoup(response.text)
            #lyrics = soup.find('div', class_='lyrics').text.strip()
            #print(lyrics)
            #lyrics = lyrics.encode('utf-8').strip()
            #with open(artist_name + ".txt", "a") as myfile:
            #    myfile.write(lyrics)
