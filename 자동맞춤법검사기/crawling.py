from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from IPython.display import clear_output 
import pandas as pd
from selenium.webdriver.common.keys import Keys
# import pyautogui
# import clipboard
from selenium.webdriver.common.alert import Alert


d = pd.read_csv(r'C:\Users\DILAB\쥬피터전용폴더\auto_fixed_word\v2_번역2_essay_dataset.csv',index_col=0,encoding='cp949')   # id가 인덱스 
# d2 = pd.read_excel('d2.xlsx', index_col=0)
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(r'C:\Users\DILAB\쥬피터전용폴더\auto_fixed_word\chromedriver.exe', chrome_options=options)
popup = Alert(driver)

for i in range(1356,1578):
    try:
        driver.get('https://www.incruit.com/tools/spell/')
        driver.implicitly_wait(3)
        driver.maximize_window()
        text_box = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div[1]/textarea[1]')
        raw_text = d["Kor_essay_2"][i]
        text_box.send_keys(raw_text)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/form/div/div[2]/div[4]/button').click()   # 맞춤법 검사 버튼 클릭
        edit_btt = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div[3]/button[1]")))
        sleep(1)
        edit_btt.click()        # 수정하기 클릭
        popup.accept()
        # pyautogui.press('enter')  # 엔터 
        # driver.implicitly_wait(10)
        # sleep(2)

        refined_text = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div[1]/div[1]/p[2]').text
        print(refined_text)
        print('#'*10)
        # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div[3]/button[2]').click()     # 복사버튼 클릭
        # pyautogui.press('enter')  # 엔터
        
        d["2차검수"][i] = refined_text
        # print('='*10)
        # print(d['Kor_essay_2'][i])
        # print(d['2차검수'][i])
        if i%10 == 0:   # 10씩 저장하기
            d.to_csv(r'C:\Users\DILAB\쥬피터전용폴더\auto_fixed_word\v2_번역2_essay_dataset.csv',encoding='cp949')
    except:
        continue
d.to_csv(r'C:\Users\DILAB\쥬피터전용폴더\auto_fixed_word\v2_번역2_essay_dataset.csv',encoding='cp949')