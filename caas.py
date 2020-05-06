'''
Mayur Deshmukh

Compression as a Service
Compression Api Wrapper for python

To do
1. Add support for SSL certificate for secured connection
2. Handle more exception

'''

import requests 
import urllib3
from CaaS import errors
import base64


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

'''Usage

How to call

from caas import text_compression

response = text_compression(filename_to_compress,path_of_file,authorization_key)

Exception Handling

If auth key is invalid then InvalidAuthKeyError exception is raised

To handle 

try:
	response = text_compression(filename_to_compress,path_of_file,authorization_key)
except InvalidAuthKeyError:
	do something

'''	

 


def image_compression(file_to_compress,compressed_file,auth_token):

	filename = file_to_compress.rpartition('/')[-1]
	extension = filename.rpartition('.')[-1]
	if extension == 'jpg' or extension == 'jpeg':
		content_type = 'image/jpeg'
	elif extension == 'png':
		content_type = 'image/png'
	elif extension == 'tiff':
		content_type = 'image/tiff'
	else:
		content_type = 'image/webp'

	url = "https://data-compression-platform.eu-gb.cf.appdomain.cloud/api/v1/image_compression"

	headers = {'auth-token': auth_token, 'Content-Type': content_type}

	with open(file_to_compress,"rb") as f:
		temp = f.read()

	response = requests.post(url,data=temp, headers=headers)

	if response.status_code == 401:
		raise InvalidAuthKeyError

	if response.status_code == 406:
		raise ImageTooSmallError

	data = response.content

	with open(compressed_file,"wb") as out:
		out.write(data)

	return response

def audio_compression(file_to_compress,compressed_file,auth_token):

	filename = file_to_compress.rpartition('/')[-1]
	extension = filename.rpartition('.')[-1]
	if extension == 'mp3':
		content_type = 'audio/mpeg'
	else:
		content_type = 'audio/wav'

	url = "https://data-compression-platform.eu-gb.cf.appdomain.cloud/api/v1/audio_compression"

	headers = {'auth-token': auth_token, 'Content-Type': content_type}

	with open(file_to_compress,"rb") as f:
		temp = f.read()

	response = requests.post(url,data=temp, headers=headers)



	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content

	with open(compressed_file,"wb") as out:
		out.write(data)

	return response

def text_compression(file_to_compress,compressed_file,auth_token):

	filename = file_to_compress.rpartition('/')[-1]

	url = "https://data-compression-platform.eu-gb.cf.appdomain.cloud/api/v1/text_compression_encoder"	
	
	headers = {'auth-token': auth_token}

	with open(file_to_compress,"rb") as f:
		temp = f.read()

	response = requests.post(url,data=temp, headers=headers)


	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content

	with open(compressed_file+'.cmp',"wb") as out:
		out.write(data)

	return response

def text_decompression(file_to_compress,compressed_file,auth_token):

	filename = file_to_compress.rpartition('/')[-1]

	url = "https://data-compression-platform.eu-gb.cf.appdomain.cloud/api/v1/text_compression_decoder"	
	
	headers = {'auth-token': auth_token}

	with open(file_to_compress,"rb") as f:
		temp = f.read()

	response = requests.post(url,data=temp, headers=headers)


	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content

	with open(compressed_file,"wb") as out:
		out.write(data)

	return response

def video_compression(file_to_compress,compressed_file,auth_token):

	filename = file_to_compress.rpartition('/')[-1]

	url = "https://data-compression-platform.eu-gb.cf.appdomain.cloud/api/v1/video_compression"

	headers = {'auth-token': auth_token}

	with open(file_to_compress,"rb") as f:
		temp = f.read()

	response = requests.post(url,data=temp, headers=headers)

	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content

	with open(compressed_file,"wb") as out:
		out.write(data)

	return response



    





    

