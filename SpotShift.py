#  _____             _   _____ _     _  __ _
# /  ___|           | | /  ___| |   (_)/ _| |
# \ `--. _ __   ___ | |_\ `--.| |__  _| |_| |_
#  `--. \ '_ \ / _ \| __|`--. \ '_ \| |  _| __|
# /\__/ / |_) | (_) | |_/\__/ / | | | | | | |_
# \____/| .__/ \___/ \__\____/|_| |_|_|_|  \__|
#       | |
#       |_|

# SpotShift.py
# by rvye (rvyeinq@gmail.com)
#
# Used for transferring playlists between Spotify and YouTube Music
#
# https://github.com/rvye/spotshift

#!usr/bin/env python
# -*- coding: utf-8 -*-

from ytmusicapi import YTMusic
import spotipy as sp
import sys
import os
import re
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")

client_credentials_manager = SpotifyClientCredentials(
  client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

session = sp.Spotify(client_credentials_manager=client_credentials_manager)

print(
  " ___           _   ___ _    _  __ _\n/ __|_ __  ___| |_/ __| |_ (_)/ _| |_\n\\__ \ '_ \/ _ \\  _\\__ \\ ' \| |  _|  _|\n|___/ .__/\\___/\\__|___/_||_|_|_|  \__|     \n    |_|                               "
)
# sshft = int(input("Select a source to transfer from: \n\n[1] Spotify to YouTube Music\n[2] YouTube Music to Spotify\n\n[0] Quit\n\n"))
sshft = 2

def transferToSpotify(url):
  id = url[40:1000]
  
  music = YTMusic("headers_auth.json")

  # a = music.get_playlist(id)
  print(id)
  
def transferToYTM(url):
  music = YTMusic("headers_auth.json")

  playlist = music.create_playlist("Playlist Transferred from SpotShift", "https://github.com/rvye/spotshift")
  
  # Reading from playlist
  if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", url):
    playlist_uri = match.groups()[0]
  else:
    raise ValueError("Expected format: https://open.spotify.com/playlist/...")

  tracks = session.playlist_tracks(playlist_uri)["items"]

  # extract name and artist
  for track in tracks:
    name = track["track"]["name"]
    artists = ", ".join(
      [artist["name"] for artist in track["track"]["artists"]])

    results = music.search(name)
    music.add_playlist_items(playlist, [results[0]['videoId']])


if sshft == 1:
  try:
    transferToYTM(input("Paste your playlist link here: "))
  except:
    print("An error occured... Maybe you pasted an invalid playlist link?
    
elif sshft == 2:
  try:
    transferToSpotify(input("Paste your playlist link here: "))
  except:
    print("An error occured... Maybe you pasted an invalid playlist link?"
          
elif sshft == 0:
  sys.exit()
else:
  print("Enter a valid number.")
