import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

def change_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='VTBDA-2024')
        controller.signal(Signal.NEWNYM)
        print("Nouvelle identité demandée.")

def check_ip():
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050',
    }
    response = requests.get('http://httpbin.org/ip', proxies=proxies)
    print("Adresse IP actuelle :", response.text)

def search_duckduckgo(query):
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050',
    }
    url = f'http://duckduckgo.com/html/?q={query}+site:.onion'
    response = requests.get(url, proxies=proxies)
    
    # Analyser le HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraire les liens
    links = []
    for a in soup.find_all('a', class_='result__a'):
        link = a['href']
        links.append(link)
    
    return links

change_ip()
check_ip()

resultats = search_duckduckgo('coffee')
for url in resultats:
    print(url)
