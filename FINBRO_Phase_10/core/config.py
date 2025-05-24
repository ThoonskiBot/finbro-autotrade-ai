import os
from dotenv import load_dotenv
load_dotenv()

ALPACA_API_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("APCA_API_BASE_URL")

LOG_PATH = "logs"
PDF_OUTPUT_DIR = "logs"
