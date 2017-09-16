# PyStreamableCom

Python RESTful API wrapper for Streamable.com that contains functionality for both experiences developers as well as novices. Compatible
with Python 3.0+ (not tested on any lower).

## Installation

This API is available via PyPi at https://pypi.python.org/pypi/PyStreamableCom.
So, it supports pip installation.


```
pip install pystreamablecom
```

## Implementation

The 'StreamableAPI' module contains a class called StreamableAPI, and making an instance of this class is as follows:

```
obj = StreamableAPI()
```

You can then call various functions depending on your objective. For instance, if you wanted to retrieve a video's information given it's
shortcode identifier, it can work as follows:

```
obj.retrieve_video('3x4mpl3')
```

The result will be a scrapable JSON format via a Python dictionary with various pieces of information, like the HTML code to embed the 
said video.
