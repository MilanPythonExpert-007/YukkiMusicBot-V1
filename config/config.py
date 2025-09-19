# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import re
import sys

from pyrogram import filters

# Hardcoded values instead of environment variables
API_ID = 24082016  # Replace with your actual API ID
API_HASH = "81af1b2969f06110e0901aa41bfb932d"  # Replace with your actual API HASH

BOT_TOKEN = "8020798464:AAHx6BU_Qi_h_jOD_Hpb8AssQW3iR2vW0HU"  # Replace with your actual bot token

MONGO_DB_URI = "your_mongodb_uri_here"  # Replace with your MongoDB URI or set to None

DURATION_LIMIT_MIN = 60
SONG_DOWNLOAD_DURATION = 180

LOG_GROUP_ID = -1002732848153  # Replace with your actual log group ID

MUSIC_BOT_NAME = "ABHAY X MPX"

OWNER_ID = [5524867269, 8287427230]  # Replace with your actual owner ID(s)

HEROKU_API_KEY = None  # Set to your Heroku API key if needed
HEROKU_APP_NAME = None  # Set to your Heroku app name if needed

UPSTREAM_REPO = "https://github.com/TeamYukki/YukkiMusicBot"
UPSTREAM_BRANCH = "master"

GIT_TOKEN = None

SUPPORT_CHANNEL = "https://t.me/DarkCheckCommunity"  # Replace with your actual channel
SUPPORT_GROUP = "https://t.me/@OSINTinfo_XBot"  # Replace with your actual group

AUTO_LEAVING_ASSISTANT = None
AUTO_LEAVE_ASSISTANT_TIME = 5400
AUTO_SUGGESTION_TIME = 5400
AUTO_DOWNLOADS_CLEAR = None
AUTO_SUGGESTION_MODE = None
PRIVATE_BOT_MODE = None

YOUTUBE_DOWNLOAD_EDIT_SLEEP = 3
TELEGRAM_DOWNLOAD_EDIT_SLEEP = 5

GITHUB_REPO = "https://github.com/TeamYukki/YukkiMusicBot"  # Replace with your repo

SPOTIFY_CLIENT_ID = None  # Set if you have Spotify integration
SPOTIFY_CLIENT_SECRET = None  # Set if you have Spotify integration

VIDEO_STREAM_LIMIT = 3
SERVER_PLAYLIST_LIMIT = 30
PLAYLIST_FETCH_LIMIT = 25

CLEANMODE_DELETE_MINS = 5

TG_AUDIO_FILESIZE_LIMIT = 104857600
TG_VIDEO_FILESIZE_LIMIT = 1073741824

SET_CMDS = False

STRING1 = None  # Replace with your string session if needed
STRING2 = None
STRING3 = None
STRING4 = None
STRING5 = None

#  __     ___    _ _  ___  _______   __  __ _    _  _____ _____ _____   ____   ____ _______
#  \ \   / / |  | | |/ / |/ /_   _| |  \/  | |  | |/ ____|_   _/ ____| |  _ \ / __ \__   __|
#   \ \_/ /| |  | | ' /| ' /  | |   | \  / | |  | | (___   | || |      | |_) | |  | | | |
#    \   / | |  | |  < |  <   | |   | |\/| | |  | |\___ \  | || |      |  _ <| |  | | | |
#     | |  | |__| | . \| . \ _| |_  | |  | | |__| |____) |_| || |____  | |_) | |__| | | |
#     |_|   \____/|_|\_\_|\_\_____| |_|  |_|\____/|_____/|_____\_____| |____/ \____/  |_|


### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
START_IMG_URL = "https://telegra.ph/file/5b2c9f5c5bcc479a8b013.jpg"  # Replace with your start image URL

PING_IMG_URL = "assets/Ping.jpeg"

PLAYLIST_IMG_URL = "assets/Playlist.jpeg"

GLOBAL_IMG_URL = "assets/Global.jpeg"

STATS_IMG_URL = "assets/Stats.jpeg"

TELEGRAM_AUDIO_URL = "assets/Audio.jpeg"

TELEGRAM_VIDEO_URL = "assets/Video.jpeg"

STREAM_IMG_URL = "assets/Stream.jpeg"

SOUNCLOUD_IMG_URL = "assets/Soundcloud.jpeg"

YOUTUBE_IMG_URL = "assets/Youtube.jpeg"

SPOTIFY_ARTIST_IMG_URL = "assets/SpotifyArtist.jpeg"

SPOTIFY_ALBUM_IMG_URL = "assets/SpotifyAlbum.jpeg"

SPOTIFY_PLAYLIST_IMG_URL = "assets/SpotifyPlaylist.jpeg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

# URL validation (kept for any hardcoded URLs)
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if not MUSIC_BOT_NAME.isascii():
    print(
        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."
    )
    sys.exit()
