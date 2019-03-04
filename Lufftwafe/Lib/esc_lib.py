#!/usr/bin/python
import time
import os

os.system("sudo pigpiod")
time.sleep(2)

import pigpio

_min  = 700
_max  = 2000
_null = 0

class drone_esc:

        def __init__(self, _pin1, _pin2, _pin3, _pin4):

		self._pin1 = _pin1
		self._pin2 = _pin2
		self._pin3 = _pin3
		self._pin4 = _pin4

		self.pi = pigpio.pi()
		self.pi.set_servo_pulsewidth(_pin1, _null)
		self.pi.set_servo_pulsewidth(_pin2, _null)
		self.pi.set_servo_pulsewidth(_pin3, _null)
		self.pi.set_servo_pulsewidth(_pin4, _null)

	def calibrate(self):

		self.pi.set_servo_pulsewidth(self._pin1, _null)
		self.pi.set_servo_pulsewidth(self._pin2, _null)
		self.pi.set_servo_pulsewidth(self._pin3, _null)
		self.pi.set_servo_pulsewidth(self._pin4, _null)
		print "Disconect the power source"
		inp = raw_input()
		if inp == '':

			self.pi.set_servo_pulsewidth(self._pin1, _max)
			self.pi.set_servo_pulsewidth(self._pin2, _max)
			self.pi.set_servo_pulsewidth(self._pin3, _max)
			self.pi.set_servo_pulsewidth(self._pin4, _max)
			print "Connect the power source"
			inp = raw_input()
			if inp == '':
				print "Beggining Final step..."
				self.pi.set_servo_pulsewidth(self._pin1, _min)
				self.pi.set_servo_pulsewidth(self._pin2, _min)
				self.pi.set_servo_pulsewidth(self._pin3, _min)
				self.pi.set_servo_pulsewidth(self._pin4, _min)
				time.sleep(12)

				self.pi.set_servo_pulsewidth(self._pin1, _null)
				self.pi.set_servo_pulsewidth(self._pin2, _null)
				self.pi.set_servo_pulsewidth(self._pin3, _null)
				self.pi.set_servo_pulsewidth(self._pin4, _null)
				time.sleep(2)

				self.pi.set_servo_pulsewidth(self._pin1, _min)
				self.pi.set_servo_pulsewidth(self._pin2, _min)
				self.pi.set_servo_pulsewidth(self._pin3, _min)
				self.pi.set_servo_pulsewidth(self._pin4, _min)
				time.sleep(1)

	def arm(self):
		print "Connect Power source"
		inp = raw_input()
		if inp == '':
				self.pi.set_servo_pulsewidth(self._pin1, _null)
				self.pi.set_servo_pulsewidth(self._pin2, _null)
				self.pi.set_servo_pulsewidth(self._pin3, _null)
				self.pi.set_servo_pulsewidth(self._pin4, _null)
				time.sleep(1)

				self.pi.set_servo_pulsewidth(self._pin1, _max)
				self.pi.set_servo_pulsewidth(self._pin2, _max)
				self.pi.set_servo_pulsewidth(self._pin3, _max)
				self.pi.set_servo_pulsewidth(self._pin4, _max)
				time.sleep(1)

				self.pi.set_servo_pulsewidth(self._pin1, _min)
				self.pi.set_servo_pulsewidth(self._pin2, _min)
				self.pi.set_servo_pulsewidth(self._pin3, _min)
				self.pi.set_servo_pulsewidth(self._pin4, _min)
				time.sleep(1)

	def control_r1(self, _thr):
		self.pi.set_servo_pulsewidth(self._pin1, _thr)

	def control_r2(self, _thr):
		self.pi.set_servo_pulsewidth(self._pin2, _thr)

	def control_l1(self, _thr):
		self.pi.set_servo_pulsewidth(self._pin3, _thr)

	def control_l2(self, _thr):
		self.pi.set_servo_pulsewidth(self._pin4, _thr)

        def stop(self):
                self.pi.set_servo_pulsewidth(self._pin1, _null)
                self.pi.set_servo_pulsewidth(self._pin2, _null)
                self.pi.set_servo_pulsewidth(self._pin3, _null)
                self.pi.set_servo_pulsewidth(self._pin4, _null)
                self.pi.stop()


class esc:

	def __init__(self, _pin):
		self._pin = _pin

		self.pi = pigpio.pi()
		self.pi.set_servo_pulsewidth(_pin, _null)

	def calibrate(self):
		self.pi.set_servo_pulsewidth(self._pin, _null)
		print "Disconect Power source: "
		inp = raw_input()
		if inp == '':
			pi.set_servo_pulsewidth(self._pin, _max)
			print "Conect Power Source: "
			inp = raw_input()
			if inp == '':
				self.pi.set_servo_pulsewidth(self._pin, _min)
				time.sleep(12)
				self.pi.set_servo_pulsewdith(self._pin, _null)
				time.sleep(2)
				self.pi.set_servo_pulsewidth(self._pin, _min)
				time.sleep(1)
				print "Done..."
				time.sleep(2)


	def arm(self):
		print "Connect Power Source: "
		inp = raw_input()
		if inp == '':
			self.pi.set_servo_pulsewidth(self._pin, _null)
			time.sleep(1)
			self.pi.set_servo_pulsewidth(self._pin, _max)
			time.sleep(1)
			self.pi.set_servo_pulsewidth(self._pin, _min)
			time.sleep(1)
			print "Done..."

	def control(self, speed):
		self.pi.set_servo_pulsewidth(self._pin, speed)

	def stop(self):
		self.pi.set_servo_pulsewidth(self._pin, _null)
		self.pi.stop()

