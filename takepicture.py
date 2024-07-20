import pygame
import pygame.camera
from datetime import datetime
import time
import requests
import cv2
import base64

version = 2
take_in_sec = 60 * 3
path = "/home/eric/Pictures/TakePicture/"
key = "SANGEAN6666!"
url = "https://workout.dev/api/takepicture"

def filename():
	return path+"TakePicture v"+str(version)+" - {:%B %d, %Y %I:%M:%S %p-B}".format(datetime.now())+".jpg"

print("Booting camera...")
pygame.camera.init()
cameras = pygame.camera.list_cameras()
print(cameras)
print(cameras[1])

print("Directory: " + path)
print("Interation (sec): " + str(take_in_sec))
print("Creating camera...")
if cameras:
	camera = pygame.camera.Camera(cameras[0], (1920, 1080))
else:
	print("No cameras found.")
	exit()

print("Taking pictures...")


path_img = filename()
name_img = "TakePicture v"+str(version)+" - {:%B %d, %Y %I:%M:%S %p-B}".format(datetime.now())+".jpg"
print(name_img)

if cameras:
    camera.start()
    image = camera.get_image()
    pygame.image.save(image, path_img)
    camera.stop()

    img = cv2.imread(path_img)
    #string_img = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
    string_img = base64.b64encode(cv2.imencode('.jpg', img)[1])
    print("Sending " + "https://workout.dev/api/takepicture" + "..")
    data = {
        "key": key,
        "name": name_img,
        "image": string_img
    }
    headers={"Content-Type": "application/json"}
    response = requests.post("https://workout.dev/api/takepicture",
        data,
        headers,
    )
    print(response.json())
