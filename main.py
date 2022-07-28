from selenium import webdriver
from selenium.webdriver.common.by import By
import time

charName = "선늘"

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
driver.get("https://lostark.game.onstove.com/Profile/Character/" + charName)

menu = driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div/div[3]/div[2]/div[1]/div[1]/a[4]').click()
tab = driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div/div[3]/div[2]/div[1]/div[5]/div/div[1]')

menus = tab.find_elements(By.TAG_NAME,'a')

for i in menus :
    print(i.text)
    i.click()
    data = driver.find_elements(By.CLASS_NAME, 'collection-list')
    for j in data:
        print(j.text)

driver.close()