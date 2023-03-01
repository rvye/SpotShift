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

import sys
import time
import requests as req
import random as rdm
import spotipy as sp
import csv
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



print(" ___           _   ___ _    _  __ _\n/ __|_ __  ___| |_/ __| |_ (_)/ _| |_\n\\__ \ '_ \/ _ \\  _\\__ \\ ' \| |  _|  _|\n|___/ .__/\\___/\\__|___/_||_|_|_|  \__|     \n    |_|                               ")


sshft = int(input("Select a source to transfer from: \n[1] Spotify to Apple Music\n[2] Apple Music to Spotify\n\n[0] Quit\n\n"))

def transferToSpotify(url):
    print("AAPL")
def transferToAAPL(url):
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
                [artist["name"] for artist in track["track"]["artists"]]
            )

            # write to csv
            writer.writerow([name, artists])
            print([name, artists])

    # Transferring to apple music
if sshft == 1:
    transferToAAPL(input("Paste your playlist link here: "))
elif sshft == 2:
    transferToSpotify("aapl")
elif sshft == 0:
    sys.exit()
else:
    print("Enter a valid number.")
