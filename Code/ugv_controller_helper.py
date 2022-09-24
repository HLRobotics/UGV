"""ugv_console_controller_helper"""
from ugv_controller_constants import *
import requests
import time


class UGVControllerHelper:
    """UGV Controller Helper"""

    def __init__(self):
        """initializing the repository"""
        self._ip_address = UGV_IP
        self.speed = UGV_DEFAULT_SPEED
        self.left_speed = UGV_LEFT_SPEED
        self.right_speed = UGV_RIGHT_SPEED

    def url_generator(self, control):
        try:
            generated_url = "http://" + self._ip_address + "/" + str(control)
            # requests.get(generated_url)
        except:
            pass

    def move_forward(self):
        """move forward"""
        control = FORWARD
        self.url_generator(control)

    def move_backward(self):
        """move backward"""
        control = BACKWARD
        self.url_generator(control)

    def move_left(self):
        """move left"""
        control = LEFT
        self.url_generator(control)

    def move_right(self):
        """move right"""
        control = RIGHT
        self.url_generator(control)

    def stop(self):
        """stop  moving"""
        control = STOP
        self.url_generator(control)

    def increase_speed(self):
        """increase speed"""
        self.speed = self.speed + 10
        print("velocity => ", self.speed)
        self.url_generator(self.speed)

    def decrease_speed(self):
        """decrease speed"""
        self.speed = self.speed - 10
        print("velocity => ", self.speed)
        self.url_generator(self.speed)

    def increase_left_motor_speed(self):
        """increase left motor speed"""
        self.left_speed = self.left_speed + 1
        self.right_speed = self.speed
        print("Left velocity => ", self.left_speed)
        print("Right velocity => ", self.right_speed)
        self.url_generator(str(self.left_speed) + "_" + str(self.right_speed))

    def decrease_left_motor_speed(self):
        """decrease left motor speed"""
        self.left_speed = self.left_speed - 1
        self.right_speed = self.speed
        print("Left velocity => ", self.left_speed)
        print("Right velocity => ", self.right_speed)
        self.url_generator(str(self.left_speed) + "_" + str(self.right_speed))

    def increase_right_motor_speed(self):
        """increase right motor speed"""
        self.right_speed = self.right_speed + 1
        self.left_speed = self.speed
        print("Left velocity => ", self.left_speed)
        print("Right velocity => ", self.right_speed)
        self.url_generator(str(self.left_speed) + "_" + str(self.right_speed))

    def decrease_right_motor_speed(self):
        """decrease right motor speed"""
        self.right_speed = self.right_speed - 1
        self.left_speed = self.speed
        print("Left velocity => ", self.left_speed)
        print("Right velocity => ", self.right_speed)
        self.url_generator(str(self.left_speed) + "_" + str(self.right_speed))
