#!/usr/bin/env python

"""
	b64chunk.py - Recreate files using base64 encoding
	author: 4lph4b

		usage: b64chunk.py [-h] [-t TARGET] [-s CHUNK_SIZE] [-d DESTINATION] FILE

		positional arguments:
		  FILE            Local file

		optional arguments:
		  -h, --help            show this help message and exit
		  -t TARGET, --target TARGET
		                        Target shell (bash, cmd, powershell - default: bash)
		  -s CHUNK_SIZE, --split CHUNK_SIZE
		                        Split by chunk size (default: 5k)
		  -d DESTINATION, --dest DESTINATION
		                        Destination file name (default: local filename)
"""

import argparse
import base64
import random
import string

# Function to convert 5k -> 5000
def convert_si_to_number(x):
    total_stars = 0
    if 'k' in x:
        if len(x) > 1:
            total_stars = float(x.replace('k', '')) * 1000 # convert k to a thousand
    elif 'M' in x:
        if len(x) > 1:
            total_stars = float(x.replace('M', '')) * 1000000 # convert M to a million
    elif 'B' in x:
        total_stars = float(x.replace('B', '')) * 1000000000 # convert B to a Billion
    else:
        total_stars = int(x) # Less than 1000
    return int(total_stars)

# Used in temp filename
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Command line arguments
parser = argparse.ArgumentParser(
	description='Recreate files using base64 encoding',
	epilog="""
Generates a series of shell commands to build a file using base64 encoding. 
Target shell can be bash, cmd.exe, or powershell (any version). 
Input file can be ascii or binary. 
Output from this script can be copy-and-pasted directly into a local or remote terminal session."""
	)
parser.add_argument('-t','--target', dest='target', default='b',
                    help='Target shell (bash, cmd, powershell - default: bash)')
parser.add_argument('-s','--split', dest='chunk_size', default='5k',
                    help='Split by chunk size (default: 5k)')
parser.add_argument('-d','--dest', dest='destination',
                    help='Destination file name (default: local filename)')
parser.add_argument(metavar='FILE', dest='file',
                    help='Local file')
args = parser.parse_args()

# Convert chunk_size
csize = convert_si_to_number(args.chunk_size)

# Destination filename
if not args.destination:
	destFilename = args.file
else:
	destFilename = args.destination

# Used for cmd & powershell
tmpVar = randomString()

# Open local file
f = open(args.file, "rb")


if args.target[0] == 'b':
	# BASH target shell
	# 	outputs directly to file

	# remove the desination file
	print("rm %s" % destFilename)

	while True:
		data = f.read(csize)
		if not data:
			break
		b64 = base64.b64encode(data)

		print('echo -n \'%s\' | base64 -d >> %s' % (b64, destFilename))


elif args.target[0] == 'c':
	# CMD target shell
	# 	uses a temporary file

	# remove the desination file
	print("del /Q %s" % destFilename)
	# remove tmp file if exists
	print('del /Q %s' % tmpVar)

	# read & b64 encode entire file
	b64 = base64.b64encode(f.read())

	# split b64 string into chunks
	for chunk in [b64[i:i+csize] for i in range(0, len(b64), csize)]:
		# echo without newline into tmp file
		print('echo|set /p="%s" >> %s' % (chunk, tmpVar))

	# b64 decode tmpfile into destination file
	print('certutil -decode %s %s' % (tmpVar, destFilename))

	# remove tmp file
	print('del /Q %s' % tmpVar)


elif args.target[0] == 'p':
	# POWERSHELL target shell
	# 	uses a temporary variable

	# remove the desination file
	print("del %s" % destFilename)
	# init temp variable
	print("$%s = @()" % tmpVar)

	while True:
		data = f.read(csize)
		if not data:
			break
		b64 = base64.b64encode(data)

		print('$%s += [System.Convert]::FromBase64String(\"%s\")' % (tmpVar, b64))

	# Sync .net pwd with powershell pwd
	print("[Environment]::CurrentDirectory = (Get-Location -PSProvider FileSystem).ProviderPath")

	# Write file
	print('[System.IO.File]::WriteAllBytes("%s", $%s)' % (destFilename, tmpVar))

	# Remove tmp variable
	print('Remove-Variable %s' % tmpVar)


else:
	print("Unknown target shell: %s" % args.target)
