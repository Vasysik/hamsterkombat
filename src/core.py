import sys
import json
import time
import locale
import requests
from colorama import *
from src.__init__ import read_config, update_status
from src.utils import load_tokens
from src.auth import get_token, authenticate
from src.exceptions import upgrade_passive, claim_daily, execute, boost, clicker_config
from src.exceptions import _sync, exhausted, execute_combo, claim_cipher, claim_key
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

config = read_config()
influxdb_config = read_json(config['influxdb_config_path'])
client = InfluxDBClient(url=influxdb_config['influxdb_url'], token=influxdb_config['influxdb_token'])
write_api = client.write_api(write_options=SYNCHRONOUS)
bucket = config['influxdb_bucket']
org = config['influxdb_org']

from src.__init__ import (
    mrh, pth, hju, kng, htm, bru,  reset, 
    read_config, _number, countdown_timer, log, 
    log_line, _banner, _clear
    )

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
init(autoreset=True)
config = read_config()

def read_hamster_config():
    with open('hamster_config.json', 'r') as f:
        return json.load(f)

def main():
    auto_upgrade = False
    combo_upgrade = False
    daily_cipher_on = False
    claim_key_on = False
    tasks_on = False

    cek_task_dict = {}
    countPerAccount = config.get('DelayPerAccount', 3)
    loop = config.get('loop', 3600)

    update_status(status="starting")
    while True:
        try:
            hamster_config = read_hamster_config()
            if hamster_config["Auto Buy Upgrade"] == "ON":
                auto_upgrade = not auto_upgrade
            if hamster_config["Auto Complete Combo"] == "ON":
                combo_upgrade = not combo_upgrade
            if hamster_config["Auto Complete Cipher"] == "ON":
                daily_cipher_on = not daily_cipher_on
            if hamster_config["Auto Complete Mini Game"] == "ON":
                claim_key_on = not claim_key_on
            if hamster_config["Auto Complete Tasks"] == "ON":
                tasks_on = not tasks_on
            
            init_data_list = load_tokens('tokens.txt')
            user_info_dict = {}
            for init_data in init_data_list:
                token = get_token(init_data)
                if token:
                    try:
                        update_status(status="login")
                        res = authenticate(token)
                        if res.status_code == 200:
                            user_data = res.json()
                            username = user_data.get('telegramUser', {}).get('username', 'Please set username first')
                            log(kng + f"Login as {pth}{username}")    
                            clicker_config(token)
                            clicker_data = _sync(token)
                            if 'clickerUser' in clicker_data:
                                user_info = clicker_data['clickerUser']
                                balance_coins = user_info['balanceCoins']
                                earn_passive_per_hour = user_info['earnPassivePerHour']
                                exchange_name = user_info['exchangeId']
                                update_status(status="get-user-info")
                                log(hju + f"Balance: {pth}{_number(balance_coins)}")
                                log(hju + f"Income: {pth}{_number(earn_passive_per_hour)}/h")
                                log(hju + f"CEO of {pth}{exchange_name} {hju}exchange")
                            update_status(status="working")
                            claim_daily(token)
                            while True:
                                exhausted(token)
                                if not boost(token):
                                    break
                            if tasks_on:
                                execute(token, cek_task_dict)
                            if daily_cipher_on:
                                claim_cipher(token)
                            if claim_key_on:    
                                claim_key(token)
                            if combo_upgrade:
                                execute_combo(token)
                            if auto_upgrade:
                                upgrade_passive(token, 1)  
                        update_status(status="ending")
                        log_line()
                        clicker_data = _sync(token)
                        if 'clickerUser' in clicker_data:
                            user_info = clicker_data['clickerUser']
                            user_info_dict[username] = user_info
                            balance_coins = user_info['balanceCoins']
                            earn_passive_per_hour = user_info['earnPassivePerHour']
                            log(hju + f"Balance: {pth}{_number(balance_coins)}")
                            log(hju + f"Income: {pth}{_number(earn_passive_per_hour)}/h")
                            point = Point("measurement").tag("username", username).field("balanceCoins", balance_coins).field("earnPassivePerHour", earn_passive_per_hour)
                            write_api.write(bucket=bucket, org=org, record=point)
                        countdown_timer(countPerAccount)
                    except requests.RequestException as e:
                        update_status(status="error")
                        log(mrh + f"Request exception for token {pth}{token[:4]}****: {str(e)}")
                else:
                    update_status(status="error")
                    log(mrh + f"Failed to login token {pth}{token[:4]}*********\n", flush=True)
            with open('current.json', 'w') as f:
                json.dump(user_info_dict, f)
            countdown_timer(loop)
        except Exception as e:
            update_status(status="error")
            log(mrh + f"An error occurred in the main loop: {kng}{str(e)}")
            countdown_timer(10)

if __name__ == '__main__':
    main()