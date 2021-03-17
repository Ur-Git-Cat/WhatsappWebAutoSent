from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import csv 

driver = webdriver.Chrome('/home/caturrn/project/automateWhatsappSent/chromedriver')
wait = WebDriverWait(driver, 10)
driver.get("https://web.whatsapp.com")

print("Scan QR terus pencet enter")
input()
print("logged in")

with open('CSV coba - Sheet3.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0;
    for row in csv_reader:
        if line_count == 0:
            line_count+=1
        API_tmp = row["API_WA"]
        API_oke = API_tmp.replace("api.whatsapp.com","web.whatsapp.com")
        driver.get(API_oke)
        send_xpath = "/html/body/div/div/div/div[4]/div/footer/div[1]/div[3]"  
        wait_button = wait.until(EC.presence_of_element_located((By.XPATH, send_xpath)))
        send_button = driver.find_element_by_xpath(send_xpath)
        time.sleep(1)
        send_button.click()
        time.sleep(5)
        #add line count
        line_count+=1

driver.quit()
