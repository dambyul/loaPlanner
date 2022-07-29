from selenium import webdriver
from selenium.webdriver.common.by import By
import notion

#캐릭터 닉네임
charName = "영광의평원"

#신규/업데이트 여부
createNew = False

#DB세팅
if createNew:
    notion.setDatabase()
else:
    notion.addCol(charName)

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get("https://lostark.game.onstove.com/Profile/Character/" + charName)

menu = driver.find_element(By.XPATH,'/html/body/div[2]/div/main/div/div[3]/div[2]/div[1]/div[1]/a[4]').click()
tab = driver.find_element(By.CLASS_NAME,'profile-collection')
tabs = tab.find_element(By.CLASS_NAME,'lui-tab__menu')
tabs = tabs.find_elements(By.TAG_NAME,'a')
for i in tabs:
    link = i.get_attribute('href')
    link = link.split('#')[1]
    i.click()
    data = driver.find_element(By.ID,link)
    title = data.find_element(By.CLASS_NAME,'collection-status')
    body = data.find_elements(By.TAG_NAME,'li')
    tmp_title = title.text.split("\n")
    titleTxt = tmp_title[0].rstrip(" 획득 현황")
    if titleTxt != "모코코 씨앗":
        print(titleTxt)
        for j in body:
            num = j.find_element(By.TAG_NAME,'span').text
            text = j.text.lstrip(num)
            if j.get_attribute('class') == "complete":
                text = text.rstrip('획득').strip()
                comp = "완료"
                print(f"[{num}] ",end="")
                print(text)
            else:
                comp = "미완료"
                print(f"[{num}] ", end="")
                print(text)
            if createNew:
                notion.createData(text, num, titleTxt, comp, charName)
            else:
                notion.editData(text, charName, comp)

driver.close()