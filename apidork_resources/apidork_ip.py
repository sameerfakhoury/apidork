import requests
from pwn import *
import time
from apidork_resources import apidork_colors, apidork_header

def get_ip_info(ip):
    
    base_url = f"https://api.ipbase.com/v1/json/{ip}"

    with log.progress(f"Searching for {ip} ") as progress:
        try:
            response = requests.get(base_url, headers={'User-Agent':apidork_header.headervalue()},timeout=20)
            data = response.json()

            if data:
                for key, value in data.items():
                    progress.status(f"{key}")
                    print(apidork_colors.arrow_green + key, ":", value)
                    time.sleep(0.2)
            else:
                print(apidork_colors.arrow_red + "No Data Found ...")
                exit()

        except requests.Timeout:
            print(apidork_colors.arrow_red + "Request timed out ... Dropping session ...")
            exit()
        except Exception as drop:
            print(apidork_colors.arrow_red + "Error occurred ...")
            exit()
