import requests

from config import (
    TEAMS_WEBHOOK_URL,
    OPEN_METEO_URL
)

def format_weather(weather):

    current = weather["current"]

    return {
        "temperature":
            current["temperature_2m"],

        "humidity":
            current["relative_humidity_2m"],

        "wind_speed":
            current["wind_speed_10m"],

        "time":
            current["time"]
    }


def build_teams_payload(weather):
    return {
        "type": "message",
        "attachments": [
            {
                "contentType":
                    "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema":
                        "http://adaptivecards.io/"
                        "schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.2",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text":
                                "Automated Teams Notification Service",
                            "weight": "Bolder",
                            "size": "Large"
                        },
                        {
                            "type": "FactSet",
                            "facts": [
                                {
                                    "title": "Temperatura",
                                    "value":
                                        f'{weather["temperature"]} °C'
                                },
                                {
                                    "title": "Umidade",
                                    "value":
                                        f'{weather["humidity"]}%'
                                },
                                {
                                    "title": "Velocidade do vento",
                                    "value":
                                        f'{weather["wind_speed"]} km/h'
                                },
                                {
                                    "title": "Horário da medição",
                                    "value": weather["time"]
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }


def main():

    weather = get_weather()

    formatted_weather = format_weather(
        weather
    )

    print(formatted_weather)

    payload = build_teams_payload(formatted_weather)

    response = requests.post(
        TEAMS_WEBHOOK_URL,
        json=payload
    )

    print(response.status_code)


def get_weather():

    response = requests.get(
        OPEN_METEO_URL
    )

    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    main()