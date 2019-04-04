import cv2
import sys
import os
import time
from dronekit_api import Utils
import json
# conn_string = '/dev/ttyUSB0'
conn_string = 'tcp:127.0.0.1:5770'
vehicle = Utils(conn_string)

camera_port = 0
count = 0

camera = cv2.VideoCapture(camera_port)
IMAGE_DIR_NAME = sys.argv[1]
IMAGE_DIR_PATH = os.path.join(os.getcwd(),IMAGE_DIR_NAME)
IMAGE_FULL_PATH = os.path.join(IMAGE_DIR_PATH,IMAGE_DIR_NAME)
FORMAT = '.jpg'

if not os.path.isdir(IMAGE_DIR_PATH):
    os.makedirs(IMAGE_DIR_PATH)
# Captures a single image from the camera and returns it in PIL format
def get_image():
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im

# A feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide.
def save_image(image,name):
    print("Taking image...")
    print(os.path.join(IMAGE_DIR_PATH,str(name))+FORMAT)
    cv2.imwrite(os.path.join(IMAGE_DIR_PATH,str(name))+FORMAT, image)

with open('./gps_log.txt', 'w') as outfile:
    time.sleep(10)
    while True:
        # _ = get_image()
        camera_capture = get_image()
        tm = time.time()
        # cv2.imshow('frame',camera_capture)
        c = cv2.waitKey(1)
        save_image(camera_capture, tm)
        state = {}
        state = vehicle.get_state()
        state['timestamp'] = tm
        outfile.write(json.dumps(state)+'\n')
        # time.sleep(1)