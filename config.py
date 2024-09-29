# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25736332")

API_HASH = os.environ.get("API_HASH", "283b4470f2828857d413bad23d11b4d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7988311574:AAGC6lCEbwqCxI0al5sPU1s6a0LRcBWhKy4") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Sumitbots") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://sumitclass8007:tw&mK$Lir*BzP23@sumit.rtfzw.mongodb.net/?retryWrites=true&w=majority&appName=sumit")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6102080572').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
