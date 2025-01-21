import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "16457832"))
API_HASH = getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")

BOT_TOKEN = getenv("BOT_TOKEN", "7962364610:AAH9aJa__qFLnEmJ0kb4n4eITlM-1LFbQmI")
OWNER_USERNAME = getenv("OWNER_USERNAME","solo_girl14")
BOT_USERNAME = getenv("BOT_USERNAME" , "MoonVibe143Bot")
BOT_NAME = getenv("BOT_NAME" , "MoonVibe")
ASSUSERNAME = getenv("ASSUSERNAME" , "Moonvibez143")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://architect04:architect04@cluster0.fylqb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", -1002066328009))
OWNER_ID = int(getenv("OWNER_ID", 6891833889))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/kingofizzy/bfn",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Beast-Fox-Network-01-19")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/beast_fox_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/avalum_nanum_143")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
STRING1 = getenv("STRING_SESSION", "BQD7IGgAxIwlqLfpBtbEw-b8r2dhKyxfCRMnH33A88Vm09kiCbuz2f4S6HZVNpRKfwM6BzCfxtI4rcKfoUVtII-NeQazDu9tUTHy5aI4e7kNt7KP6K8kcFPGijCO5STw43n8w_5WlFzlg35OuWb8r60zblfdDK7bJE5cCIn16YXoAdwTWwjojWnEz_yqVXC0xZaBeC-HpNA7u58h0SrWHhBiDumxvsl3Sw5t7NeCwEjjQnz2g_G25X-CcvOlwUpj2NEBZCTcqKlW3iRUgawvIaecddigR7qO4EU06D34hlFO1XVW_IQqoRa1sU9Dx28ZVjJMQeD2e0I0Bm8a7oEk8ymZDLsp6wAAAAHZxUp8AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://envs.sh/sE4.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://envs.sh/sE4.jpg")
PLAYLIST_IMG_URL = "https://envs.sh/sE4.jpg"
STATS_IMG_URL = "https://envs.sh/sE4.jpg"
TELEGRAM_AUDIO_URL = "hhttps://envs.sh/sE4.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/sE4.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
