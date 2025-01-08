import requests

# YouTube API Configuration
API_KEY = 'YOUR_YOUTUBE_API_KEY'
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

def get_youtube_recommendations(query, max_results=5):
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': API_KEY,
        'maxResults': max_results
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        videos = []
        for item in data['items']:
            video = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            videos.append(video)
        return videos
    else:
        return []

# Example Usage
# print(get_youtube_recommendations('Python programming for beginners'))
