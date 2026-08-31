import os
from dotenv import  load_dotenv
from pathlib import Path

load_dotenv()


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# APPLICATION
# ============================================================

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
APP_LOGO = os.getenv("APP_LOGO")

WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"


# ============================================================
# DATABASE
# ============================================================

DB_HOST = os.getenv("AKIPOS_DB_HOST", "localhost")
DB_PORT = int(os.getenv("AKIPOS_DB_PORT", "3306"))
DB_NAME = os.getenv("AKIPOS_DB_NAME", "akipos")
DB_USER = os.getenv("AKIPOS_DB_USER", "root")
DB_PASSWORD = os.getenv("AKIPOS_DB_PASSWORD", "")


DATABASE_CONFIG = {
    "host": DB_HOST,
    "port": DB_PORT,
    "database": DB_NAME,
    "user": DB_USER,
    "password": DB_PASSWORD,
}


# ============================================================
# API
# ============================================================

API_HOST = os.getenv("AKIPOS_API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("AKIPOS_API_PORT", "8000"))

API_BASE_URL = f"http://{API_HOST}:{API_PORT}"


# ============================================================
# AI CLOUD
# ============================================================

AI_ENABLED = False

AI_API_KEY = os.getenv("AKIPOS_AI_API_KEY", "")

AI_API_URL = os.getenv(
    "AKIPOS_AI_API_URL",
    ""
)


# ============================================================
# POS
# ============================================================

PAYMENT_METHODS = (
    "CASH",
    "TRANSFER",
    "QRIS",
)


# ============================================================
# INVENTORY
# ============================================================

INVENTORY_METHOD = "FIFO"


# ============================================================
# APPLICATION SETTINGS
# ============================================================

DEFAULT_PAGE_SIZE = 20

CURRENCY = "IDR"

DECIMAL_PLACES = 0