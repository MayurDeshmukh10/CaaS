# CaaS

Caas is a Python library which provides Compression as a Service. CaaS offers reasonable and high speed compression by taking advantage of the Serverless Technology. Caas mainly performs effective compression on Image, Audio and Video files and effective lossless compression/decompression on text files. CaaS library uses custom file compression algorithms which are deployed on Openwhisk Serverless Framework.

## Installation:

CaaS can be installed by running ` pip install CaaS `. It requires ` Python 3.6.0 and above ` to run. 

## Abstract Usage:

The detailed usage of each interface is given in the section Interfaces. Here is the abstract usage of the CaaS library.

` from CaaS import interface `
######
` response = interface("filename_of_file_to_be_compressed","filename_of_compressed_file","authorization_key") `

here,
` interface `: the interface for compressing image, video, audio and text files. It is discussed in detail for each type of file in Interfaces section.
######
` response `: stores HTTP status code returned for your request.  

## Interfaces:

### CaaS::image_compression
image_compression is the interface for Image Compression.
It uses Semantic Perceptual Image Compression algorithm to compress the image files.
Semantic Perceptual Image Compression algorithm is implemented and deployed on the Openwhisk Serverless Framework.
CaaS provides support for compression of JPEG and PNG image files.

#### Usage:
` from CaaS import image_compression `
######
` response = image_compression("image_file_to_be_compressed","filename_of_compressed_image_file","authorization_key")`


### CaaS::video_compression
video_compression is the interface for Video Compression.
It uses Semantic Perceptual Image Compression algorithm to compress the video files.
Semantic Perceptual Image Compression algorithm is implemented and deployed on the Openwhisk Serverless Framework.
CaaS provides support for compression of MP4 video files.

#### Usage:
` from CaaS import video_compression `
######
` response = video_compression("video_file_to_be_compressed","filename_of_compressed_video_file","authorization_key") `

### CaaS::audio_compression
audio_compression is the interface for Audio Compression.
It uses Principal Component Analysis algorithm to compress the audio files.
Principal Component Analysis algorithm is implemented and deployed on the Openwhisk Serverless Framework.
CaaS provides support for compression of WAV and MP3 audio files.

#### Usage:
` from CaaS import audio_compression `
######
` response = audio_compression("audio_file_to_be_compressed","filename_of_compressed_audio_file","authorization_key") `


### CaaS::text_compression
text_compression is the interface for Text Compression.
It uses Adaptive Huffman Compression algorithm to compress the text files.
Adaptive Huffman Compression algorithm is implemented and deployed on the Openwhisk Serverless Framework.
CaaS provides support for compression of TXT Files and Programming Files(e.g.: .cpp, .py, .java, .js, etc).

#### Usage:
` from CaaS import text_compression `
######
` response = text_compression("text_file_to_be_compressed","filename_of_compressed_text_file","authorization_key") `

### CaaS::text_decompression
text_decompression is the interface for Text Decompression.
It uses Adaptive Huffman Decompression algorithm to decompress the text files.
Adaptive Huffman Decompression algorithm is implemented and deployed on the Openwhisk Serverless Framework.
CaaS provides support for decompression of TXT Files and Programming Files(e.g.: .cpp, .py, .java, .js, etc).

##### NOTE: As the implemented Text Compression and Decompression is lossless, the input to the decompression interface must be the text file compressed with the text_compression interface.


#### Usage:
` from CaaS import text_decompression `
######
` response = text_decompression("text_file_to_be_decompressed","filename_of_decompressed_text_file","authorization_key") `


