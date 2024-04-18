import requests
from pwn import *
from bs4 import BeautifulSoup
from apidork_resources import apidork_colors

def get_filetype(domain,filetype):

    url = f"https://www.google.com/search?q=site:{domain} filetype:{filetype}&start=0&num=20" 
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)

    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('a', href=True)

    url_filetype_split = ""
    with log.progress("Seacrhing Websites ") as progress:
        try:

            for result in search_results:
                url_filetype = result['href']

                if url_filetype.startswith("/url?q="):
                    url_filetype_split = url_filetype.split('/url?q=')[1].split("&")[0]
                    progress.status(f"{url_filetype_split}")
                    response = requests.get(url_filetype_split, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)

                    if response.status_code != 200:
                        continue 
                    else: 
                        print(apidork_colors.arrow_green + url_filetype_split)

                    time.sleep(0.2)

        except requests.Timeout:
            print(apidork_colors.arrow_red + "Request timed out ... Dropping session ...")
            exit()
        except requests.RequestException as drop:
            print(apidork_colors.arrow_red + "Error occurred ...")
            exit()