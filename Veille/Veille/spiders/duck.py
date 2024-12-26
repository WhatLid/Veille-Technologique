import scrapy
from bs4 import BeautifulSoup

class OnionCafeSpider(scrapy.Spider):
    name = 'onion'
    
    # Définir l'URL de recherche DuckDuckGo pour café et .onion
    start_urls = ['https://duckduckgo.com/html/?q=hidden wiki']
    
    def parse(self, response):
        # Analysez le HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraire les liens des résultats
        for result in soup.find_all('a', class_='result__a'):
            link = result['href']
            yield {
                'url': link
            }
        
        # Optionnel : Suivre d'autres liens si nécessaire
        # Si vous souhaitez suivre les pages suivantes (pagination)
        next_page = soup.find('a', {'rel': 'next'})
        if next_page:
            yield response.follow(next_page['href'], self.parse)