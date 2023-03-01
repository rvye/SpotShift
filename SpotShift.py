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
# Used for transferring Spotify playlists to Apple Music (or vice-versa)
#
# https://github.com/rvye/spotshift

#!usr/bin/env python
# -*- coding: utf-8 -*-

from ytmusicapi import YTMusic
import requests as req
import spotipy as sp
import csv
import sys
import os
import re
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# load_dotenv()

# CLIENT_ID = os.getenv("CLIENT_ID", "")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
CLIENT_ID = "d92022b036d5409198689c7719bd123c"
CLIENT_SECRET = "3a85d8d5b7a14e6383935de817a21043"

client_credentials_manager = SpotifyClientCredentials(
  client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

session = sp.Spotify(client_credentials_manager=client_credentials_manager)

print(
  " ___           _   ___ _    _  __ _\n/ __|_ __  ___| |_/ __| |_ (_)/ _| |_\n\\__ \ '_ \/ _ \\  _\\__ \\ ' \| |  _|  _|\n|___/ .__/\\___/\\__|___/_||_|_|_|  \__|     \n    |_|                               "
)


def dev(url):
  # Reading from playlist
    music = YTMusic("headers_auth.json")

    playlist = music.create_playlist("Playlist Transferred from SpotShift", "https://github.com/rvye/spotshift")
  
  if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", url):
    playlist_uri = match.groups()[0]
  else:
    raise ValueError("Expected format: https://open.spotify.com/playlist/...")

  tracks = session.playlist_tracks(playlist_uri)["items"]

  with open("a.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    # write header column names
    writer.writerow(["track", "artist"])

    # extract name and artist
    for track in tracks:
      name = track["track"]["name"]
      artists = ", ".join(
        [artist["name"] for artist in track["track"]["artists"]])

      # write to csv
      writer.writerow([name, artists])
      print([name, artists])

      music.add_playlist_items(playlist, [name, artists])
  

  

# sshft = int(input("Select a source to transfer from: \n\n[1] Spotify to Apple Music\n[2] Spotify to Youtube Music\n[3] Apple Music to Spotify\n[4] Apple Music to YouTube Music\n[5] YouTube Music to Spotify\n[6] YouTube Music to Apple Music\n\n[0] Quit\n\n"))
sshft = 2


def transferToSpotifyAAPL(url):
  print("AAPL")


def transferToSpotifyGOOG(url):
  print(url)


def transferToGOOGaapl():
  print("GA")


def transferToGOOGspotify(url):
  # Reading from playlist
  if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", url):
    playlist_uri = match.groups()[0]
  else:
    raise ValueError("Expected format: https://open.spotify.com/playlist/...")

  tracks = session.playlist_tracks(playlist_uri)["items"]

  with open("a.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    # write header column names
    writer.writerow(["track", "artist"])

    # extract name and artist
    for track in tracks:
      name = track["track"]["name"]
      artists = ", ".join(
        [artist["name"] for artist in track["track"]["artists"]])

      # write to csv
      writer.writerow([name, artists])
      print([name, artists])

  # req.post()


def transferToAAPLgoog(url):
  print(url)


def transferToAAPLspot(url):
  print(url)


if sshft == 1:
  # transferToAAPL(input("Paste your playlist link here: "))
  transferToAAPLspot("a")
elif sshft == 2:
  #transferToGOOGspotify(input("Paste your playlist link here: "))

  dev()
elif sshft == 3:
  transferToSpotifyAAPL("apple to spotify")
elif sshft == 4:
  transferToGOOGaapl("apple to google")
elif sshft == 5:
  transferToSpotifyGOOG("yt to spot")
elif sshft == 6:
  transferToAAPLgoog("youtube to apple")
elif sshft == 0:
  sys.exit()
else:
  print("Enter a valid number.")
