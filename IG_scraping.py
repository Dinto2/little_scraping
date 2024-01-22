# Imports
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
import urllib.request as reqq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os, time

# Profiles list
igs_list = [
'codeorangetoth',
'criterioncollection',
'letterboxd',
]

# Functions using different pages to watch instagram without an account
def storiesig_me(ig):
  url = "https://storiesig.me/en/"+ig
  browser.get(url)
  time.sleep(8)
  try:
    posts = browser.find_elements(By.XPATH,value="/html/body/div[1]/div/div[2]/div[7]/div/img")
  except:
    posts = ''
  print(len(posts),url)  
  return len(posts)
  
def instasaved(ig):
  url = "https://instasaved.net/en/save-stories/"+ig
  browser.get(url)
  time.sleep(8)
  try:
    video = browser.find_elements(By.XPATH,value="/html/body/div[3]/div/div[1]/div[2]/div/video")
  except:
    video = ''
  try:
    image = browser.find_elements(By.XPATH,value="/html/body/div[3]/div/div[1]/div[2]/div/img")
  except:
    image = ''
  total = len(video)+len(image)
  if total >= 1:
    print((len(video)+len(image)),url)
  return len(video)+len(image)
  
def instanavigation(ig):
  url = "https://instanavigation.com/user-profile/"+ig
  browser.get(url)
  time.sleep(8)
  try:
    posts = browser.find_elements(By.XPATH,value="/html/body/div/div[3]/div[3]/div[5]/div/div/div/div/img")
  except:
    posts = ''
  print(len(posts),url)  
  return len(posts)

# Functions list. We just have one enabled. We'll iterate over all pages, so we don't want repeat same actions.
pages = [
instasaved,
#storiesig_me,
#instanavigation,
]

# Open Selenium
browser = webdriver.Firefox()
number = 0
for ig in igs_list[:]:
  posts = 0
  print(number,ig)
  for page in pages:
    if posts != 0:
      continue
    else:
      posts = page(ig)
  print('\n')    
  number += 1
browser.close()

