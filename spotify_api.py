import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "d02248b48d914f17901127aa10bafe60"
CLIENT_SECRET = "540562209057401ebee0e5126b83c81c"

auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(auth_manager=auth_manager)


def get_playlist_tracks(playlist_url):
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    
    all_tracks = []
    
    for item in tracks:
        track = item['track']
        if track:
            all_tracks.append({
                "id": track['id'],
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "popularity": track['popularity']
            })
    
    return all_tracks


def get_audio_features(track_ids):
    features = sp.audio_features(track_ids)
    return features