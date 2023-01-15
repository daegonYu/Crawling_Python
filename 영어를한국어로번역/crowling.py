from selenium import webdriver
import pandas as pd


driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://papago.naver.com/')
driver.maximize_window()

d = pd.read_excel('refined_datafile.xlsx',index_col=0)
d2 = pd.read_excel('d2.xlsx', index_col=0)
# for i in range(len(d)):
text = ' ' + d.iloc[0][1]
english = driver.find_element_by_xpath('/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[3]')
english.send_keys(text)
korean = driver.find_element_by_xpath('/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[5]')
d2.loc[len(d2)] = korean.text()
english.clear()
print(d2)