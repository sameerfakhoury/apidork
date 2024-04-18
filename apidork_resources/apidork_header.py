from fake_useragent import UserAgent
from apidork_resources import apidork_colors

try:
    def headervalue():
        user_agent = UserAgent()
        random_user_agent = user_agent.random
        return random_user_agent

except Exception as drop:
    print(apidork_colors.arrow_red + "Error occurred ...")