import os
import sys
import urllib.request
import json
import pandas as pd

client_id = "QJtS6W2l_Z6GFq_IzBXx" # 개발자센터에서 발급받은 Client ID 값
client_secret = "1M_PYmo3Pt" # 개발자센터에서 발급받은 Client Secret 값
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
source = 'en'
target = 'ko'

d = pd.read_excel('refined_datafile.xlsx', index_col=0)
# d.iloc[i][1] 로 i행 선택

d2 = pd.read_excel('d.xlsx')

# 하루 3개가 최대치다.
for i in range(5):
    text = d.iloc[i][1]
    # text = 'hello'
    # text = "Dear local newspaper, I think effects computers have on people are great learning skills/affects because they give us time to chat with friends/new people, helps us learn about the globe(astronomy) and keeps us out of troble! Thing about! Dont you think so? How would you feel if your teenager is always on the phone with friends! Do you ever time to chat with your friends or buisness partner about things. Well now - there's a new way to chat the computer, theirs plenty of sites on the internet to do so: @ORGANIZATION1, @ORGANIZATION2, @CAPS1, facebook, myspace ect. Just think now while your setting up meeting with your boss on the computer, your teenager is having fun on the phone not rushing to get off cause you want to use it. How did you learn about other countrys/states outside of yours? Well I have by computer/internet, it's a new way to learn about what going on in our time! You might think your child spends a lot of time on the computer, but ask them so question about the economy, sea floor spreading or even about the @DATE1's you'll be surprise at how much he/she knows. Believe it or not the computer is much interesting then in class all day reading out of books. If your child is home on your computer or at a local library, it's better than being out with friends being fresh, or being perpressured to doing something they know isnt right. You might not know where your child is, @CAPS2 forbidde in a hospital bed because of a drive-by. Rather than your child on the computer learning, chatting or just playing games, safe and sound in your home or community place. Now I hope you have reached a point to understand and agree with me, because computers can have great effects on you or child because it gives us time to chat with friends/new people, helps us learn about the globe and believe or not keeps us out of troble. Thank you for listening."
    encText = urllib.parse.quote(text)
    data = "source={}&target={}&text=".format(source,target) + encText
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        decode = json.loads(response_body.decode('utf-8'))    
        result = decode['message']['result']['translatedText']    
        d2.loc[len(d2)] = result
        d2.to_excel('d2.xlsx')
        
    else:
        print("Error Code:" + rescode)







# 해야할 일 
# 1. 파일 불러와서
# 2. for <판다스로 한행씩 번역한 후
# 3. 판다스 데이터 프레임에 다 넣는다.>
# 4. 해당 데이터 프레임 열 추가 후, 엑셀로 저장한다.