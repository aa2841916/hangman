import urllib.response
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site = site

    def scrape(self):
        r = urllib.response.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

new = 'http://t1451test.1451cn.com/pat/#/patients/region/province-home/'
Scraper(new).scrape()