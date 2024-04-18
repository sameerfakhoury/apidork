import requests
from apidork_resources import apidork_header, apidork_colors

def get_place_cord(place_name):
    
    base_url = f"https://nominatim.openstreetmap.org/search?format=json&q={place_name}"
    
    try:
        response = requests.get(base_url, headers={'User-Agent':apidork_header.headervalue()},timeout=20)
        data = response.json()

        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]

            print(apidork_colors.arrow_green + "latitude :" , lat)
            print(apidork_colors.arrow_green + "longitude :" ,lon)

        else: 
            print(apidork_colors.arrow_red + "No Data Found ...")
            exit()
    
    except requests.Timeout:
                print( apidork_colors.arrow_red + "Request timed out ... Dropping session ...")
                exit()
    except Exception as w:
            print(apidork_colors.arrow_red + "Error occurred ...")
            exit()


            
