import requests
import logging
import datetime
import time
import send_sms


def check_server_ok(server_url):
    while(True):
        response = requests.get(server_url)
        responce_code = str(response.status_code)
        current_datetime = datetime.datetime.now()
        logging.basicConfig(filename='check_server_log.txt', level=logging.INFO)
        logging.info(f'{current_datetime} {server_url} status: {responce_code}')
        if responce_code != '200':
            send_sms.send_panic_msg()
            break
        time.sleep(3)


if __name__ == "__main__":
    check_server_ok('https://python101.online')
