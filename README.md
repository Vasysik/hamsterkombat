# Hamster Kombat Auto Farming Bot 
This is a bot that can help you to run hamsterkombat telegram bot which has quite complete features with auto upgrade (3 methods), auto complete combo, auto complete daily cipher, auto complete Mini Game & auto complete tasks.

# Config
  ```bash
{
    "min_tap": 1038,
    "max_tap": 1800,
    "DelayPerAccount": 5,
    "tapDelay": true,
    "ClaimKeysDelay": true,
    "delayUpgrade": false,
    "max_price": 5000000,
    "loop": 3800,
    "use_current": true,
    "use_influx": true,
    "influxdb_config_path": "influxdb_config.json",
    "influxdb_org": "",
    "influxdb_bucket": ""
}
  ```

# Hamster Config
  ```bash
{
    "Auto_Buy_Upgrade": "ON",
    "Auto_Complete_Combo": "ON",
    "Auto_Complete_Cipher": "ON",
    "Auto_Complete_Mini_Game": "ON",
    "Auto_Complete_Tasks": "ON"
}
  ```

# Influx Config
  ```bash
{
    "influxdb_url": "",
    "influxdb_token": ""
}
  ```

## Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Vasysik/hamsterkombat.git
    ```
2. Go to the project directory:
    ```bash
    cd hamsterkombat
    ```
3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
before starting the bot you must have your own initdata / queryid telegram! why query id? with query_id it is definitely more profitable because you don't have to bother changing your init data every time.

1. Use PC/Laptop or Use USB Debugging Phone
2. open the `hamster kombat bot`
3. Inspect Element `(F12)` on the keyboard
4. at the top of the choose "`Application`" 
5. then select "`Session Storage`" 
6. Select the links "`Hamster Kombat`" and "`tgWebAppData`"
7. Take the value part of "`tgWebAppData`"
8. take the part that looks like this: 

```txt 
query_id=xxxxxxxxx-Rxxxxuj&user=%7B%22id%22%3A1323733375%2C%22first_name%22%3A%22xxxx%22%2C%22last_name%22%3A%22%E7%9A%BF%20xxxxxx%22%2C%22username%22%3A%22xxxxx%22%2C%22language_code%22%3A%22id%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=xxxxx&hash=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
9. add it to `tokens.txt` file or create it if you dont have one


You can add more and run the accounts in turn by entering a query id in new line like this:
```txt
query_id=xxxxxxxxx-Rxxxxuj&user=%7B%22id%22%3A1323733375%2C%22first_name%22%3A%22xxxx%22%2C%22last_name%22%3A%22%E7%9A%BF%20xxxxxx%22%2C%22username%22%3A%22xxxxx%22%2C%22language_code%22%3A%22id%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=xxxxx&hash=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
query_id=xxxxxxxxx-Rxxxxuj&user=%7B%22id%22%3A1323733375%2C%22first_name%22%3A%22xxxx%22%2C%22last_name%22%3A%22%E7%9A%BF%20xxxxxx%22%2C%22username%22%3A%22xxxxx%22%2C%22language_code%22%3A%22id%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=xxxxx&hash=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
## RUN THE BOT
after that run the kombat hamster bot by writing the command

# Console

```bash
python main.py
```

# Docker

Build:
```bash
docker build -t my-hamster-app .
```

Start:
```bash
docker run -it -d --name hamster-container my-hamster-app
```


