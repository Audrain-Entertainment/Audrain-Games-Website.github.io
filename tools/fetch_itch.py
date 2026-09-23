#!/usr/bin/env python3
"""
This script was used to scrape the Time Bomb page on itch.io to find its 
promotional image and download it into the 'assets/images/' directory.

Usage:
    python fetch_itch.py
"""

import urllib.request
import re
import os

url = 'https://draino7n7.itch.io/time-bomb'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # Itch.io stores the main promo image in the 'og:image' meta tag
    # Note: the content attribute comes before the property attribute on itch.io
    match = re.search(r'content="([^"]+)"\s+property="og:image"', html)
    if match:
        image_url = match.group(1)
        print(f"Found image: {image_url}")
        
        # Download the image
        img_req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        img_data = urllib.request.urlopen(img_req).read()
        
        filepath = os.path.join('..', 'assets', 'images', 'icon-timebomb.png')
        with open(filepath, 'wb') as f:
            f.write(img_data)
        print("Downloaded icon-timebomb.png")
    else:
        print("No og:image found on the itch.io page.")
except Exception as e:
    print(f"Error scraping itch.io: {e}")
