# Imports
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio, datetime

# Fechas
last_date = 1705927391
date_now = int(datetime.datetime.now().timestamp())

async def twitch_example(channels):
  twitch = await Twitch(YOUR_ID, YOUR_SECRET)
  for channel in channels_list:
    try:
      channel_videos = await first(twitch.get_videos(user_id=channel))
      ch_videos = channel_videos.to_dict()
      channel_name = ch_videos['user_name']
      hashes = '#' * (len(str(channel_name)) + 6)
      string = ch_videos['created_at']
      date_video = datetime.datetime.strptime(string[0:10],"%Y-%m-%d").timestamp()  
      hour = (int(string[11:13]) * 3600) + (int(string[14:16]) * 60) + (int(string[17:19]))
      if((date_video + hour) >= last_date):
        name_video = ch_videos['title']
        url = ch_videos['url']
        created = datetime.datetime.strptime(string[0:10],"%Y-%m-%d")
        duration = ch_videos['duration']
        print(f"{name_video} {created} {duration} de ##{channel_name}##\n{url}\n\n")
    except:
      continue

channels_list = [
22510310, # gamesdonequick
163299585, # blastpremier
124425627, # lpl
]

asyncio.run(twitch_example(channels_list))

with open('TW_scraping.py', 'r') as f:
  data = f.readlines()
data[6] = f"last_date = {date_now}\n"
with open('TW_scraping.py', 'w') as file:
    file.writelines(data)
