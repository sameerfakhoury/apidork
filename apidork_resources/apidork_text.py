import requests
from pwn import *
from bs4 import BeautifulSoup
import time
from apidork_resources import apidork_colors , apidork_header


def get_text(domain, text_search):

    with log.progress("Checking ") as progress:
        try: 
            response = requests.get(domain, headers={'User-Agent':apidork_header.headervalue()},timeout=20)
            if response.status_code != 200:
                print(apidork_colors.arrow_red + "Error occurred ...")
                exit()

            soup = BeautifulSoup(response.content, 'html.parser')
            text = ' '.join([tag.strip() for tag in soup.find_all(text=True)])

            text_lower = text.lower()
            keyword_lower = text_search.lower()
            keyword_length = len(text_search)
            index = text_lower.find(keyword_lower)

            if index != -1:
                while index != -1:
                    start_index = max(0, index)
                    end_index = min(len(text_lower), index + keyword_length + 30)
                    found_text = text[start_index:end_index]
                    print(apidork_colors.arrow_green + found_text)
                    time.sleep(0.2)
                    index = text_lower.find(keyword_lower, index + 1)
                    progress.status(found_text)
            else:
                print(apidork_colors.arrow_red + "Keyword isn't found")

        except Exception as fail:
            print(apidork_colors.arrow_red + "Error occurred ...")