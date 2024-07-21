from datetime import datetime
import time
import requests

key = "SANGEAN6666!"
url = "http://workout.dev.ddev.site/api/"   # Trailing slash is required to send POST data
sec = 10
id = "P"

def log(msg):
    print("{:%B %d, %Y %I:%M:%S %p}".format(datetime.now()) + "-" + id + " :: " + msg)

while True:
    data = {
        "key": key,
        "datetime": str(datetime.now()),
        "method": "Picture.ping",
    }
    headers={"Content-Type": "application/json"}

    try:
        log("Sending ping...")
        log(url)
        response = requests.post(url, data, headers)
    except Exception as ex:
        log("Error sending ping...")
        log(ex.message)
        log("Exiting program.")
        exit()

    try:
        log("Reading response...")
        log(str(response.json()))
    except requests.JSONDecodeError:
        log("Error decoding response...")
        log(response.text)
        log("Exiting.")
        exit()

    log("Waiting " + str(sec) + " seconds...")
    time.sleep(sec)

log("End.")