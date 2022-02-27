from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
number = 0
while True:
    driver = webdriver.Chrome(PATH)
    driver.get("https://splinterlands.io")
    time.sleep(3)
    go = driver.find_element_by_id("play_now_btn")
    go.click()
    time.sleep(5)
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")
    email.send_keys("YOUR E-Mail")
    password.send_keys("Your PW")
    password.submit()
    time.sleep(5)
    close = WebDriverWait(driver, 360).until(
    EC.presence_of_element_located((By.CLASS_NAME, "close")))
    close.click()
    i = 0
    while i < 20:
        try:
            battle = driver.find_element_by_id("battle_category_btn")
            battle.click()
            ready = True  
        except:
            driver.get("https://splinterlands.com/?p=battle_history")
            ready = True
        while ready == True:
                try:
                    make = WebDriverWait(driver, 360).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "btn--create-team")))
                    time.sleep(15)
                    make.click()
                    time.sleep(10)
                    i += 1
                    ready = False
                    x = driver.find_element_by_class_name("mana-cap").text
                    mana_cap = int(x)
                    mana = 0
                    summoner = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-49-')]")
                    time.sleep(5)
                    summoner.click()
                    mana += 3
                    tank = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-50-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    tank.click()
                    mana += 5
                    monster1 = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-47-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    if mana + 3 <= mana_cap:
                        monster1.click()
                        mana += 3
                    monster2 = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-141-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    if mana + 3 <= mana_cap:
                        monster2.click()
                        mana +=3
                    monster3 = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-52-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    if mana + 2 <= mana_cap:
                        monster3.click()
                        mana += 2
                    monster4 = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-51-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    if mana + 4 <= mana_cap:
                        monster4.click()
                        mana += 4
                    monster5 = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-139-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    if mana + 4 <= mana_cap:
                        monster5.click()
                        mana += 4
                    monster6 = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-135-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    if mana + 3 <= mana_cap:
                        monster6.click()
                        mana += 3
                    monster7 = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-138-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    if mana + 2 <= mana_cap:
                        monster7.click()
                        mana += 2
                    monster8 = driver.find_element_by_xpath("//*[starts-with(@id, 'starter-136-')]")
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight/0);")
                    time.sleep(1)
                    if mana + 1 <= mana_cap:
                        monster8.click()
                        mana += 1
                    fight = driver.find_element_by_class_name("btn-green")
                    time.sleep(3)
                    fight.click()
                    rumble = WebDriverWait(driver, 180).until(
                    EC.presence_of_element_located((By.ID, "btnRumble")))
                    time.sleep(20)
                    rumble.click()
                    time.sleep(5)
                    skip = driver.find_element_by_id("btnSkip")
                    time.sleep(2)
                    skip.click()
                    end = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "btn--done")))
                    time.sleep(10)
                    end.click()
                    
                    
                    print(i)
                except:
                    driver.get("https://splinterlands.com/?p=battle_history")
                    time.sleep(10)
                    ready = False
    
    number += 1
    print("Finished!!!")
    print("number" + str(number))
    #time.sleep(3500)
driver.quit()
