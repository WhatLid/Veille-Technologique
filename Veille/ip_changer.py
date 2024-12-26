from stem import Signal
from stem.control import Controller
import requests

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

change_ip()
check_ip()