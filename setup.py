from setuptools import setup
from os import path

setup(
  name = 'CaaS',         # How you named your package folder (MyLib)
  packages = ['CaaS'],   # Chose the same as "name"
  version = '1.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Python library for Compression as a Service. CaaS can compress images, audio, video, text files ', 
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  author = 'Mayur Deshmukh',                   # Type in your name
  author_email = 'mayur.s.deshmukh10@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/MayurDeshmukh10/CaaS',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/MayurDeshmukh10/CaaS/archive/V_7.tar.gz',    # I explain this later on
  keywords = ['compression', 'image compression', 'video compression', 'audio compression', 'text compression','Compression as a service'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
