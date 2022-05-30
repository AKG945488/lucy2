# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "6137333"  
    API_HASH = "3422e1d5035e9fe5f31ab7cedb511900"
    TOKEN = "5323702143:AAHM6HpscgDRXKWV9JtQhNmyKrbW-SEEb84"
    OWNER_ID = "1739887067"
    OWNER_USERNAME = "LUCY_MANAGEMENT_BOT"
    MONGO_DB_URI = "mongodb+srv://akganthesm123456:XTQ3Vbue579p9Ms@cluster0.1roc7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    SUPPORT_CHAT = "LUCY_BOTS"
    JOIN_LOGGER = "-1001556960219"
    EVENT_LOGS = "-1001643051258"

    # RECOMMENDED
    INFOPIC = "https://telegra.ph/file/736f13fd86d7bf6ebac95.jpg"   
    CF_API_KEY = ""
    LASTFM_API_KEY = ""
    BOT_USERNAME = "LUCY_MANAGEMENT_BOT"
    WALL_API = ""
    OPENWEATHERMAP_ID = ""
    TEMP_DOWNLOAD_DIRECTORY = ""
    REM_BG_API_KEY = ""
    TIME_API_KEY = ""
    CASH_API_KEY = ""
    REM_BG_API_KEY = ""
    SESSION_STRING = "1AZWarzgBu52gc8HNyz_ibvJUdwgKk-7CsP1tcmGaBl2hdIoMXD6AGGUNnq64W0fdVtVGz02Hb-GtJQQmWR_50c-SEFOc7YbR_zZWUKWnABmx04q2iJqkZE_Yy6Qzjkwgj28nK-zZzy19Z7uG4e-CVekIrBab6Aj0kQXnDsI43x3Z8Dp2ZuQ-XEzJNoAyFx0LGeRwtsoSBmNieiTa35e4kyVVhFJhf68RgQz_LD3O6IY3dlrYKnl5_7AlhiEHTNEMeLZtB7minHDPou4GzsQeiMj0oeQdUpX_9HK1w7v3TTgeU6-C_1kczgTWVL3lT2Tz11wQpiYw9XBgVDUWo8-gDvkDVEnjdsQ="
    ARQ_API_KEY = "UIUXOY-NTKWDC-QHFFMD-DHHKVV-ARQ"
    ARQ_API = "UIUXOY-NTKWDC-QHFFMD-DHHKVV-ARQ"
    ARQ_API_URL = "aww"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    BOT_ID = "5323702143"
    STRING_SESSION = "1AZWarzgBu52gc8HNyz_ibvJUdwgKk-7CsP1tcmGaBl2hdIoMXD6AGGUNnq64W0fdVtVGz02Hb-GtJQQmWR_50c-SEFOc7YbR_zZWUKWnABmx04q2iJqkZE_Yy6Qzjkwgj28nK-zZzy19Z7uG4e-CVekIrBab6Aj0kQXnDsI43x3Z8Dp2ZuQ-XEzJNoAyFx0LGeRwtsoSBmNieiTa35e4kyVVhFJhf68RgQz_LD3O6IY3dlrYKnl5_7AlhiEHTNEMeLZtB7minHDPou4GzsQeiMj0oeQdUpX_9HK1w7v3TTgeU6-C_1kczgTWVL3lT2Tz11wQpiYw9XBgVDUWo8-gDvkDVEnjdsQ="
    SQLALCHEMY_DATABASE_URI = "postgres://dlvsomei:0p0AcLQEWwWq89iMnPuR0lypr1AIF9UH@castor.db.elephantsql.com/dlvsomei"
    DATABASE_URL = "postgres://dlvsomei:0p0AcLQEWwWq89iMnPuR0lypr1AIF9UH@castor.db.elephantsql.com/dlvsomei"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "2qrr~TrRIdNnZHEPvdTFjO7pG8LjtH1_I~zLwCLjGakrWlzaAMQ4fO~K0s75E9sJ"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1669178360"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1669178360"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1669178360"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1669178360"
    WOLVES = "1669178360"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    ALLOW_CHATS = True
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
