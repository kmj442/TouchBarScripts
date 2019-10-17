# plex server restart

import os
import sys
import time
import datetime

FIFTEEN = 900
HALF_HOUR = 1800
HOUR = 3600

def main():
	# initial check
	running = check_plex()
	while not running:
		start_plex()
		time.sleep(60)
		print("Plex Started: {0}".format(datetime.datetime.now()))
	while True:
		try:
			wait_check()
			running = check_plex()
			if not running:
				print("Plex found not running: {0}".format(datetime.datetime.now()))
				start_plex()
		except KeyboardInterrupt:
			print("Exiting Monitor - plex is no longer being monitored.")
			sys.exit(0)

def start_plex():
	""" starts plex service again after being found not running """
	print("Staring Plex: {0}".format(datetime.datetime.now()))
	os.popen("C:\\Program Files (x86)\\Plex\\Plex Media Server\\Plex Media Server.exe")

def wait_check():
	""" Depending on what time it is, it'll timeout between queries """
	current_hour = datetime.datetime.now().hour
	if current_hour < 16:
		print("Checking again in 30 minutes.")
		time.sleep(HALF_HOUR)
	elif current_hour >= 16:
		print("Checking again in 15 minutes.")
		time.sleep(FIFTEEN)

def check_plex():
	""" Just combines get_tasklist and plex_search to reduce code """
	tasklist = get_tasklist()
	return plex_search(tasklist)

def get_tasklist():
	""" Used to retrieve and parse tasklist to monitor """
	return os.popen("tasklist").read().split("\n")

def plex_search(tasklist):
	""" Used to search the tasklist for "Plex Media Server.exe" """
	running = False
	for row in tasklist:
		if "Plex Media Server.exe" in row:
			print("Plex is running: {0}".format(datetime.datetime.now()))
			running = True
			break
	return running


if __name__ == '__main__':
	main()