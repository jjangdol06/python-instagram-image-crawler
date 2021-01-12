from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import shutil

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('태그 : ')
url = baseUrl + quote_plus(plusUrl)

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get(url)

time.sleep(3)

# 자동 로그인
ID = 'id_' #인스타그램 ID 작
PW = 'password' #인스타그램 PW성 작

#화면 띄우기
# browser = webdriver.Chrome('./chromedriver')
driver.get("https://instagram.com")

#로딩하는 시간 기다리기
time.sleep(2)

#Login ID 속성값 찾고 입력하기
login_id = driver.find_element_by_name('username')
login_id.send_keys(ID)

#Login PW 속성값 찾기 입력하기
login_pw = driver.find_element_by_name('password')
login_pw.send_keys(PW)
login_pw.send_keys(Keys.RETURN)
time.sleep(5)

#로그인 정보 저
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
time.sleep(5)

#검색할 해쉬태그 url
driver.get(url)
time.sleep(3)

#크롤링+이미지 저장
html = driver.page_source
soup = BeautifulSoup(html)
imglist = []

for j in range(0, 10000):
	insta = soup.select('.v1Nh3.kIKUG._bz0w')

	for i in insta:
		# 인스타 주소에 i번 째의 a태그의 href 속성을 더하여 출력한다.
		print('https://www.instagram.com' + i.a['href'])
		# 인스타 페이지 소스에서 이미지에 해당하는 클래스의 이미지 태그의 src 속성을 imgUrl에 저장한다.
		imgUrl = i.select_one('.KL4Bh').img['src']
		imglist.append(imgUrl)
		imglist = list(set(imglist))
		html = driver.page_source
		soup = BeautifulSoup(html)
		insta = soup.select('.v1Nh3.kIKUG._bz0w')
	print(j)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(2)

n = 0
print(imglist)
for i in range(0, 1000):
	image_url = imglist[n]
	resp = requests.get(image_url, stream=True)
	local_file = open('./img/' + plusUrl + str(n) + 'jpg', 'wb')
	resp.raw.decode_content = True
	shutil.copyfileobj(resp.raw, local_file)
	n+=1
	del resp

# 마지막에 driver를 닫아준다. (열린 창을 닫는다.)
driver.close()
