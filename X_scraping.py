# Imports
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os, time, random, datetime, re

# Dates
last_date = 1705926595
date_now = int(datetime.datetime.now().timestamp())

# Users list, you just paste users that you want to read.
users_list = [
'github',
'culturaltutor',
]

# Nitter instances. Some are down sometimes, so maybe you have to change it periodically.
instance_pages = [
#'https://nitter.net/',
'https://nitter.unixfox.eu/',
]

def extract_date(div):
  try:
    return div.find_elements(By.CSS_SELECTOR,value='.tweet-header span.tweet-date a')[0].text
  except:
    return 'xxx'
    
def extract_link(div):
  return div.find_elements(By.CSS_SELECTOR,value='a.tweet-link')[0].get_attribute("href")
  
def extract_text(div):
  return div.find_elements(By.CSS_SELECTOR,value='.tweet-content.media-body')[0].text

def regist_hour(date):
  if 'h' in date:
    return int(re.search('(\d+)', date).group(1)) * 3600
  if 'm' in date:
    return int(re.search('(\d+)', date).group(1)) * 60
  else:
    return 100375000

def nitter():
  time.sleep(2)
  tweets = browser.find_elements(By.XPATH,value="/html/body/div/div/div[3]/div/div")
  divs = len(tweets)
  for i in tweets[:-2]:
    date = extract_date(i)
    if date[0].isdigit():
      seconds = regist_hour(date)
      # Check if Tweet's timestamp is before or after the last time the code was executed
      if (date_now - seconds) >= last_date:
        link = extract_link(i)
        status = extract_text(i)
        print(date,link)
        print(status.lstrip().rstrip().replace('\n',' ').replace('\t',' '))
        print('\n')

# Open Selenium      
browser = webdriver.Firefox()

# Enumerate users in Terminal
number = 0
for usr in users_list[:]:
  # User name in Terminal with hash around.
  separator = '#' * (len(usr) + 6)
  print(f"{number}\n{separator}\n## {usr} ##\n{separator}\n")
  
  server = random.choice(instance_pages)
  address = server+usr+"/with_replies"
  # Open User page
  browser.get(address)
  # Extract new tweets
  nitter()
  browser.find_elements(By.CSS_SELECTOR,value='body')[0].send_keys(Keys.PAGE_DOWN)
  try:
    browser.find_elements(By.CSS_SELECTOR,value='.show-more a')[0].click()
    nitter()
    print('\n')  
    number += 1  
  except IndexError:
    # Sometimes User has Protected tweets
    print('\n')
    print('IndexError: list index out of range || Protected tweets??')

# Close Selenium    
browser.close()

with open('X_scraping.py', 'r') as f:
  data = f.readlines()
data[9] = f"last_date = {date_now}\n"
with open('X_scraping.py', 'w') as file:
  file.writelines(data)
