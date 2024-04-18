import requests
from apidork_resources import apidork_header, apidork_colors

def get_my_ip():
    base_url = f"https://api.ipify.org/?format=json"
    
    try:
        response = requests.get(base_url, headers={'User-Agent':apidork_header.headervalue()},timeout=20)
        data = response.json()

        if data:
            myip = data["ip"]
            print(apidork_colors.arrow_green + "Your Public IP: " , myip)

        else: 
            print(apidork_colors.arrow_red + "No Data Found ...")
            exit()
    
    except requests.Timeout:
                print( apidork_colors.arrow_red + "Request timed out ... Dropping session ...")
                exit()
    except Exception as w:
            print(apidork_colors.arrow_red + "Error occurred ...")
            exit()