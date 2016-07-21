#!/usr/bin/python

import sys

import cellprofiler.cpmodule as cpm
import cellprofiler.settings as cps
from cellprofiler.settings import YES, NO

'''
bnwerr = "BNWError: "

class BNWError( Exception ):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
'''

class YoDontUseThisModule(cpm.CPModule):
    variable_revision_number = 1
    module_name = 'yo_dont_use_this_module'
    category = 'Other'

    def create_settings(self):
        # All the omero images that are loaded are assumed to have
        # as many or more channels than the highest channel number
        # the user specifies.
        self.channels = []
        self.channel_count = cps.HiddenCount(self.channels, "Channel count")
        # Add the first channel
        self.add_channelfn(False)

        # Button for adding other channels
        self.add_channel = cps.DoSomething("", "Add another channel", self.add_channelfn)
    
    def settings(self):
        return 0

    def run(self, workspace):
        return 0

    def add_channelfn(self, can_remove_True):
        return 0;

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
		raise Exception
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
def get_token( cleaned_tokens, token ):
    if (token == 'J'):
        return cleaned_tokens[0]
    elif (token == 'U'):
        return cleaned_tokens[1]
    elif (token == 'V'):
        return cleaned_tokens[2]
    elif (token == 'X'):
        return cleaned_tokens[3]
    elif (token == 'Y'):
        return cleaned_tokens[4]
    else:
        raise Exception

def image_path_to_token( image_path, token ):
    tokens = clean_tokens(get_tokens(convert_image_string(image_path)))
    tokens.sort()
    return get_token(tokens, token)

'''
if (len (sys.argv) == 1):
	raise BNWError('BNWError: no arguments')
else:
    for num in range(1, len (sys.argv)):
        print image_path_to_tokens(sys.argv[num], 'X')
'''
