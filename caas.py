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
	
	url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/6680cf59d332053774ebff7968541738e498ef46b8d4df20fb25851b3dcca438/compression/image_compression_api"

	headers = {'auth-token': auth_token, 'Content-Type': "image/jpeg"}

	with open(file_to_compress,"rb") as f:
		temp = f.read()

	base64image = base64.b64encode(temp)

	response = requests.post(url, headers=headers, files={file_to_compress: base64image},verify=False)

	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content


	with open(compressed_file,"wb") as out:
		out.write(data)

	return response


def video_compression(file_to_compress,compressed_file,auth_token):
	
	url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/6680cf59d332053774ebff7968541738e498ef46b8d4df20fb25851b3dcca438/compression/video_compression_api"

	headers = {'auth-token': auth_token,'Content-Type': "video/mp4"}

	with open(file_to_compress,"rb") as f:
		temp = f.read()

	base64image = base64.b64encode(temp)


	response = requests.post(url, headers=headers, files={file_to_compress: base64image},verify=False)

	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content


	with open(compressed_file,"wb") as out:
		out.write(data)

	return response





def text_compression(file_to_compress,compressed_file,auth_token):
	url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/6680cf59d332053774ebff7968541738e498ef46b8d4df20fb25851b3dcca438/compression/text_compression_encoder_api"

	headers = {'auth-token': auth_token, 'Content-Type': 'text/plain'}

	with open(file_to_compress,'rb') as file:
		response = requests.post(url, headers=headers, files={file_to_compress: file},verify=False)

	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content

	

	with open(compressed_file,"wb") as out:
		out.write(data)

	return response


def text_decompression(file_to_compress,compressed_file, auth_token):
	
	url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/6680cf59d332053774ebff7968541738e498ef46b8d4df20fb25851b3dcca438/compression/text_compression_decoder_api"

	headers = {'auth-token': auth_token, 'Content-Type': "application/x-binary"}

	with open(file_to_compress,"rb") as f:
		temp = f.read()

	base64image = base64.b64encode(temp)


	response = requests.post(url, headers=headers, files={file_to_compress: base64image},verify=False)

	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content


	with open(compressed_file,"wb") as out:
		out.write(data)

	return response


def audio_compression(file_to_compress,compressed_file,auth_token):
	
	url = "https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/6680cf59d332053774ebff7968541738e498ef46b8d4df20fb25851b3dcca438/compression/audio_compression_api"

	headers = {'auth-token': auth_token,'Content-Type': "audio/mpeg"}

	with open(file_to_compress,"rb") as file:
		response = requests.post(url, headers=headers, files={file_to_compress: file},verify=False)

	if response.status_code == 401:
		raise InvalidAuthKeyError

	data = response.content


	with open(compressed_file,"wb") as out:
		out.write(data)

	return response



# For testing purpose

def test_call(auth_token):

	url = "https://fn.enlight.dev/api/v1/web/kkwbecom05/default/test_auth1/"
	#url = "https://fn.enlight.dev/api/v1/web/kkwbecom05/default/test_api/"
	headers = {'auth-token': auth_token}

	response = requests.post(url, headers=headers, verify=False)


	return response    
    





    

