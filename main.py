from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from functions import Functions
import functions
import concurrent.futures
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

number_account_creation = 2
num_concurrent_runs = 20
counter = 0
proxy_counter_per_each_loop = 0
Functions = Functions()
load_dotenv()

Functions.get_proxies()

# with concurrent.futures.ThreadPoolExecutor(max_workers=num_concurrent_runs) as executor:
#     futures = [executor.submit(Functions.check_proxies) for _ in range(num_concurrent_runs)]
#     concurrent.futures.wait(futures)
    
# valid_proxies = functions.valid_proxies
valid_proxies =['139.59.1.14:8080', '47.88.11.3:69', '89.145.162.81:3128', '47.88.11.3:9091', '159.203.61.169:3128', '194.182.178.90:3128', '39.104.89.111:8009', '39.104.89.111:8058', '139.59.1.14:3128', '47.252.1.180:33060', '47.252.1.180:1234', '47.252.1.180:80', '8.219.169.172:9000', '64.225.8.179:10006', '49.0.246.130:8090', '49.0.246.130:8084', '47.253.105.175:8047', '64.225.8.132:10004', '91.206.229.249:3128', '198.11.175.192:800', '206.233.177.254:80', '103.146.17.241:80', '']
proxy_number = len(valid_proxies)
driver = webdriver.Chrome(executable_path="./resources/chrome driver/chromedriver.exe")
wait = WebDriverWait(driver, 5) 
for _ in range(number_account_creation):
    firstName, lastName, emailAddress, gender, password = Functions.info_generator_api()
    print(firstName)
    proxy_counter_per_each_loop = 0
    while True:
        try:
            if(counter> proxy_number-1):
                counter=0
                if(proxy_counter_per_each_loop == proxy_number):
                    break
            proxy_counter_per_each_loop = 0
            proxy_ip = valid_proxies[counter]
            chrome_options = Options()
            # chrome_options.add_argument(f'--proxy-server={proxy_ip}')
            driver = webdriver.Chrome(executable_path="./resources/chrome driver/chromedriver.exe",options=chrome_options)
            driver.get("https://facebook.com")
            create_new_account = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id^='u_0_0_123']")))
            counter +=1
            proxy_counter_per_each_loop += 1
            break
        except Exception as e:
            counter +=1
            proxy_counter_per_each_loop += 1   
            continue
            

        



proxy = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
res = requests.get(proxy)
res_list = list(res)
print(res_list)
print(res)

try:

    proxy_url = '139.59.1.14:8080'
    proxy = {'http': proxy_url, 'https': proxy_url}
    response = requests.get('http://facebook.com', proxies=proxy, timeout=5)
    response.raise_for_status()
    print('Proxy is working')
   

except Exception as e:
    print(e)


proxy_ip = "103.105.196.130:3128"
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy_ip}')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://whatismyipaddress.com")
time.sleep(10)


load_dotenv()
name_generator_api = f"https://api.parser.name/?api_key={os.getenv('NAME_GENERATOR_API_KEY')}&endpoint=generate"
name_generator_response = requests.get(name_generator_api)
if name_generator_response.status_code == 200:
   name_generator_response_json = name_generator_response.json()

firstName =  name_generator_response_json["data"][0]["name"]["firstname"]["name"]
lastName =  name_generator_response_json["data"][0]["name"]["lastname"]["name"]
emailAddress =   name_generator_response_json["data"][0]["email"]
gender = name_generator_response_json["data"][0]["name"]["firstname"]["gender"]

print(gender)
print(firstName)
print(lastName)
print(emailAddress)

password_length = 16 
password_generator_api = f"https://api.api-ninjas.com/v1/passwordgenerator?length={password_length}"
password_generator_response = requests.get(password_generator_api,  headers={"X-Api-Key": f"{os.getenv('PASSWORD_GENERATOR_API_KEY')}"})

password_generator_response_json = password_generator_response.json()
password = password_generator_response_json["random_password"]

print(password)


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 5) 

driver.get("https://www.facebook.com/")


create_new_account = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id^='u_0_0_']")))
create_new_account.click()

first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
first_name.send_keys("firstName")

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("lastName")

reg_address = driver.find_element(By.NAME, "reg_email__")
reg_address.send_keys("emailAddress")

reg_password = driver.find_element(By.NAME, "reg_passwd__")
reg_password.send_keys("password")

birthday_day = driver.find_element(By.NAME, "birthday_day")
birthday_day_dropdown  = Select(birthday_day)
birthday_day_dropdown.select_by_value("1")

birthday_month = driver.find_element(By.NAME, "birthday_month")
birthday_month_dropdown  = Select(birthday_month)
birthday_month_dropdown.select_by_value("1")

birthday_year = driver.find_element(By.NAME, "birthday_year")
birthday_year_dropdown  = Select(birthday_year)
birthday_year_dropdown.select_by_value("2000")

if "m" == "m":
    gender = driver.find_element(By.CSS_SELECTOR, "input[name='sex'][value='2']")
    gender.click()
else:
    gender = driver.find_element(By.CSS_SELECTOR, "input[name='sex'][value='1']")
    gender.click()
    
    


sign_up = wait.until(EC.element_to_be_clickable((By.NAME, "websubmit")))
sign_up.click()

x = input("enter")


