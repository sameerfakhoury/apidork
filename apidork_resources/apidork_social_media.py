import requests
from pwn import *
import time
from apidork_resources import apidork_header, apidork_colors

def social_media(social_name):

    social_websites = {
    'github.com': "https://www.github.com/",
    'linkedin.com': "https://linkedin.com/",
    'facebook.com': "https://www.facebook.com/",
    'twitter.com': "https://twitter.com/",
    'pinterest.com': "https://www.pinterest.com/",
    'instagram.com': "https://www.instagram.com/",
    'snapchat.com': "https://www.snapchat.com/add/",
    'twitch.com': "https://www.twitch.tv/",
    'medium.com': "https://medium.com/@",
    'youtube.com': "https://www.youtube.com/",
    'reddit.com': "https://www.reddit.com/u/",
    'discord.com': "https://www.discord.com/",
    'quora.com': "https://www.quora.com/",
    }

    with log.progress("Seacrhing SocialMedia ") as progress:
        for key, value in social_websites.items():
            full_link = f"{value}{social_name}"
            try:
                response = requests.get(full_link, headers={'User-Agent':apidork_header.headervalue()},timeout=20)
                time.sleep(0.2)
                progress.status(f"{key}")
                
                if response.status_code == 200:
                    print(apidork_colors.arrow_green + response.url )

            except requests.Timeout:
                print( apidork_colors.arrow_red + "Request timed out ... Dropping session ...")
                exit()
            except Exception as e:
                print(apidork_colors.arrow_red + "Error occurred ...")
                exit()
