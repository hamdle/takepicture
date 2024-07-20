import pygame.camera
from datetime import datetime
import requests
import cv2
import base64

version = 2
path = "/home/eric/Pictures/TakePicture/"
key = "SANGEAN6666!"
url = "http://workout.dev.ddev.site/api"
id = "B"

def filename():
	return "TakePicture v" + str(version) + " - {:%B %d, %Y %I:%M:%S %p}".format(datetime.now()) + "-" + id + ".jpg"

def log(msg):
    print("{:%B %d, %Y %I:%M:%S %p}".format(datetime.now()) + "-" + id + " :: " + msg)

log("Initializing cameras...")
pygame.camera.init()
cameras = pygame.camera.list_cameras()

if cameras:
    log("Loading camera...")
    camera = pygame.camera.Camera(cameras[0], (1920, 1080))
    if camera is None:
        log("Failed to load camera...")
        log("Exiting program.")
        exit()
    log(cameras[0])
else:
    log("No cameras found...")
    log("Exiting program.")
    exit()

name_img = filename()
path_img = path + name_img

try:
    log("Starting camera...")
    camera.start()
except Exception as ex:
    log("Error starting camera...")
    log(ex.message)
    log("Exiting program.")
    exit()

log("Taking picture...")

image = camera.get_image()
log("Saving picture...")
pygame.image.save(image, path_img)
camera.stop()
log(path_img)

img = cv2.imread(path_img)
b64_img = base64.b64encode(cv2.imencode('.jpg', img)[1])    # .decode()

data = {
    "key": key,
    "name": name_img,
    "image": b64_img,
    "method": "Picture.takepicture",
}
headers={"Content-Type": "application/json"}

try:
    log("Sending picture...")
    log(url)
    response = requests.post(url, data, headers)
except Exception as ex:
    log("Error sending picture...")
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

log("End.")