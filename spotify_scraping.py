# Imports
import requests, bs4, re

# List of podcasts you'll scrap. Just paste their urls.
podcasts_list = [
"https://open.spotify.com/show/4XPl3uEEL9hvqMkoZrzbx5",
"https://open.spotify.com/show/70rf86wwnaI9aKz73hO3CF",
"https://open.spotify.com/show/7Cvsbcjhtur7nplC148TWy",
"https://open.spotify.com/show/0rOatMqaG3wB5BF4AdsrSX",
"https://open.spotify.com/show/2Shpxw7dPoxRJCdfFXTWLE",
]

def scrap_podcasts(podcasts):
  for i in range(0, len(podcasts)):
    url = requests.get(podcasts[i])
    page = bs4.BeautifulSoup(url.text, features="lxml")
    podcast_title = page.select('title')[0]
    name = re.search("<title>(.*) \|", str(podcast_title)).group(1)  
    episode = page.select('.GUufNEt4tOKYiLgTlfXQ')
    try:
      info = re.search('alt="([#\|\(\)á-úa-zA-Z0-9_ ,:.-]*)"', str(episode)).group(1)  
    except:
      info = re.search("alt='([#\"\|\(\)á-úa-zA-Z0-9_ ,:.-]*)'", str(episode)).group(1)        
    episode_date = page.select('._q93agegdE655O5zPz6l')
    date = re.search('>([á-úa-zA-Z0-9_ ,:.]*)', str(episode_date)).group(1)
    episode_duration = page.select('.pTebN32OH1h3EY5tUJ3d .UyzJidwrGk3awngSGIwv')
    duration = re.search('>([á-úa-zA-Z0-9_ ,:.]*)', str(episode_duration)).group(1)
    print(f'{date}  -  {name}  -  {info}  -  {duration}')
  print('')  

if __name__ == "__main__":
  print('\n')
  scrap_podcasts(podcasts_list)
