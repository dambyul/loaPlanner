from selenium import webdriver
from selenium.webdriver.common.by import By
import notion
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('--start-maximized')
options.add_argument('--start-fullscreen')
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=options)
driver.get("https://lostark.game.onstove.com/ItemDictionary")
tab = driver.find_element(By.CLASS_NAME,'main-category')
tabs = tab.find_elements(By.TAG_NAME,'label')
a = [i for i in tabs if i.text == "수집 포인트 아이템"]
a[0].click()
tab = driver.find_element(By.CLASS_NAME,'sub-category')
tabs = tab.find_elements(By.TAG_NAME,'label')
for i in tabs:
    i.click()
    time.sleep(0.2)
    tab_ = driver.find_element(By.CLASS_NAME, 'list-box')
    tab_S = tab_.find_elements(By.CLASS_NAME, 'name')
    for j in tab_S:
        result = None
        while result is None:
            try:
                j.click()
                time.sleep(0.2)
                data = driver.find_element(By.CLASS_NAME,  "lui-tab__content")
                result = data.text
                notion.addLoc(j.text,data.text)
            except:
                pass
    driver.execute_script('scroll(0, -250);')