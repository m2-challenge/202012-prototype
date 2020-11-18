import pigpio
import time


class Motor():
    def __init__(self, in1, in2):
        """Initialize Motor Class

        Args:
            in1 (int): GPIO pin (only 12, 13, 18, 19 pin can be used)
            in2 (int): GPIO pin (only 12, 13, 18, 19 pin can be used)
        """
        self.in1 = in1
        self.in2 = in2
        pi = pigpio.pi()
        pi.set_mode(self.in1, pigpio.OUTPUT)
        pi.set_mode(self.in2, pigpio.OUTPUT)

    def setSpeed(self, speed):
        """Set Motor Speed

        Args:
            speed (int): between -100 and 100
        """
        speed = speed * 10000 if(speed > 100) else 1000000
        speed = speed * 10000 if(speed < -100) else -1000000
        if(speed > 0):
            self.pi.hardware_PWM(self.in1, 500, speed)
            self.pi.hardware_PWM(self.in2, 500, 0)
        elif(speed < 0):
            self.pi.hardware_PWM(self.in1, 500, 0)
            self.pi.hardware_PWM(self.in2, 500, -speed)
        else:
            self.pi.hardware_PWM(self.in1, 500, 0)
            self.pi.hardware_PWM(self.in2, 500, 0)

    def stop(self):
        """Set Motor Speed 0 (Stop)
        """
        self.pi.hardware_PWM(self.in1, 500, 0)
        self.pi.hardware_PWM(self.in2, 500, 0)

    def __del__(self):
        self.stop()


if __name__ == "__main__":
    print("Motor Test")
    motor = Motor(12, 13)

    motor.setSpeed(50)
    time.sleep(1)

    motor.setSpeed(100)
    time.sleep(3)

    motor.setSpeed(-70)
    time.sleep(2)

    motor.setSpeed(0)
    time.sleep(1)

    motor.stop()
    print("Done")
