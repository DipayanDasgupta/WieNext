import requests
from bs4 import BeautifulSoup

def fetch_recommended_videos(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    videos = []
    for video in soup.select('a#video-title'):
        title = video['title']
        link = f"https://www.youtube.com{video['href']}"
        videos.append({'title': title, 'link': link})
    return videos

# Example usage
# print(fetch_recommended_videos('Python programming for beginners'))
