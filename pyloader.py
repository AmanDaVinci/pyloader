#!/usr/bin/env python

__author__ = "Aman <aman@amandavinci.me"
__version__ = "$Revision: 0.0.1 $"
__date__ = "$Date: 09/05/2017 $"

"""
Recipe for downloading a sequence of files over http

Usage: /.pyloader.py [url] [start] [end] [filepath] 
"""
import os
import sys		
import urllib.request, urllib.parse, urllib.error

def download(url, start, end, filepath):
	'''
	File Downloader

	Args
		url
		start
		end
		filepath

	Returns
		True if succesfull 
	'''
	for i in range(start, end+1):
		print("Downloading file#{}...".format(i))
		urllib.request.urlretrieve(url.format(i), filepath.format(i))


if __name__ == '__main__':
	if len(sys.argv) == 5:
		try:
			download(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
		except IOError:
			print("ERROR: Download Failed...")
	else:
		print("Usage: /.pyloader.py [url] [start] [end] [filepath]")