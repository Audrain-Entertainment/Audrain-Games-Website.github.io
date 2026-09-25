#!/usr/bin/env python3
"""
This script downloads specific app icons from Google Play URLs and saves them 
into the 'assets/images/' directory.

Usage: 
    python download_icons.py

It appends '=w256-h256-rw' to the base Google Play image URL to request a 
nicely sized 256x256 image instead of a massive original file.
"""

import urllib.request
import os

# Dictionary of target filename -> Base Google Play image URL
icons = {
  'icon-holdemsolitaire.png': 'https://play-lh.googleusercontent.com/ZafAOg-x5Bu_wtT-zHgGGob1rYcXbRMWV6GBpZD1nDcpaGmqms4fAM_9NwRfemgoXTWgEagkPl8tnwNNl5o6',
  'icon-quickholdem.png': 'https://play-lh.googleusercontent.com/PgZ9wTzFffb90MWzfqJwdc8ZK1-Mu2RzwdaKR5SBY6ZcbYXC-HDJYUKS_htABKXws3O2BUJ81h5pL2V3Gvj96A',
  'icon-fiveletter.png': 'https://play-lh.googleusercontent.com/t5fwP1R3FcaTVT_KtnlJqEbK5RUSTNFlx-pjY8FqYlnDB7J97xnuXgjzH2WeR0UZpt9lXWHes2p0YUeoapI1',
  'icon-ultimatetictactoe.png': 'https://play-lh.googleusercontent.com/fikbSXQPwLToBp6MtZS3dYOVJ2wSrc2tXIbFKcqyTiFH4cQp-vIpGgEVbAqgpcMhVyaV6dv1_7ZloQ0sjBO1',
  'icon-blackjacktrainer.png': 'https://play-lh.googleusercontent.com/p9a9L0VZPuodETn_aCDNmcEQo1wXlZncj9UCQ5t0ZB-3llfxpPQSnAyUJjQyMTC1Y5IIZ338dRpNwnTgp1w_Mg',
  'icon-letterlogic.png': 'https://play-lh.googleusercontent.com/myrio4LSQ-gJzD51w8eDOzNWsXz4IzdDqIav8yQaJvXmz38Jr5bDVa34tUHCm3Y2nkH8sWGDsqfWbWKQliRP_IY'
}

for filename, url in icons.items():
    # Save directly to the website's assets/images/ folder
    filepath = os.path.join('..', 'assets', 'images', filename)
    
    # Request a specific size (256x256)
    req = urllib.request.Request(url + '=w256-h256-rw', headers={'User-Agent': 'Mozilla/5.0'})
    try:
        data = urllib.request.urlopen(req).read()
        with open(filepath, 'wb') as f:
            f.write(data)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
