from dotenv import load_dotenv
import os

load_dotenv()

TEAMS_WEBHOOK_URL = os.getenv(
    "TEAMS_WEBHOOK_URL"
)

OPEN_METEO_URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=-8.05"
    "&longitude=-34.88"
    "&current=temperature_2m,"
    "relative_humidity_2m,"
    "wind_speed_10m"
)