import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
import sys

spotify_client_id = ""
spotify_secret_id = ""

SP = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_secret_id))

Playlist_code = input("플레이리스트 코드를 입력하세요: ").strip()
try:
    tracks = SP.playlist_tracks(Playlist_code)['items']
    
    if not tracks:
        print("플레이리스트에서 노래를 찾을 수 없습니다.")
        sys.exit()

    print(f"{Playlist_code} 플레이리스트가 입력되었습니다.")

    random_Track = random.choice(tracks)['track']

    print(f"🎵 랜덤으로 추천된 노래 🎵")
    print(f"제목: {random_Track['name']}")
    print(f"아티스트: {', '.join(artist['name'] for artist in random_Track['artists'])}")
    print(f"앨범: {random_Track['album']['name']}")
    print(f"[노래 듣기]({random_Track['external_urls']['spotify']})")

except Exception as e:
    print(f"오류 발생: {e}")
