import re

import sys

from os import getenv

from dotenv import load_dotenv

from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org

API_ID = int(getenv("API_ID", "25367211"))

API_HASH = getenv("API_HASH", "622c6c7d4a16ab160758b160786b0be6")

## Get it from @Botfather in Telegram.

BOT_TOKEN = getenv("BOT_TOKEN", "6558463329:AAFx_bEQfIvI-kPw0FBBgvzsMsIkwZwnvdk")

# Database to save your chats and stats.

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://gezginbey1:mytmyt4747@cluster0.ha1v0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.

DURATION_LIMIT_MIN = int(

    getenv("DURATION_LIMIT", "760")

)  # Remember to give value in Minutes

# Duration Limit for downloading Songs in MP3 or MP4 format from bot

SONG_DOWNLOAD_DURATION = int(

    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "360")

)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1002352102473))

# A name for your Music bot.

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","ElifMuzikBot")

# Your User ID.

OWNER_ID = list(

    map(int, getenv("OWNER_ID", "6318415383").split())

)  # Input type must be interger

# Get it from http://dashboard.heroku.com/account

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

# For customized or modified Repository

UPSTREAM_REPO = getenv(

    "UPSTREAM_REPO",

    "https://github.com/Meyit47zade/MytMzk-",

)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# GIT TOKEN ( if your edited repo is private)

GIT_TOKEN = getenv("GIT_TOKEN", None)

# Only  Links formats are  accepted for this Var value.

SUPPORT_CHANNEL = getenv(

    "SUPPORT_CHANNEL", "https://t.me/BottDestek") # Example:- https://t.me/ArchBots

SUPPORT_GROUP = getenv(

    "SUPPORT_GROUP", "https://t.me/BizBizeSohbetGrubu")  # Example:- https://t.me/ARCH_SUPPORTS

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "true")

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Time after which bot will suggest random chats about bot commands.

AUTO_SUGGESTION_TIME = int(

    getenv("AUTO_SUGGESTION_TIME", "3400")

)  # Remember to give value in Seconds

# Set it True if you want to delete downloads after the music playout ends from your downloads folder

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo.. Will be shown on /start Command

GITHUB_REPO = getenv("GITHUB_REPO", None) 

# Spotify Client.. Get it from https://developer.spotify.com/dashboard

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2041df9cbcd142cba804578a2cf85939")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "80ffd296320e49299830e80b11e3bf73")

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "10"))

# Maximum Limit Allowed for users to save playlists on bot's server

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

# Cleanmode time after which bot will delete its old messages from chats

CLEANMODE_DELETE_MINS = int(

    getenv("CLEANMODE_MINS", "600")

)  # Remember to give value in Seconds

# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(

    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")

)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(

    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")

)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes

# If you want your bot to setup the commands automatically in the bot's menu set it to true.

# Refer to https://i.postimg.cc/Bbg3LQTG/image.png

SET_CMDS = getenv("SET_CMDS", False)

# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @YukkiStringBot
STRING1 = getenv("STRING_SESSION", "BAGDEqsAdQpm7x2LjV4IYIlD_GE74xiKwGHhtUnK-gigAtgKcKClPWRwNlpcWxFziRRLBpYKMlQAV6LF-F5OSiXVHHaVmd3GF-q2d5mtmLUtvbxnn7-Cpk-th4vP8mlbz8Scz4qT6fh0mqHnB7BAAq54uiaxVV0wJw0cSXsSNf26TbK8EIjyxx8TmV-n7UYNyCO2zRA7Yhc-f-zClg54c3NbNJujKnBbtLBFLFl4buT3RcRpyY1yr2V4iWWZxabBtIGhqRwv1whXCoQ6o2yG7pf-hOm1Dhfj1Qe12aAnN3D6VPUI40RRcXLTPJD7vtT5pWBk2lQs6HjJKWKRqHI57-8wyDEIlAAAAAGg8OtbAA")

STRING2 = getenv("STRING_SESSION2", None)

STRING3 = getenv("STRING_SESSION3", None)

STRING4 = getenv("STRING_SESSION4", None)

STRING5 = getenv("STRING_SESSION5", None)

### DONT TOUCH or EDIT codes after this line

BANNED_USERS = filters.user()

YTDOWNLOADER = 1

LOG = 2

LOG_FILE_NAME = "ArchMusiclogs.txt"

adminlist = {}

lyrical = {}

chatstats = {}

userstats = {}

clean = {}

votemode = {}

confirmer = {}

autoclean = []

# Images

START_IMG_URL = getenv(
     "START_IMG_URL", 
     "https://i.imghippo.com/files/dS0EY1726416364.jpg",
     

)

PING_IMG_URL = getenv(

    "PING_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

PLAYLIST_IMG_URL = getenv(

    "PLAYLIST_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

GLOBAL_IMG_URL = getenv(

    "GLOBAL_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

STATS_IMG_URL = getenv(

    "STATS_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

TELEGRAM_AUDIO_URL = getenv(

    "TELEGRAM_AUDIO_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

TELEGRAM_VIDEO_URL = getenv(

    "TELEGRAM_VIDEO_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

STREAM_IMG_URL = getenv(

    "STREAM_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

SOUNCLOUD_IMG_URL = getenv(

    "SOUNCLOUD_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

YOUTUBE_IMG_URL = getenv(

    "YOUTUBE_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

SPOTIFY_ARTIST_IMG_URL = getenv(

    "SPOTIFY_ARTIST_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

SPOTIFY_ALBUM_IMG_URL = getenv(

    "SPOTIFY_ALBUM_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

SPOTIFY_PLAYLIST_IMG_URL = getenv(

    "SPOTIFY_PLAYLIST_IMG_URL",

    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOVLFVl0gIGQWKZ1Z7B4Vqw_Z9-05Xr3aHIw&usqp=CAU",

)

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
