import RPi.GPIO as GPIO
import time

class ultra_sonic:
    def __init__(self, _trig, _echo, _vardist):
        self._trig = _trig
        self._echo = _echo
        self._vardist = _vardist

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._echo, GPIO.OUT)
        GPIO.setup(self._trig, GPIO.IN)

    def dispurce(self):
        GPIO.output()
        time.sleep(2)
        GPIO.output()
        time.sleep(0.00001)
        GPIO.output()
        while GPIO.input(self._echo) == 0:
            start = time.time()
        while GPIO.input(self._echo) == 1:
            stop  = time.time()

        duration = end - start
        distance = duration * 17150
        distance = round(distance, 3) # in CM

        return distance
