import glob, os
import midi
from urlparse import urljoin
from bs4 import BeautifulSoup
import requests

os.chdir("data")
for file in glob.glob("*.mid"):
    pattern = midi.read_midifile(file)
    pattern = repr(pattern)
    with open("input.txt", "a") as myfile:
        myfile.write(pattern)
