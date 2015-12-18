from urlparse import urljoin
from bs4 import BeautifulSoup
import requests

artist_url = "http://genius.com/artists/Justin-bieber"
BASE_URL = "http://" +raw_input("Enter website domain, such as genius.com: ")
artist_name = raw_input("Enter Arist name")
artist_url = "http://genius.com/artists/" + artist_name



response = requests.get(artist_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

#Iterate through Index_lists
soup = BeautifulSoup(response.text, "lxml")
for song_link in soup.select('ul.characters_index_list > li > a'):
    link = urljoin(BASE_URL, song_link['href'])
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    lyrics = soup.find('div', class_='lyrics').text.strip()
    print(lyrics)
    lyrics = lyrics.encode('utf-8').strip()
    with open(artist_name + ".txt", "a") as myfile:
        myfile.write(lyrics)

#Iterate through Artists in an index_list
soup = BeautifulSoup(response.text, "lxml")
for song_link in soup.select('ul.artists_index_list > li > a'):
    link = urljoin(BASE_URL, song_link['href'])
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    lyrics = soup.find('div', class_='lyrics').text.strip()
    print(lyrics)
    lyrics = lyrics.encode('utf-8').strip()
    with open(artist_name + ".txt", "a") as myfile:
        myfile.write(lyrics)

#iterate through an Artist's songs and print lyrics
soup = BeautifulSoup(response.text, "lxml")
for song_link in soup.select('ul.song_list > li > a'):
    link = urljoin(BASE_URL, song_link['href'])
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    lyrics = soup.find('div', class_='lyrics').text.strip()
    print(lyrics)
    lyrics = lyrics.encode('utf-8').strip()
    with open(artist_name + ".txt", "a") as myfile:
        myfile.write(lyrics)
