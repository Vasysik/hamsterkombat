# This file can be empty, it just indicates that this directory should be treated as a package
import os
import json
import locale
import time
from datetime import datetime
from colorama import *

mrh = Fore.LIGHTRED_EX
pth = Fore.LIGHTWHITE_EX
hju = Fore.LIGHTGREEN_EX
kng = Fore.LIGHTYELLOW_EX
bru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
htm = Fore.LIGHTBLACK_EX

last_log_message = None
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def _banner():
    banner = r"""
 ██╗████████╗███████╗     ██╗ █████╗ ██╗    ██╗
 ██║╚══██╔══╝██╔════╝     ██║██╔══██╗██║    ██║
 ██║   ██║   ███████╗     ██║███████║██║ █╗ ██║
 ██║   ██║   ╚════██║██   ██║██╔══██║██║███╗██║
 ██║   ██║   ███████║╚█████╔╝██║  ██║╚███╔███╔╝
 ╚═╝   ╚═╝   ╚══════╝ ╚════╝ ╚═╝  ╚═╝ ╚══╝╚══╝  """ 
    print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
    print(hju + f" Hamster Kombat Auto Bot")
    print(mrh + f" NOT FOR SALE = Free to use")
    print(mrh + f" before start please '{hju}git pull{mrh}' to update bot")

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_config():
    config_path = os.path.join(os.path.dirname(__file__), '../config.json')
    with open(config_path, 'r') as file:
        try:
            config_content = file.read()
            return json.loads(config_content)
        except json.JSONDecodeError as e:
            return {}
        
def read_status():
    with open('status.json', 'r') as f:
        return json.load(f)

def update_status(status=read_status()['status'], end_string=read_status()['endString']):
    with open('status.json', 'w') as f:
        json.dump({"status": status, "endString": end_string}, f)

def log(message):
    global last_log_message
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if message != last_log_message:
        update_status(end_string=message)
        print(f"{htm}[{current_time}] {message}")
        last_log_message = message

def log_line():
    print(pth + "~" * 60)

def countdown_timer(seconds, looper = False):
    while seconds:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        h = str(h).zfill(2)
        m = str(m).zfill(2)
        s = str(s).zfill(2)
        if looper: update_status(status="waiting", end_string=f"please wait until {h}:{m}:{s} ")
        print(f"{pth}please wait until {h}:{m}:{s} ", flush=True, end="\r")
        seconds -= 1
        time.sleep(1)
    if looper: update_status(status="waiting", end_string=f"please wait until {h}:{m}:{s} ")
    print(f"{pth}please wait until {h}:{m}:{s} ", flush=True, end="\r")

def _number(number):
    return locale.format_string("%d", number, grouping=True)