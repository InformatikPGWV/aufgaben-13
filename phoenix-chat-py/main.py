import requests

# from datetime import datetime
import time
from rich import print
import os

"""
            Good Code
░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░
░░████████████░░░█████████████████░░░░░░
"""


class Chat:
    def __init__(self, url, room, author):
        self.url = url
        self.room = room
        self.author = author

    def set_room(self, room):
        self.room = room

    def set_name(self, name):
        self.name = name


class Message:
    def __init__(self, id, author, content):
        self.id = id
        self.author = author
        self.content = content


def main():
    chat = initialize()

    while True:
        clear_screen()
        messages = get_messages_from_last(chat, 60 * 60)

        for message in messages:
            pretty_print(chat, message)

        user_send_massage(chat)


def send_message(chat, message):
    body = {
        "action": "add",
        "user": chat.author,
        "chat": chat.room,
        "message": message,
    }
    requests.post(chat.url, json=body)


def user_send_massage(chat):
    nachricht = input(
        "┎┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┒\n Wie soll deine Nachricht lauten?: \n┖┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┚\n"
    )
    if nachricht.upper() == "!CHANGEROOM":
        chat.room = int(input("In welchem Raum möchtest du chatten?: "))
    elif nachricht.upper() == "!CHANGENAME":
        chat.author = input("Mit welchem Namen möchtest du chatten?: ")
    elif nachricht.strip() == "":
        pass
    else:
        send_message(chat, nachricht)


def get_messages(chat, date):
    body = {
        "action": "get",
        "chat": chat.room,
        "date": date,
    }
    response = requests.post(chat.url, json=body)
    messages = []

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


def initialize():
    username = input("Wie heisst du?: ")
    room = int(input("In welchem Raum möchtest du chatten?: "))
    url = "http://chat.phoenixgymnasium.de"

    return Chat(url=url, room=room, author=username)


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pretty_print(chat, message):
    name = ""
    if message.author == chat.author:
        name = "DU"
    else:
        name = message.author

    print(f"{name} --> {message.content}")


if __name__ == "__main__":
    main()

"""
░░░░░░░░░░░░░░░░░░░░░▄▀░░▌
░░░░░░░░░░░░░░░░░░░▄▀▐░░░▌
░░░░░░░░░░░░░░░░▄▀▀▒▐▒░░░▌
░░░░░▄▀▀▄░░░▄▄▀▀▒▒▒▒▌▒▒░░▌
░░░░▐▒░░░▀▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░░░▌▒░░░░▒▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▐▒░░░░░▒▒▒▒▒▒▒▒▒▌▒▐▒▒▒▒▒▀▄
░░░░▌▀▄░░▒▒▒▒▒▒▒▒▐▒▒▒▌▒▌▒▄▄▒▒▐
░░░▌▌▒▒▀▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒█▄█▌▒▒▌
░▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▄▀█▌▒▒▒▒▒▀▀▒▒▐░░░▄
▀▒▒▒▒▌▒▒▒▒▒▒▒▄▒▐███▌▄▒▒▒▒▒▒▒▄▀▀▀▀
▒▒▒▒▒▐▒▒▒▒▒▄▀▒▒▒▀▀▀▒▒▒▒▄█▀░░▒▌▀▀▄▄
▒▒▒▒▒▒█▒▄▄▀▒▒▒▒▒▒▒▒▒▒▒░░▐▒▀▄▀▄░░░░▀
▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▄▒▒▒▒▄▀▒▒▒▌░░▀▄
▒▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▒▀▀▀▀▒▒▒▄▀
"""
