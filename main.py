import random
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '37e244d77b054f80909cfa3fb306c0a8'
CLIENT_SECRET = 'ee786be6b77f4fb29c7e4620737db52a'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

def get_random_song(playlist_id):
    try:
        tracks = sp.playlist_tracks(playlist_id)['items']

        if not tracks:
            return "플레이리스트에서 노래를 찾을 수 없습니다."

        random_track = random.choice(tracks)['track']

        return (f"🎵 랜덤으로 추천된 노래 🎵\n"
                f"제목: {random_track['name']}\n"
                f"아티스트: {', '.join(artist['name'] for artist in random_track['artists'])}\n"
                f"앨범: {random_track['album']['name']}\n"
                f"[노래 듣기]({random_track['external_urls']['spotify']})")

    except Exception as e:
        return f"API 요청 중 오류가 발생했습니다: {e}"

def music_info():
    while True:
        song_name = input("검색하고 싶으신 노래 제목을 입력하세요 (종료: exit): ").strip()
        if song_name.lower() == "exit":
            print("프로그램 종료")
            break

        results = sp.search(q=song_name, limit=1, type="track")
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            print("\n[노래 정보]")
            print(f"제목: {track['name']}")
            print(f"아티스트: {', '.join(artist['name'] for artist in track['artists'])}")
            print(f"앨범: {track['album']['name']}")
            print(f"발매일: {track['album']['release_date']}")
            print(f"미리 듣기: {track['preview_url'] if track['preview_url'] else '미리 듣기 불가'}")
            print(f"Spotify 링크: {track['external_urls']['spotify']}")
        else:
            print("❌ 해당 노래를 찾을 수 없습니다.")
            
            
def playlist_info():
     while True:
        playlist_id = input("플레이리스트 ID를 입력하세요.(종료 : exit): ").strip()
        if playlist_id.lower() == "exit":
            print("프로그램 종료")
            break

        try:
            playlist = sp.playlist(playlist_id)
            print("\n[플레이리스트 정보]")
            print(f"이름: {playlist['name']}")
            print(f"설명: {playlist['description']}")
            print(f"총 트랙 수: {playlist['tracks']['total']}")
            print(f"Spotify 링크: {playlist['external_urls']['spotify']}")
        except Exception as e:
            print(f"❌ 해당 플레이리스트를 찾을 수 없습니다: {e}")

def Artist_Info():
    while True:
        artist_name = input("아티스트 이름을 입력하세요 (종료: exit): ").strip()
        if artist_name.lower() == "exit":
            print("프로그램 종료")
            break

        try:
            results = sp.search(q=artist_name, limit=1, type="artist")
            if results['artists']['items']:
                artist = results['artists']['items'][0]
                print("\n[아티스트 정보]")
                print(f"이름: {artist['name']}")
                print(f"장르: {', '.join(artist['genres']) if artist['genres'] else '정보 없음'}")
                print(f"팔로워 수: {artist['followers']['total']:,}")
                print(f"Spotify 링크: {artist['external_urls']['spotify']}")
            else:
                print("❌ 해당 아티스트를 찾을 수 없습니다.")
        except Exception as e:
            print(f"❌ 아티스트 정보를 가져오는 중 오류가 발생했습니다: {e}")

            

def main():
    Command_list = ["PlaylistRandomRCMD", "MusicInfo", "PlaylistInfo","ArtistInfo"]
    Command_name = input("명령어 입력 (PlaylistRandomRCMD / MusicInfo / PlaylistInfo/ ArtistInfo): ").strip()

    if Command_name not in Command_list:
        print("명령어를 찾을 수 없습니다.")
        sys.exit()

    if Command_name == "PlaylistRandomRCMD":
        playlist_id = input("플레이리스트 ID를 입력하세요: ").strip()
        song_info = get_random_song(playlist_id)
        print(song_info)
    elif Command_name == "MusicInfo":
        music_info()
    elif Command_name == "PlaylistInfo":
        playlist_info()
    elif Command_name == "ArtistInfo":
        Artist_Info()
        
        

if __name__ == '__main__':
    main()
