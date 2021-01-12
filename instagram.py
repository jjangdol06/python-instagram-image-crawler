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
ID = 'chalna_studio_' #인스타그램 ID
PW = 'dogkite33*' #인스타그램 PW

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

# save login info
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
time.sleep(5)

#reloate to hashtag
driver.get(url)
time.sleep(3)
#####

# html = driver.page_source
# soup = BeautifulSoup(html)
# imglist = []

# for i in range(0, 100):
# 	insta = soup.select('.v1Nh3.kIKUG._bz0w')

# 	for i in insta:
# 		print('https://www.instagram.com' + i.a['href'])
# 		imgUrl = i.select_one('.KL4Bh').img['src']
# 		imglist.append(imgUrl)
# 		imglist = list(set(imglist))
# 		html = driver.page_source
# 		soup = BeautifulSoup(html)
# 		insta = soup.select('.v1Nh3.kIKUG._bz0w')

# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 	time.sleep(2)

# n=0
# for i in range(0,6000):
# 	image_url = imglist[n]
# 	resp = requests.get(image_url, stream=True)
# 	local_file = open('./img/' + plusUrl + str(n) + '.jpg', 'wb')
# 	resp.raw.decode_content = True
# 	shutil.copyfileobj(resp.raw, local_file)
# 	n+=1
# 	del resp

# driver.close()

# select는 페이지에 있는 정보를 다 가져 온다.
# 클래스가 여러 개면 기존 클래스의 공백을 없애고 .으로 연결시켜 주어야 한다.
# insta = soup.select('.v1Nh3.kIKUG._bz0w')

n = 1
for j in range(0, 100):
	html = driver.page_source
	soup = BeautifulSoup(html)
	insta = soup.select('.v1Nh3.kIKUG._bz0w')

	for i in insta:
		# 인스타 주소에 i번 째의 a태그의 href 속성을 더하여 출력한다.
		print('https://www.instagram.com' + i.a['href'])
		# 인스타 페이지 소스에서 이미지에 해당하는 클래스의 이미지 태그의 src 속성을 imgUrl에 저장한다.
		imgUrl = i.select_one('.KL4Bh').img['src']
		with urlopen(imgUrl) as f:
			# img라는 폴더 안에 programmer(n).jpg 파일을 저장한다.
			# 텍스트 파일이 아니기 때문에 w(write)만 쓰면 안되고 binary 모드를 추가시켜야 한다.
			with open('./img/' + plusUrl + str(n) + '.jpg', "wb") as h:
				# f를 읽고 img에 저장한다.
				img = f.read()
				# h에 위 내용을 쓴다.
				h.write(img)
		# 계속 programmer 1에 덮어쓰지 않도록 1을 증가시켜 준다
		n += 1
		print(imgUrl)
		# 출력한 걸 보았을 때 구분하기 좋도록 빈 줄을 추가시킨다.
		print()
	print(j)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(2)


# 마지막에 driver를 닫아준다. (열린 창을 닫는다.)
driver.close()s
