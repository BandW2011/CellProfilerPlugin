#!/usr/bin/python
'''
import sys

def convertImageString( str ):
	sys.stdout.write( str )
	sys.stdout = "test"
	print "test2"
	return

for arg in sys.argv:
	print arg
'''
import sys

class BNWError( Exception ):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

# takes an image path and strips it 
def convert_image_string( image_path ):
	# to slice a string, use string[start:end]
	# to find last str in string, use string.rfind(str)
	# to find length of string, use len(string)
	t = image_path.rfind("/")
	if (t == -1):
		return image_path
	new_string = image_path[t:len (image_path)]
	if (new_string[len (new_string) - 1] == "/"):
		raise BNWError('BNWError: path is a directory')
		quit()
	if (new_string[0] == "/" and len (new_string) != 1):
		return new_string[1:len (new_string)]
	else:
		return new_string

# image--L0000--S00--U04--V00--J14--E01--O00--X00--Y00--T0000--Z00--C00.ome.tif
def get_tokens( image_name ):
	return image_name.split('--')

# u, v, j, x, y,
def clean_tokens( tokens ):
	cleaned_tokens = [None]

	for token in tokens:
		if (token[0] == 'U' or token[0] == 'V' or token[0] == 'J' or token[0] == 'X' or token[0] == 'Y'):
			if (token.find('.') != -1):
				token = token[0:token.find]
			if (cleaned_tokens[0] == None):
				cleaned_tokens[0] = token
			else: cleaned_tokens.append(token)

	return cleaned_tokens



# /gasd/aad/image--L0000--S00--U04--V00--J14--E01--O00--X00--Y00--T0000--Z00--C00.ome.tif

if (len (sys.argv) == 1):
	raise BNWError('BNWError: no arguments')
else:
	for num in range(1, len (sys.argv)):
		converted_string = convert_image_string(sys.argv[num])
		print clean_tokens(get_tokens(converted_string))
