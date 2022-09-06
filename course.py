from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import winsound
import time
 
 ###要偵測的課名&老師名
class_name = ""
professor_name = ""
###每隔幾秒刷新
renew_time = 5

options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
chrome = webdriver.Chrome(chrome_options=options)
chrome.get("https://course.ncku.edu.tw/index.php?c=qry11215")
find1 = chrome.find_element(By.XPATH,'//*[@id="main_content"]/div[2]/button[1]')
find1.click()
time.sleep(3)
find1 = chrome.find_element(By.XPATH,'//*[@id="main_content"]/div[2]/button[2]')
find1.click()
time.sleep(3)


class_name_input = chrome.find_element(By.XPATH,'//*[@id="cosname"]')
class_name_input.send_keys(class_name)

professor_name_input = chrome.find_element(By.XPATH,'//*[@id="teaname"]')
professor_name_input.send_keys(professor_name)

# week_input = chrome.find_element(By.XPATH,'//*[@id="sel_wk"]')
# week_input.click()
# day_select = chrome.find_element(By.XPATH,'//*[@id="sel_wk"]')

search_button = chrome.find_element(By.XPATH,'//*[@id="main_content"]/div[3]/button')
search_button.click()
time.sleep(5)
try: 
    text = chrome.find_element(By.XPATH,'//*[@id="main_content"]/div[6]/table/tbody/tr[2]/td[4]').text
except:
    print("course not found")
    chrome.quit()
    exit()
winsound.Beep(400,1000)
while True:
    time.sleep(renew_time)
    text = chrome.find_element(By.XPATH,'//*[@id="main_content"]/div[6]/table/tbody/tr[2]/td[4]').text
    print(text)
    if "額滿" not in text: 
        winsound.Beep(400,1000)
    chrome.refresh()
    

chrome.quit()