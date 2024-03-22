import requests
import queue
from dotenv import load_dotenv
import os

all_proxies = queue.Queue()
valid_proxies = []

class Functions:
    
    load_dotenv()
    
    def get_proxies(self):
        global all_proxies
        global valid_proxies
        proxy = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        res = requests.get(proxy)
        res_text = res.content.decode("utf-8") 
        proxies_list = res_text.split("\r\n")
        for proxy in proxies_list:
            all_proxies.put(proxy)

    def check_proxies(self):
        global all_proxies
        while not all_proxies.empty():
            proxy = all_proxies.get()
            try:
                res = requests.get("http://facebook.com",
                                proxies={"http":proxy,
                                        "https":proxy},
                                        timeout=5
                                        )
            except:    
                continue
                
            if res.status_code == 200:
                valid_proxies.append(proxy)
                
    def info_generator_api(self):
        name_generator_api = f"https://api.parser.name/?api_key={os.getenv('NAME_GENERATOR_API_KEY')}&endpoint=generate"
        name_generator_response = requests.get(name_generator_api)
        if name_generator_response.status_code == 200:
           name_generator_response_json = name_generator_response.json()

        firstName =  name_generator_response_json["data"][0]["name"]["firstname"]["name"]
        lastName =  name_generator_response_json["data"][0]["name"]["lastname"]["name"]
        emailAddress =   name_generator_response_json["data"][0]["email"]
        gender = name_generator_response_json["data"][0]["name"]["firstname"]["gender"]
        
        password_length = 16 
        password_generator_api = f"https://api.api-ninjas.com/v1/passwordgenerator?length={password_length}"
        password_generator_response = requests.get(password_generator_api,  headers={"X-Api-Key": f"{os.getenv('PASSWORD_GENERATOR_API_KEY')}"})

        password_generator_response_json = password_generator_response.json()
        password = password_generator_response_json["random_password"]
        
        data = (firstName, lastName, emailAddress, gender, password)
        return data



        
                

   
        