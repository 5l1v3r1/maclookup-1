#!/usr/bin/python3

import requests
import sys

def checkarg():
	if len(sys.argv) < 2:
		print('The argument must be a mac address write in any form:\n00-11-22-33-44-55\n00:11:22:33:44:55\n00.11.22.33.44.55\n001122334455\n0011.2233.4455\n\n\
	Ex. maclookup.py FC:FB:FB:01:FA:21 or maclookup.py FCFBFB01FA21\n')
		sys.exit()
	elif sys.argv[1] == 'help':
		print('The argument must be a mac address write in any form:\n00-11-22-33-44-55\n00:11:22:33:44:55\n00.11.22.33.44.55\n001122334455\n0011.2233.4455\n\n\
	Ex. maclookup.py FC:FB:FB:01:FA:21 or maclookup.py FCFBFB01FA21\n')
		sys.exit()

def maclookup():
	checkarg()
	#PARAMS = "FC:FB:FB:01:FA:21"
	URL = "https://api.macvendors.com/"
	r = requests.get(url = URL + sys.argv[1])
	data = r.text
	print(data)


if __name__ == '__main__':
    maclookup()