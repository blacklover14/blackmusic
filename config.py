import os

API_ID = int(os.getenv("API_ID", "23506344"))
API_HASH = os.getenv("API_HASH", "f0d7f34991f0b3266fdc1d9fa4e4d9fd")
BOT_TOKEN = os.getenv("8621566489:AAEPxAeYkl8Dr-UTEnlqghImsM7_f_y7orc")
SESSION_STRING = os.getenv("ASSISTANT_SESSION") or os.getenv("BQFmragAJxbM9_apBXk8A8UNPcFVtaAJru8wl1y_Dar3YHbz1_NCvclPyYaVRrnWz5Cw3-wjuEgzvTsVTnhFTTMXV1qCnt2nFrqTvG-PVc6uxZyW41CA9XPFncOp3EArYx0H0aJpznCIirX-clzOqnIhJPQ43l0dmx4zPjaP81zxtO74jNNAefbnGaD3J6obAo63dWQjVr9THQslSsKwijyCyvNPFMeJimZaFAAnfCwt3KOQRSQG4F8ISg7_7Kknd0LTezcchpEoLgemWbUBjW7ySPYHEBvmsa-yp83iqS1ylrOBmppYz_01Z27CJ-KXB-3XT092bbxGkFZV-0h-8ZcHMQQ0GQAAAAIVSKrwAA")
MAIN_OWNER = int(os.getenv("OWNER_ID", "8286835275"))
DEPLOYED_OWNER_ID = int(os.getenv("OWNER_ID", "8286835275"))
SEARCH_API_URL = os.getenv("SEARCH_API_URL", "https://search-api.kustbotsweb.workers.dev")
DOWNLOAD_API_BASE = os.getenv("DOWNLOAD_API_BASE", "").rstrip("/")
COOKIES_FILE = os.getenv("COOKIES_FILE", "cookies.txt")
YOUTUBE_COOKIES = os.getenv("YOUTUBE_COOKIES", "")
RATE_LIMIT_COUNT = 4
RATE_LIMIT_WINDOW = 6
MAX_TITLE_LEN = 30
PORT = int(os.getenv("PORT", "8080"))
