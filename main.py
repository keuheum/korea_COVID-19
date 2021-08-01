from datetime import datetime

import requests
from bs4 import BeautifulSoup

req = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=zhfhsk&qdt=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98")
soup = BeautifulSoup(req.text, "html.parser")
today = datetime.now().strftime('%Y년 %m월 %d일')

print(f"확진자 - {soup.find('li' , class_='info_01').text.split(' ')[3]}명   (전체 확진자 - {soup.find('li' , class_='info_01').text.split(' ')[2]}명)")
print(f"검사중 - {soup.find('li' , class_='info_02').text.split(' ')[3]}명   (전체 검사중 - {soup.find('li' , class_='info_02').text.split(' ')[2]}명)")
print(f"격리해제 - {soup.find('li' , class_='info_03').text.split(' ')[3]}명 (전체 격리해제 - {soup.find('li' , class_='info_03').text.split(' ')[2]}명)")
print(f"사망자 - {soup.find('li' , class_='info_04').text.split(' ')[3]}명     (전체 사망자 - {soup.find('li' , class_='info_04').text.split(' ')[2]}명)")

close = input("창을 닫으려면 엔터키를 눌러주세요")
