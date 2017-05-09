#!/usr/bin/env python

"""Quick & easy recipe for downloading a file or a sequence of files

USAGE: $/.pyloader.py [url] [start] [end] [path/to/downloaded/file]
"""

__author__ = "Aman <aman@amandavinci.me>"
__version__ = "Revision: 0.0.1"
__date__ = "Date: 09/05/2017"

import os
import sys		
import urllib.request, urllib.parse, urllib.error

def download(url, start, end, filepath):
	"""File Downloader

	Args:
		url: url to download from
		start: index to start download from
		end: index to stop download at
		filepath: name of the downloaded file

	Returns:
		True if succesful 
	"""
	for i in range(start, end+1):
		currFile = filepath.format(i)
		print("Downloading " + currFile + "...")
		urllib.request.urlretrieve(url.format(i), currFile)
		print("SUCCESS: Downloaded " + currFile + "\n")



if __name__ == '__main__':
	if len(sys.argv) == 5:
		try:
			print("Attempting to start download...\n")
			download(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
			print("Completed succesfully!")
		except IOError:
			print("ERROR: Download Failed...")
	else:
		print("USAGE: $/.pyloader.py [url] [start] [end] [path/to/downloaded/file]")