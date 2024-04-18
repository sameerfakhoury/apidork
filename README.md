# apidork

    █████╗ ██████╗ ██╗██████╗  ██████╗ ██████╗ ██╗  ██╗
    ██╔══██╗██╔══██╗██║██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝
    ███████║██████╔╝██║██║  ██║██║   ██║██████╔╝█████╔╝ 
    ██╔══██║██╔═══╝ ██║██║  ██║██║   ██║██╔══██╗██╔═██╗ 
    ██║  ██║██║     ██║██████╔╝╚██████╔╝██║  ██║██║  ██╗
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   

------------------------------------------------------------

apidork: is an OSINT Python tool coded by Sammer Fakhoury to simplify the utilization of Google dorks and public APIs. The tool offers ten options, with five of them pertaining to Google dorks and the remaining five related to APIs.

The tool enables users to gather data such as social media accounts linked to a username, websites associated with a domain, files with specific extensions related to a domain, keyword searches within a website, and compilation of sites featuring a particular keyword in their titles.

Additionally, the tool facilitates the easy collection of data from public APIs, including information regarding a specific IP, self-checking of one's own IP, details concerning zip/postal codes, as well as extracting coordinates from a location name with the option to check associated information.

The tool offers benefits such as extracting data from various sources through an uncomplicated syntax, achieved by selecting the relevant option type and the necessary data. Additionally, it automatically verifies the validity of a link by making a request and assessing the response.

However, there are a few disadvantages to note. Execution related to Google dorks may occasionally experience delays or connection drops, necessitating a re-execution of the command. It's advised not to execute a large volume of data for a particular domain or via the API to avoid potential blocking.

Regarding usage, the creator of the tool disclaims responsibility for any misuse, emphasizing its educational purpose. If one wishes to add features to the tool, they must contact the creator for permission and are not authorized to reuse the code without proper approval.

------------------------------------------------------------
Steps to follow to install the tool: 

    1. in your terminal: git clone https://github.com/sameerfakhoury/apidork.git
    2. cd apidork
    3. pip install -r requirements.txt
    4. python3 apidork.py
    5. now you are ready to use the tool and check each option with the coresponding infromaiton to use with
------------------------------------------------------------
Syntax: python3 apidork.py -option1 "value1" -option2 "value2"
Options to use:

    1. username search: -u "user_name" -- example: python3 apidork.py -u "example"                                                              
    2. files related to domain: -d "domain_name" -f "file_extension" -- example: python3 apidork.py -d "example.com" -f "pdf"                   
    3. text in website: -url "full_url" -t "keyword" -- example: python3 apidork.py -url "https://example.com/index.html" -t "helloword"        
    4. restrict search to domain : -d "domain_name" -- example: python3 apidork.py -d "xxx.xxx.xx"                                              
    5. links title with keyword: -k "title_keyword" -- example: python3 apidork.py -k "xxxxxxxxxx"                                              
                                                                                                                                                
    6. extract location information: -lat "latitude" -lon "longitude" -- example: python3 apidork.py -lat "xx.xxx..." -lon "xx.xxx..."          
    7. extract location coordinates: -l "location_name" -- example: python3 apidork.py -l "xxxx xxx xx ..."                                     
    8. extract IP informations: -ip "ip" -- example: python3 apidork.py -ip "x.x.x.x"                                                           
    9. check your public IP: -myip -- example: python3 apidork.py -myip                                                                         
    10. extract Zip/postal code informations: -c "country" -z "zipcode" -- example: python3 -c "xx" -z "xxxxx"                                  
