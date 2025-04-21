import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

def spotify_login():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="-",
        scope="playlist-modify-public",
        cache_path="token.txt"
    ))

def get_billboard_songs(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    titles = soup.select("li h3")
    songs = [title.get_text(strip=True) for title in titles][:100]
    return songs

def search_songs(sp, songs):
    uris = []
    for song in songs:
        result = sp.search(q=song, type="track", limit=1)
        tracks = result["tracks"]["items"]
        if tracks:
            uris.append(tracks[0]["uri"])
    return uris

def create_playlist(sp, user_id, name, uris):
    playlist = sp.user_playlist_create(user=user_id, name=name, public=True)
    sp.playlist_add_items(playlist_id=playlist["id"], items=uris)
    return playlist
