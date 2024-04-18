import requests
from pwn import *
from apidork_resources import apidork_header, apidork_colors

def get_place_info(latitude, longitude):

    base_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
    with log.progress(f"Seacrhing For {latitude},{longitude} ") as progress:
        try:
            response = requests.get(base_url, headers={'User-Agent':apidork_header.headervalue()},timeout=20)
            data = response.json()
            
            if data:
                address_details = data["address"] 
                lat = data["lat"]
                lon = data["lon"]
            
                for key, value in address_details.items():
                    progress.status(f"{key}")
                    print(apidork_colors.arrow_green + key, ":", value)
                    time.sleep(0.2)

                print(apidork_colors.arrow_green + "latitude :" , lat)
                print(apidork_colors.arrow_green +"longitude :" ,lon)
                
            else: 
                print(apidork_colors.arrow_red + "No Data Found ...")
                exit()
                
        except requests.Timeout:
                    print( apidork_colors.arrow_red + "Request timed out ... Dropping session ...")
                    exit()
        except Exception as w:
                print(apidork_colors.arrow_red + "Error occurred ...")
                exit()




