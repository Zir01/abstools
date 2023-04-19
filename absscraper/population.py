import requests
from typing import List
from bs4 import BeautifulSoup

class Link():
    name:str
    url:str

    def __init__(self, name:str, url:str):
        self.name = name
        self.url = url


class Release(Link):
    pass
class Download(Link):
    pass
    
class ReleaseDetails():
    date:str
    reference_period:str
    description:str
    downloads:List[Download]


class Population():

    def __init__(self):
        self.base_url = "https://www.abs.gov.au"

    def _find_releases(self, soup:BeautifulSoup, block_id:str)->List[Release]:
        releases = []
        items = soup.find(id=block_id)
        rows = items.find_all('div', class_='views-row')
        for row in rows:
            anchor = row.find('a')
            url = ""
            if anchor['href'][:5] == 'https':
                url = anchor['href']
            else:
                url = self.base_url + anchor['href']
            releases.append(Release(anchor.text, url))
        return releases    

    def _find_latest_releases(self, soup:BeautifulSoup)->List[Release]:
        return self._find_releases(soup, "block-views-block-topic-releases-listing-topic-latest-release-block")
    def _find_previous_releases(self, soup:BeautifulSoup)->List[Release]:
        return self._find_releases(soup, "block-views-block-topic-releases-listing-topic-previous-releases-block")            
    
    def _find(self, url:str):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        latest = self._find_latest_releases(soup)
        previous = self._find_previous_releases(soup)
        return latest + previous                


    def national_state_releases(self)->List[Release]:
        pop_url = f"{self.base_url}/statistics/people/population/national-state-and-territory-population"
        return self._find(pop_url)

    def regional_3218_releases(self)->List[Release]:
        pop_url = f"{self.base_url}/statistics/people/population/regional-population"
        return self._find(pop_url)

    def regional_3235_releases(self)->List[Release]:
        pop_url = f"{self.base_url}/statistics/people/population/regional-population-age-and-sex"
        return self._find(pop_url)        


    def release_details(self, release:Release):

        dl = requests.get(release.url)
        print(release.url)
        soup = BeautifulSoup(dl.content, 'html.parser')
        body = soup.find('head')
        release_date = body.find('meta', {"name" : 'dcterms.issued'})
        reference_period = body.find('meta', {"name" : 'dcterms.temporal'})
        description = body.find('meta', {"name" : 'description'})
        print(reference_period)

        details = ReleaseDetails()
        details.date = release_date['content']
        details.reference_period = reference_period['content']
        details.description = description['content']
        details.downloads = self.downloads_list(release)

        return details


    def downloads_list(self, release:Release)->List[Download]:

        result = []

        dl = requests.get(release.url)
        soup = BeautifulSoup(dl.content, 'html.parser')
        links = soup.find_all("a", {"title" : lambda L: L and L.endswith('.xls')})
        for link in links:
            result.append(Download(link['aria-label'], link['href']))
        return result
             

    

    