#!/usr/bin/env python3

from pwn import *
import sys
from apidork_resources import apidork_social_media , apidork_ip , apidork_myip , apidork_zipcode , apidork_site , apidork_title
from apidork_resources import apidork_filetype , apidork_colors , apidork_text , apidork_banner , apidork_location_coordinate , apidork_location_name

apidork_banner.banner_call()
try:
    if len(sys.argv) == 1 and ( sys.argv[0] == "apidork.py" or sys.argv[0] == "./apidork.py") :
         print(apidork_colors.arrow_red + "Specify an option with the realted data ...")

    elif len(sys.argv) == 3 and sys.argv[1] == "-u":  
        social_name = sys.argv[2]
        apidork_social_media.social_media(social_name)

    elif len(sys.argv) == 5 and sys.argv[1] == "-d" and sys.argv[3] == "-f":
        domain = sys.argv[2]  
        filetype = sys.argv[4] 
        apidork_filetype.get_filetype(domain, filetype=filetype)
    
    elif len(sys.argv) == 5 and sys.argv[1] == "-url" and sys.argv[3] == "-t":
        domain = sys.argv[2]  
        textserach = sys.argv[4] 
        apidork_text.get_text(domain, textserach)

    elif len(sys.argv) == 5 and sys.argv[1] == "-lat" and sys.argv[3] == "-lon":
        latitude = sys.argv[2]
        longitude = sys.argv[4]
        apidork_location_coordinate.get_place_info(latitude, longitude)
    
    elif len(sys.argv) == 3 and sys.argv[1] == "-l":
        place_name = sys.argv[2]
        apidork_location_name.get_place_cord(place_name)

    elif len(sys.argv) == 3 and sys.argv[1] == "-ip":
        ip = sys.argv[2]
        apidork_ip.get_ip_info(ip)

    elif len(sys.argv) == 2 and sys.argv[1] == "-myip":
        apidork_myip.get_my_ip()

    elif len(sys.argv) == 5 and sys.argv[1] == "-c" and sys.argv[3] == "-z":
        country = sys.argv[2]  
        zipcode = sys.argv[4] 
        apidork_zipcode.get_zip_info(country,zipcode)

    elif len(sys.argv) == 3 and sys.argv[1] == "-d":
        domain = sys.argv[2]  
        apidork_site.get_site(domain)
    
    elif len(sys.argv) == 3 and sys.argv[1] == "-k":
        title = sys.argv[2]  
        apidork_title.get_title(title)
            
    else: 
        print(apidork_colors.arrow_red + "Syntax Wrong ...")

except Exception as drop:
   print(apidork_colors.arrow_red + "Error occurred ...")