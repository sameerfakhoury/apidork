from apidork_resources import apidork_colors

def banner_call():
    print("""
    █████╗ ██████╗ ██╗██████╗  ██████╗ ██████╗ ██╗  ██╗
    ██╔══██╗██╔══██╗██║██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝
    ███████║██████╔╝██║██║  ██║██║   ██║██████╔╝█████╔╝ 
    ██╔══██║██╔═══╝ ██║██║  ██║██║   ██║██╔══██╗██╔═██╗ 
    ██║  ██║██║     ██║██████╔╝╚██████╔╝██║  ██║██║  ██╗
    ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝                                             
    """)

    print("█▓▒▒░░░[>>] coded by Sameer Fakhoury [@@] OSINT tool based on Google Dorks & public API's ░░░▒▒▓█")
    print("█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█\n")
    print(apidork_colors.RED + "Syntax:"  + apidork_colors.YELLOW + " python3 apidork.py -option1 \"value1\" -option2 \"value2\" ")

    colgreen = apidork_colors.GREEN
    colyellow = apidork_colors.YELLOW

    print(""" 
    {g}1. username search: -u "user_name" {y}-- example: python3 apidork.py -u "example"
    {g}2. files related to domain: -d "domain_name" -f "file_extension" {y}-- example: python3 apidork.py -d "example.com" -f "pdf"
    {g}3. text in website: -url "full_url" -t "keyword" {y}-- example: python3 apidork.py -url "https://example.com/index.html" -t "helloword"
    {g}4. restrict search to domain : -d "domain_name" {y}-- example: python3 apidork.py -d "xxx.xxx.xx"
    {g}5. links title with keyword: -k "title_keyword" {y}-- example: python3 apidork.py -k "xxxxxxxxxx"
          
    {g}6. extract location information: -lat "latitude" -lon "longitude" {y}-- example: python3 apidork.py -lat "xx.xxx..." -lon "xx.xxx..."
    {g}7. extract location coordinates: -l "location_name" {y}-- example: python3 apidork.py -l "xxxx xxx xx ..."
    {g}8. extract IP informations: -ip "IP" {y}-- example: python3 apidork.py -ip "x.x.x.x"
    {g}9. check your public IP: -myip {y}-- example: python3 apidork.py -myip
    {g}10. extract Zip/postal_code informations: -c "country" -z "zipcode" {y}-- example: python3 -c "xx" -z "xxxxx"
    """.format(g=colgreen , y=colyellow))