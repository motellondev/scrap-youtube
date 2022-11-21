from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import json
import time

# Setting webdriver
options = Options()
options.binary_location = '/usr/bin/brave-browser'
driver = webdriver.Chrome(options = options)
driver.get("https://www.youtube.com/c/AlexMotellon/videos")

# Accepting cookies
cookies = driver.find_element(By.CSS_SELECTOR, '[aria-label="Aceptar todo"]') # Accept All
cookies.click()
time.sleep(1)

# Scrolling down
element_html = driver.find_element(By.TAG_NAME, 'html')
driver.implicitly_wait(1)
for i in range(2): # Increase range depending on the number of videos in the channel
	element_html.send_keys(Keys.END)
	time.sleep(1)

# Getting all videos (URL & Thumbnail)
videos = driver.find_elements(By.ID, "thumbnail")
titles = driver.find_elements(By.ID, "video-title-link")

# Filtering empty elements
videos = list(filter(lambda video: (video.get_attribute("href") != None), videos))
titles = list(filter(lambda title: (title.get_attribute("title") != ""), titles))

# Creating dict and list
videos_list = []
for video, title in zip(videos,titles):
	url = video.get_attribute("href")
	title = title.get_attribute("title")
	video_dict = {"url":url, "title":title}
	# print(video_dict)
	videos_list.append(video_dict)

# Writting list in a json file
with open('data.json', 'w') as f:
    json.dump(videos_list, f, indent=2)
  
driver.quit()