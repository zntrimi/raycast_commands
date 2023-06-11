#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Gyazo URL Extractor
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 📁
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }

# Documentation:
# @raycast.description EXtract Direct File URL from Gyazo URL
# @raycast.author Zentaro 

import sys
import requests
import pyperclip
import webbrowser

# Dictionary of supported file extensions and their MIME types
EXTENSION_MIME_MAP = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg"
}

def validate_file_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            if content_type in EXTENSION_MIME_MAP.values():
                return True
    except requests.exceptions.RequestException:
        pass
    return False

def get_direct_download_url(url):
    # extract image id from url
    image_id = url.split('/')[-1]

    # construct direct download url
    direct_download_url = f"https://i.gyazo.com/{image_id}"

    # check if direct download url is valid
    for extension, mime_type in EXTENSION_MIME_MAP.items():
        full_url = direct_download_url + extension
        if validate_file_url(full_url):
            return full_url

    return None

original_url = str(sys.argv[1])

direct_download_url = get_direct_download_url(original_url)

#Copy to clipboard
if direct_download_url:
    pyperclip.copy(direct_download_url)
    print("File URL copied to clipboard.")
else:
    print("Invalid URL or unsupported file format.")

#Open in browser
webbrowser.open(direct_download_url)
