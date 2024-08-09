import requests
from collections import defaultdict
from src.utils import get_headers
from src.__init__ import countdown_timer, log

def load_promo(filename='promo.txt'):
    with open(filename, 'r') as file:
        promo_codes = [line.strip() for line in file]
    promo_dict = defaultdict(list)
    for code in promo_codes:
        code_type = code.split('-')[0]
        promo_dict[code_type].append(code)
    return promo_dict

def save_promo(promo_dict, filename='promo.txt'):
    with open(filename, 'w') as file:
        for code_list in promo_dict.values():
            for code in code_list:
                file.write(code + '\n')

def redeem_promo(token):
    promo_dict = load_promo()
    
    if not promo_dict:
        log(f"No codes available in promo.txt.")
        return

    max_attempts = 4
    attempts_tracker = defaultdict(int)
    http_error_tracker = defaultdict(int)
    max_http_errors = 2

    while promo_dict:
        for code_type, codes in list(promo_dict.items()):
            if attempts_tracker[code_type] >= max_attempts:
                if codes:
                    log(f"4/4 {code_type} have been applied today.")
                continue

            promo_code = codes[0]
            url = 'https://api.hamsterkombatgame.io/clicker/apply-promo'
            headers = get_headers(token)
            payload = {"promoCode": promo_code}

            try:
                res = requests.post(url, headers=headers, json=payload)
                res.raise_for_status()

                if res.status_code == 200:
                    log(f"Applied Promo {promo_code}")
                    codes.pop(0)
                    save_promo(promo_dict)
                    countdown_timer(5)
                    attempts_tracker[code_type] += 1
                    http_error_tracker[code_type] = 0 
                else:
                    log(f"Failed to apply {promo_code}")
                    codes.pop(0) 
                    save_promo(promo_dict)

            except requests.exceptions.HTTPError as e:
                log(f"Error applying {promo_code}")
                http_error_tracker[code_type] += 1
                if http_error_tracker[code_type] >= max_http_errors:
                    log(f"{code_type} Assuming maximum redemption")
                    attempts_tracker[code_type] = max_attempts
            except Exception as err:
                log(f"Error: {err}. Promo code: {promo_code}")
                codes.pop(0)  
                save_promo(promo_dict)

        if all(attempts >= max_attempts or not codes for attempts, codes in zip(attempts_tracker.values(), promo_dict.values())):
            break

    if all(attempts >= max_attempts for attempts in attempts_tracker.values()):
        log("Max reached for all promo types.")