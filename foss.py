import servo
import machine
import urequests
import time

class fossflag:
	def __init__(self):
		print('Fossflag init')
		self.servoFlag = servo.Servo(machine.Pin(15))
		self.previousTweets = {}

	def flagRaise(self):
		print('Flag raise')
		self.servoFlag.write_angle((90+45))

	def flagLower(self):
		print('Flag lower')
		self.servoFlag.write_angle((90-45))

	def pull(self):
		r = urequests.get('http://tim.gremalm.se/twitter.php')
		responseText = r.text
		r.close()

		responseText = responseText.rstrip()
		print('Response %s' % responseText)
		rLines = responseText.split('\n')
		foundnewTweet = False
		for line in rLines:
			words = line.split('\t')
			ttime = words[0]
			md5 = words[1]

			if not md5 in self.previousTweets:
				self.previousTweets[md5] = ttime
				foundnewTweet = True

		if foundnewTweet:
			print('New tweet detected')
			self.flagRaise()
			time.sleep(2)
			self.flagLower()
			time.sleep(1)
			self.servoFlag.pwm.deinit()

