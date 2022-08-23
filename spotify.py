import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope= 'user-top-read'
auth=spotipy.SpotifyOAuth(scope=scope,show_dialog=True)
smthing=spotipy.Spotify(auth_manager=auth)
time_period=input('Stats from how long ago?\n1 month  6 months  all time:\n')
if time_period.lower()=='1 month':
    time='short_term'
elif time_period.lower()=='6 months':
    time='medium_term'
elif time_period.lower()=='all time':
    time='long_term'
else:
    print('invalid input')
    raise Exception('make sure input is same as options displayed')
top_tracks=smthing.current_user_top_tracks(limit=10,time_range=time)
top_artists=smthing.current_user_top_artists(limit=5,time_range=time)
useful_track=top_tracks['items']
print('TOP SONGS\n')
for item in (useful_track):
    song_artist=item['artists'][0]['name']
    song=item['name']
    print(useful_track.index(item)+1,song+' - '+song_artist)
print('\nTOP ARTISTS\n')
useful_artist=top_artists['items']
for skip in useful_artist:
    artist=skip['name']
    print(useful_artist.index(skip)+1,artist)
