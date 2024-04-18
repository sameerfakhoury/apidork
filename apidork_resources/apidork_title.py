import requests
from pwn import *
from bs4 import BeautifulSoup
from apidork_resources import apidork_colors

def get_title(title):
    url = f"https://www.google.com/search?q=intitle:{title}&start=0&num=20" 
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)

    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('a', href=True)
    url_intitle = ""
    with log.progress("Seacrhing Websites ") as progress:
        try:
            for result in search_results:
                url_site = result.get('href')
                
                if url_site.startswith("/url?q="):
                    url_intitle = url_site.split('/url?q=')[1].split('&sa=')[0]
                    progress.status(f"{url_intitle}")
                    response = requests.get(url_intitle, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
                    time.sleep(0.2)

                    if response.status_code != 200:
                        continue 
                    else: 
                        print(apidork_colors.arrow_green + url_intitle)

        except requests.Timeout:
            print(apidork_colors.arrow_red + "Request timed out ... Dropping session ...")
            exit()
        except requests.RequestException as e:
            print(apidork_colors.arrow_red + "Error occurred ...")
            exit()