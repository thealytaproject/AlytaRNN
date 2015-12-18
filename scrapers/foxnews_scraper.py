from urlparse import urljoin
from bs4 import BeautifulSoup
import requests

#artist_url = "http://genius.com/artists/Justin-bieber"
#BASE_URL = "http://" +raw_input("Enter website domain, such as genius.com: ")
#artist_name = raw_input("Enter Arist name")
#artist_url = "http://genius.com/artists/" + artist_name


for i in range(0, 50):
    BASE_URL = "http://www.foxnews.com/on-air/the-five/transcripts?page=%s" % i

    response = requests.get(BASE_URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
    #Iterate through Index_lists
    soup = BeautifulSoup(response.text, "lxml")
    for transcript_link in soup.select('#block-thefive-transcripts-search-list > article > header > div > h2 > a'):
        link = transcript_link['href'] + "print"
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "lxml")
        for line in soup.select('#content > div > div > div > div > div.main > article'):
            line_out = line.text.encode('utf-8')
            length = len(line_out.split('\n'))
            for j in line_out.split('\n')[23:length-2]:
                with open("foxfive.txt", "a") as myfile:
                    myfile.write(j + '\n')
    print("Scraped page %s " % i)
            #
