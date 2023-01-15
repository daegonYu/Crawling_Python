from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os               # 폴더 생성



class HowThat:
    def __init__(self, regions):
        self.driver = webdriver.Chrome()
        self.regionNames = regions
        self.etc = ['지역명소','숙박','음식점','즐길거리']
        self.food =[]             # ['군산','군산맛집','사진URL']
        self.lodgment = []
        self.enjoylist = []
        self.bestRegion = []        # 명소이름, 별점, 사진URL


    def makeFolder(self):
        os.makedirs('./전라북도',exist_ok=True)
        for i in range(len(self.regionNames)):
            path = './'+'전라북도/'+self.regionNames[i]
            os.makedirs(path, exist_ok=True)
            for j in range(len(self.etc)):
                path = './' +'전라북도/'+ self.regionNames[i] + '/' + self.etc[j]     # ./군산/숙박
                os.makedirs(path, exist_ok=True)

    def food_crawling(self):
        for i in range(len(self.regionNames)):
            URL = 'https://www.tripadvisor.co.kr/Search?q='+self.regionNames[i]
            self.driver.get(URL)     # 지역 URL 들어감
            self.food.append([])      # 시별 구분
            self.driver.implicitly_wait(100)  # 잠깐 대기
            element = self.driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[3]/a')   # 음식점 배너 선택
            self.driver.execute_script("arguments[0].click();",element)      # 클릭
            self.driver.implicitly_wait(100)  # 잠깐 대기
            restaurants = self.driver.find_elements_by_css_selector('.result-title')        # 음식점 이름들 select
            for m in range(len(restaurants)):
                self.food[i].append([])         # 음식점 개수만큼 리스트 추가   [[]]// [[],[]]
                self.food[i][m] = [self.regionNames[i], restaurants[m].text]    # food = [['군산', '군산횟집'],[...,...]]
                img_urls = self.driver.find_elements_by_css_selector('#BODY_BLOCK_JQUERY_REFLOW > div.page > div > div.ui_container.main_wrap > div > div > div > div > div.content_column.ui_column.is-9-desktop.is-12-tablet.is-12-mobile > div > div.ui_columns.sections_wrapper > div > div.prw_rup.prw_search_search_results.ajax-content > div > div.main_content.ui_column.is-12 > div > div > div > div > div > div > div > div > div.ui_column.is-3-desktop.is-3-tablet.is-4-mobile.thumbnail-column > div > div.frame > div > div.aspect.is-shown-at-mobile.is-hidden-tablet > div')
                img_urls[m] = img_urls[m].get_attribute("style")  # 음식점 사진의 주소값들이 리스트로 들어감
                img_urls[m] = img_urls[m].lstrip('background-image: url("')  # 정제
                img_urls[m] = img_urls[m].rstrip('");')                      # 정제
                self.food[i][m].append(img_urls[m])           # [['군산'],['군산횟집'],['사진URL']]


    def lodgement_crawling(self):
        for i in range(len(self.regionNames)):
            URL = 'https://www.tripadvisor.co.kr/Search?q='+self.regionNames[i]
            self.driver.get(URL)     # 지역 URL 들어감
            self.lodgment.append([])      # 시별 구분
            self.driver.implicitly_wait(100)  # 잠깐 대기
            element = self.driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[2]/a')   # 배너 선택
            self.driver.execute_script("arguments[0].click();",element)      # 클릭
            self.driver.implicitly_wait(100)  # 잠깐 대기
            restaurants = self.driver.find_elements_by_css_selector('.result-title')        # 음식점 이름들 select
            for m in range(len(restaurants)):
                self.lodgment[i].append([])         # 음식점 개수만큼 리스트 추가   [[]]// [[],[]]
                self.lodgment[i][m] = [self.regionNames[i], restaurants[m].text]    # food = [['군산', '군산횟집'],[...,...]]
                img_urls = self.driver.find_elements_by_css_selector('#BODY_BLOCK_JQUERY_REFLOW > div.page > div > div.ui_container.main_wrap > div > div > div > div > div.content_column.ui_column.is-9-desktop.is-12-tablet.is-12-mobile > div > div.ui_columns.sections_wrapper > div > div.prw_rup.prw_search_search_results.ajax-content > div > div.main_content.ui_column.is-12 > div > div > div > div > div > div > div > div > div.ui_column.is-3-desktop.is-3-tablet.is-4-mobile.thumbnail-column > div > div.frame > div > div.aspect.is-shown-at-mobile.is-hidden-tablet > div')
                img_urls[m] = img_urls[m].get_attribute("style")  # 음식점 사진의 주소값들이 리스트로 들어감
                img_urls[m] = img_urls[m].lstrip('background-image: url("')  # 정제
                img_urls[m] = img_urls[m].rstrip('");')                      # 정제
                self.lodgment[i][m].append(img_urls[m])           # [['군산'],['군산횟집'],['사진URL']]

    def enjoylist_crawling(self):
        for i in range(len(self.regionNames)):
            URL = 'https://www.tripadvisor.co.kr/Search?q='+self.regionNames[i]
            self.driver.get(URL)     # 지역 URL 들어감
            self.enjoylist.append([])      # 시별 구분
            self.driver.implicitly_wait(100)  # 잠깐 대기
            element = self.driver.find_element_by_xpath('//*[@id="search-filters"]/ul/li[4]/a')   # 배너 선택
            self.driver.execute_script("arguments[0].click();",element)      # 클릭
            self.driver.implicitly_wait(100)  # 잠깐 대기
            restaurants = self.driver.find_elements_by_css_selector('.result-title')        # 음식점 이름들 select
            for m in range(len(restaurants)):
                self.enjoylist[i].append([])         # 음식점 개수만큼 리스트 추가   [[]]// [[],[]]
                self.enjoylist[i][m] = [self.regionNames[i], restaurants[m].text]    # food = [['군산', '군산횟집'],[...,...]]
                img_urls = self.driver.find_elements_by_css_selector('#BODY_BLOCK_JQUERY_REFLOW > div.page > div > div.ui_container.main_wrap > div > div > div > div > div.content_column.ui_column.is-9-desktop.is-12-tablet.is-12-mobile > div > div.ui_columns.sections_wrapper > div > div.prw_rup.prw_search_search_results.ajax-content > div > div.main_content.ui_column.is-12 > div > div > div > div > div > div > div > div > div.ui_column.is-3-desktop.is-3-tablet.is-4-mobile.thumbnail-column > div > div.frame > div > div.aspect.is-shown-at-mobile.is-hidden-tablet > div')
                img_urls[m] = img_urls[m].get_attribute("style")  # 음식점 사진의 주소값들이 리스트로 들어감
                img_urls[m] = img_urls[m].lstrip('background-image: url("')  # 정제
                img_urls[m] = img_urls[m].rstrip('");')                      # 정제
                self.enjoylist[i][m].append(img_urls[m])           # [['군산'],['군산횟집'],['사진URL']]

    def picture_downlode(self):
        # 음식점부터 etc[2]
        for i in range(len(self.regionNames)):       # ['군산','정읍'...]
            for j in range(len(self.food[i])):    # ['군산횟집','이성당']
                    imgURL = self.food[i][j][2]           # 주소
                    urllib.request.urlretrieve(imgURL, f'./전라북도/'+self.regionNames[i]+'/'+self.etc[2]+'/'+self.food[i][j][1] +'.jpg')      # .전라북도/군산/음식점/군산횟집.jpg
            for j in range(len(self.lodgment[i])):
                    imgURL = self.lodgment[i][j][2]  # 주소
                    urllib.request.urlretrieve(imgURL, f'./전라북도/' + self.regionNames[i] + '/' + self.etc[1] + '/' +self.lodgment[i][j][1] + '.jpg')
            for j in range(len(self.enjoylist[i])):
                    imgURL = self.enjoylist[i][j][2]  # 주소
                    urllib.request.urlretrieve(imgURL, f'./전라북도/' + self.regionNames[i] + '/' + self.etc[3] + '/' +self.enjoylist[i][j][1] + '.jpg')

    def bestRegion_crawling(self):
        URLs = [
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01w6gz&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720#ttdm=35.839254_126.576647_10&ttdmf=%252Fg%252F1tpg_n0w',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01w6hs&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAxdzZocxIJ7J217IKw7Iuc',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01w961&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAxdzk2MRIJ7KCE7KO87Iuc',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0233v8&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzN2OBIJ7JmE7KO86rWw,',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0233r7&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzNyNxIJ7KeE7JWI6rWw',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0233ss&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzNzcxIJ66y07KO86rWw',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0231qx&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzFxeBIJ6rmA7KCc7Iuc',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0233nj&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzNuahIJ67aA7JWI6rWw',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0231v8&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzF2OBIJ7KCV7J2N7Iuc',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0233pm&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzNwbRIJ7J6E7Iuk6rWw',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F03s5kd&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAzczVrZBIJ7J6l7IiY6rWw',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0233nx&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzNueBIJ6rOg7LC96rWw',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0233t4&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzN0NBIJ7Iic7LC96rWw',
            'https://www.google.com/travel/things-to-do?g2lb=2502548%2C2503770%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4518326%2C4536454%2C4545890%2C4554491%2C4562607%2C4564872%2C4570416%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0233mc&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjoqvC1wI_xAhXDPXAKHZT4BpIQuL0BMAF6BAgFEBo&cshid=1623412070087720&tcfs=EhYKCS9tLzAyMzNtYxIJ64Ko7JuQ7Iuc'
        ]
        for i in range(len(self.regionNames)):
            self.bestRegion.append([])      # [[]]
            self.driver.get(URLs[i])
            self.driver.implicitly_wait(100)
            # elem = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/div[1]/div/div/input')
            # elem.clear()
            # elem.send_keys(self.regionNames[i])
            # elem.send_keys(Keys.RETURN)
            bestRegionNames = self.driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/c-wiz/div/div/div/div/c-wiz/div/div/div/div/div/div/div/div/div/div/div')
            scopePoints = self.driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/c-wiz/div/div/div/div/c-wiz/div/div/div/div/div/div/div/div/div/div/span/span/span')
            imgURLs = self.driver.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/c-wiz/div/div/div/div/c-wiz/div/div/div/div/div/div/div/div/div/easy-img/img')
            k = 0
            for j in range(len(bestRegionNames)):  # 명소이름 개수만큼 돈다.
                bestRegionName = bestRegionNames[j].text  # 선유도
                try:
                    scopePoint = scopePoints[k].text        # 범위 넘어갈 경우
                except:
                    scopePoint=""       # 평점은 없다.
                k += 2
                imgURL = imgURLs[j].get_attribute('src')        # 주소값만 불러와서 저장
                self.bestRegion[i].append([])      # [[[],[]],[[]]]
                self.bestRegion[i][j] = [self.regionNames[i], bestRegionName, imgURL, scopePoint]       # ['군산','철길마을',URL주소,4.3]

    def bestRegion_downlode(self):
        for i in range(len(self.regionNames)):       # ['군산','정읍'...]
            for j in range(len(self.bestRegion[i])):    # 군산의 개수만큼, 전주의 개수만큼
                    imgURL = self.bestRegion[i][j][2]           # URL 주소
                    try:
                        urllib.request.urlretrieve(imgURL, f'./전라북도/'+self.regionNames[i]+'/'+self.etc[0]+'/'+self.bestRegion[i][j][1] +'.jpg')      # .전라북도/군산/지역명소/군산횟집.jpg
                    except:
                        pass






# driver.quit()       # 창 닫기

if __name__ == '__main__':
    regionNames = ['군산', '익산', '전주', '완주', '진안', '무주', '김제', '부안', '정읍', '임실', '장수', '고창', '순창', '남원']

    h = HowThat(regionNames)    # 원하는 지역 인풋
    h.makeFolder()  # 폴더 생성
    h.food_crawling()    # 크롤링
    h.lodgement_crawling()   # 크롤링
    h.enjoylist_crawling()  # 크롤링
    h.picture_downlode()    # 앞의 세개 크롤링 사진 다운
    h.bestRegion_crawling() # 지역 명소 크롤링
    h.bestRegion_downlode()   # 지역 명소 크롤링 사진 다운
