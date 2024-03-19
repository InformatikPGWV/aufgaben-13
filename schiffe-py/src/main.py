from rich import print


import openmeteo_requests
import requests_cache
from retry_requests import retry
import os

import pyfiglet


def main():
    runtime_data = {"active_player": None, "board": None}

    # Show Main Menu
    main_menu(runtime_data)

    # Check if game is running, if so, join, else go to the main menu

    # print("[red]Rot :)[/red] [green] Green UwU [/green] [bold purple]Justus be like[/]")
    print(
        "chippi chippi chappa chappa dubi dubi daba daba magico mi dubi dubi boom boom boom"
    )

    current_weather = get_weather_data(52.52, 13.41)

    # Daten für el Spielbretto:
    # X X X X
    # | | | L P1 Ship Placed
    # | | L__ P2 Ship Placed
    # | L____ P1 discovered P2's ship
    # L______ P2 discovered P1's ship

    example = {
        "roomcode": "1234",
        "finished": False,
        "next_player": 2,
        "rows": 8,
        "cols": 8,
    }

    print(current_weather["temperature"])

    rows = example["rows"]
    cols = example["cols"]
    Player1_feld(rows, cols)


def enable_bdsm_mode(bool):
    pass


def create_board(rows, cols):
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append([False, False, False, False])
            # erster Wert für plaziertes Schiff (spieler1)
            # zweiter Wert für plaziertes Schiff (spieler2)
            # dritter Wert P1 discovered P2's ship
            # vierter Wert P2 discovered P1's ship
            # �����������������������
        board.append(row)
    return board


def Player1_feld(rows, cols):
    Player_board_1 = []
    for i in range(rows):
        boerdchen = []
        for j in range(cols):
            if board[i][1] == True and board[i][4] == True:
                boerdchen.append("T") #T = Treffer
          
            if board[i][1] == True:
                boerdchen.append("X")
            else:
                boerdchen.append("O")
        Player_board_1.append(boerdchen)
    return Player_board_1
  

def Player2_feld(rows, cols):
    Player_board_2 = []
    for i in range(rows):
        boerdchen = []
        for j in range(cols):
            if board[i][2] == True and board[i][3] == True:
                boerdchen.append("T")
          
            if board[i][2] == True:
                boerdchen.append("X")
            else:
                boerdchen.append("O")

        Player_board_2.append(boerdchen)
    return Player_board_2


def main_menu(runtime_data):
    print(50 * "=")


def room_code_menu():  # make sure user has good experience
    pass


def show_credits():
    pass


def end_game():
    pass


def print_board(current_player):
    pass


def schiffchenplatzieren():
    pass


def print_ascii(text):
    print(str(pyfiglet.figlet_format(str(text), font="banner3")))


# Screen stuff


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# ======== Weather


def get_weather_data(latitude, longitude):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession(".cache", expire_after=60)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "is_day",
            "precipitation",
            "rain",
            "wind_speed_10m",
            "wind_direction_10m",
        ],
        "wind_speed_unit": "ms",
        "timeformat": "unixtime",
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    # print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    # print(f"Elevation {response.Elevation()} m asl")
    # print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    # print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Current values. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_relative_humidity_2m = current.Variables(1).Value()
    current_is_day = current.Variables(2).Value()
    current_precipitation = current.Variables(3).Value()
    current_rain = current.Variables(4).Value()
    current_wind_speed_10m = current.Variables(5).Value()
    current_wind_direction_10m = current.Variables(6).Value()

    weather_data = {
        "time": current.Time(),
        "temperature": current_temperature_2m,
        "relative_humidity": current_relative_humidity_2m,
        "is_day": current_is_day,
        "precipitation": current_precipitation,
        "rain": current_rain,
        "wind_speed": current_wind_speed_10m,
        "wind_direction": current_wind_direction_10m,
    }

    return weather_data


# ===== CHAT STUFF
class Chat:
    def __init__(self, url, room, author):
        self.url = url
        self.room = room
        self.author = author


class Message:
    def __init__(self, id, author, content):
        self.id = id
        self.author = author
        self.content = content


def send_message(chat, message):
    body = {
        "action": "add",
        "user": chat.author,
        "chat": chat.room,
        "message": message,
    }
    requests.post(chat.url, json=body)


def get_messages(chat, date):
    body = {
        "action": "get",
        "chat": chat.room,
        "date": date,
    }
    response = requests.post(chat.url, json=body)

    messages = []

    if response.status_code != 200:
        return messages

    for message in response.json():
        id = message["id"]
        author = message["user"]
        content = message["message"]

        message = Message(id=id, author=author, content=content)
        messages.append(message)

    return messages


def get_messages_from_last(chat, seconds):
    now = int(time.time())
    date = now - seconds
    return get_messages(chat, date)


if __name__ == "__main__":
    main()
