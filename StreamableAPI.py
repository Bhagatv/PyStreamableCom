'''
StreamableAPI.py
~~~~~~~~~~~~~~~~~~
Python API to allow easier use with the Streamable API.

Author: Veeral Bhagat



Implementation
~~~~~~~~~~~~~~~~~

>>> obj = StreamableAPI()
>>> obj.upload_video(...)
{'status' : 1, 'shortcode' :'fake_shortcode'}


'''






import requests



UPLOAD_URL = 'https://api.streamable.com/upload'
IMPORT_URL = 'https://api.streamable.com/import'
RETRIEVE_URL = 'https://api.streamable.com/videos/'
EMBED_URL = 'https://api.streamable.com/oembed.json'
ROOT = 'https://streamable.com'


class StreamableAPI:
    def __init__(self):
        pass
    
    def upload_video(self, file_path: 'Full path to video', auth: ('username','password'),title=None,getURL = False):
        '''Allows you to upload a video on your local drive to streamable.com on your account. Returns JSON string
           that has the unique shortcode identifier of the video and the status code. If getURL is True, then the function
           will return the URL to the video, and not the extra data.'''
        
        infile = open(file_path,'rb')
        if title != None:
            data = {'title': title}
        
        response = requests.post(UPLOAD_URL,infile, data = title, auth = auth)

        if getURL:
            return self.retrieve_video(response.json()['shortcode'])['url']
        return response.json()

    def import_video(self, url: 'URL to video', auth: ('username','password'),title=None):
        '''Allows user to upload a video from another website on Streamable directly. Returns JSON string that has
           that has the unique shortcode identifier of the video and the status code.'''
        
        data = {'url':url}
        
        if title != None:
            data['title'] = title
        
        response = requests.get(IMPORT_URL, data = data, auth = auth)

        return response.json()

    def retrieve_video(self, shortcode: str, getURL = False):
        '''Allows user to make a request to get the information of an uploaded video in a JSON string. If getURL is True, then the function
           will return the URL to the video, and not the extra data.'''

        response = requests.get(RETRIEVE_URL+shortcode)

        if getURL:
            return response.json()['url']

        return response.json()

    def embed_video(self, url: 'URL to video', maxwidth=None, maxheight=None):
        '''Allows user to get information to embed a Streamable.com video, including specific HTML code. Optional arguments
           include maxwidth and maxheight of the embeded clip.'''
    
        data = {'url':url}

        if maxwidth != None:
            data['maxwidth'] = maxwidth
        if maxheight != None:
            data['maxheight'] = maxheight

        response = requests.get(EMBED_URL,data=data)

        return response.json()

    
                    
    
