import cv2
import numpy as np
from djitellopy import tello
import KeyPressModule as kp
import time

kp.init()
me = tello.Tello()
me.connect()
me.streamon()
frame_read = me.get_frame_read()
print(me.get_battery())

global img




def route1():
    if kp.getKey("o"):
        me.takeoff()
        time.sleep(0.5)
        me.send_rc_control(0, 0, 25, 0)
        time.sleep(3)
        me.send_rc_control(0, 50, 0, 0)
        time.sleep(3)
        me.send_rc_control(0, 0, 0, 50)
        time.sleep(3)
        me.send_rc_control(0, 10, 0, 0)
        time.sleep(3)

        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', frame_read.frame)
        time.sleep(1)


        me.send_rc_control(0, -10, 0, 0)
        time.sleep(3)
        me.send_rc_control(0, 0, 0, -50)
        time.sleep(3)
        me.send_rc_control(0, -50, 0, 0)
        time.sleep(3)
        me.send_rc_control(0, 0, -25, 0)
        time.sleep(3)

        me.land()

    elif kp.getKey("p"):
        me.takeoff()
        time.sleep(0.5)
        me.send_rc_control(0, 0, 25, 0)
        time.sleep(3)
        me.send_rc_control(0, 0, 0, 50)
        time.sleep(3)
        me.send_rc_control(0, 30, 0, 0)
        time.sleep(3)
        me.send_rc_control(0, 0, 20, 0)
        time.sleep(3)

        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', frame_read.frame)
        time.sleep(2)

        me.send_rc_control(0, 0, -20, 0)
        time.sleep(3)
        me.send_rc_control(0, -30, 0, 0)
        time.sleep(3)
        me.send_rc_control(0, 0, 0, -50)
        time.sleep(3)
        me.send_rc_control(0, 0, -25, 0)
        time.sleep(3)

        me.land()




while True:
    vals = route1()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)


