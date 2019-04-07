import time
import foss

print('Sleep before fossflag init')
time.sleep(10)

flag = foss.fossflag()

def mainloop():
	print('Mainloop')
	while True:
		try:
			print('Poll loop')
			flag.pull()
			time.sleep(30)

		except:
			print('Loop Exception')
			pass
mainloop()

