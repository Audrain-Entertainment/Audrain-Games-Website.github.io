#!/usr/bin/env python3
"""
This script scrapes the Google Play Store to find the official, high-resolution 
app icon URLs for a given list of Android apps.

Usage: 
    python scrape_icons.py

It looks for the 'og:image' meta tag in the HTML of the Google Play Store page,
which typically points to the app's icon.
"""

import urllib.request
import re
import json

# Dictionary mapping local game names to their Google Play Package IDs
apps = {
    'HoldemSolitaire': 'com.AudrainEntertainment.HoldemSolitaire',
    'QuickHoldem': 'com.AudrainEntertainment.QuickHoldem',
    'FiveLetter': 'com.AudrainEntertainment.FiveLetter',
    'UltimateTicTacToe': 'com.AudrainEntertainment.UltimateTicTacToe',
    'BlackjackTrainer': 'com.AudrainEntertainment.BlackjackTrainer',
    'LetterLogic': 'games.audrain.letterlogic'
}

results = {}

for name, pkg in apps.items():
    url = f'https://play.google.com/store/apps/details?id={pkg}'
    # Use a standard user-agent so Google doesn't block the request
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Look for the Open Graph image tag
        match = re.search(r'property="og:image"\s+content="([^"]+)"', html)
        if match:
            results[name] = match.group(1)
        else:
            # Fallback to finding the first play-lh user content image
            match = re.search(r'https://play-lh\.googleusercontent\.com/[a-zA-Z0-9_-]+', html)
            if match:
                results[name] = match.group(0)
    except Exception as e:
        print(f"Error scraping {pkg}: {e}")

print("Scraping complete. Found URLs:")
print(json.dumps(results, indent=2))
