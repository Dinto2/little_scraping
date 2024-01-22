# Imports
import requests, re, datetime

# Fechas
date_now = int(datetime.datetime.now().timestamp())
last_date = 1705926311

# Channels list. Use "videos/streams/shorts" sections
channels_list = [
"https://www.youtube.com/@freecodecamp/videos",
"https://www.youtube.com/@freecodecampespanol/videos",
"https://www.youtube.com/@dwdeutsch/shorts",
"https://www.youtube.com/@BBCWorldService/streams",
]

# Get date from last video. If you use YT in another language, replace
# "año/mes/semana/dia/hora/minuto/segundo" with "Year/month/week/day/hour/minute/second

def get_date(data):
  try:
    years = int(re.search('(\d+) año', data).group(1)) * 31557600
  except:
    years = 0
  try:
    months = int(re.search('(\d+) mes', data).group(1)) * 2629800
  except:
    months = 0
  try:
    weeks = int(re.search('(\d+) semana', data).group(1)) * 604800
  except:
    weeks = 0
  try:
    days = int(re.search('(\d+) día', data).group(1)) * 86400
  except:
    days = 0
  try:
    hours = int(re.search('(\d+) hora', data).group(1)) * 3600
  except:
    hours = 0
  try:
    minutes = int(re.search('(\d+) minuto', data).group(1)) * 60
  except:
    minutes = 0
  try:
    seconds = int(re.search('(\d+) segundo', data).group(1)) * 1
  except:
    seconds = 0
  created = date_now - (years + months + weeks + days + hours + minutes + seconds)
  return created

# Main function
def show(channels):
  strings = ['']
  for i in range(0, (len(channels))):
    try:
      html = requests.get(channels[i]).text
      info = re.search('(?<={"label":").*?(?="})', html).group()
      date_created = get_date(info)
      if(date_created >= last_date):
        strings.append(info)
    except:
      print(channels[i])
  longest = len(max(strings, key=len))
  print("\n".join([f"{string: >{longest}} \n" for string in strings]))

print('\n')
show(channels_list)

with open('YT_scraping.py', 'r') as f:
  data = f.readlines()
data[5] = f"last_date = {date_now}\n"
with open('YT_scraping.py', 'w') as file:
  file.writelines(data)

