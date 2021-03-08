from typing import Text
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

# Give Your URL Here
my_url = "https://subslikescript.com/series/Two_and_a_Half_Men-369179/season-1/episode-1-Pilot"

u_client = ureq(my_url)
page_html = u_client.read()
u_client.close()

page_soup = soup(page_html, "html.parser")
script =  page_soup.find("div", {"class":"full-script"})

outfile = open('./script.txt', 'w')
outfile.write(script.text)