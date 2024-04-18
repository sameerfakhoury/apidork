import requests
from pwn import *
import time
from apidork_resources import apidork_colors, apidork_header

def get_zip_info(country,zipcode):
    base_url = f"https://api.zippopotam.us/{country}/{zipcode}"

    with log.progress(f"Searching for {country},{zipcode} info") as progress:
        try:
            response = requests.get(base_url, headers={'User-Agent':apidork_header.headervalue()},timeout=20)
            data = response.json()

            if data:
               
               places = data["places"][0]
               for key, value in data.items():
                    if key != "places":
                        progress.status(key)
                        print(apidork_colors.arrow_green + key, ":", value)
                        time.sleep(0.2)
                    else:
                        for place_key, place_value in places.items():
                            progress.status(place_key)
                            print(apidork_colors.arrow_green + place_key, ":", place_value)
                            time.sleep(0.2)
                            
            else:
                print(apidork_colors.arrow_red + "No Data Found ...")
                exit()

        except requests.Timeout:
            print(apidork_colors.arrow_red + "Request timed out ... Dropping session ...")
            exit()
        except Exception as drop:
            print(apidork_colors.arrow_red + f"Error occurred: ...")
            exit()