import os
import re

def update_file(path, replacements):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update root index.html
update_file('index.html', [
    ('pages/android-games.html', 'android/'),
    ('pages/itch-games.html', 'itch/'),
    ('pages/privacy-policy.html', 'privacy/'),
    ('letterlogic/index.html', 'games/letterlogic/'),
    ('letterlogic/android', 'games/letterlogic/android')
])

# Update android, itch, privacy
for f in ['android/index.html', 'itch/index.html', 'privacy/index.html']:
    update_file(f, [
        ('android-games.html', '../android/'),
        ('itch-games.html', '../itch/'),
        ('privacy-policy.html', '../privacy/'),
        ('../letterlogic/index.html', '../games/letterlogic/'),
        ('../letterlogic/android', '../games/letterlogic/android')
    ])

# Update games/letterlogic/index.html
update_file('games/letterlogic/index.html', [
    ('../assets/', '../../assets/'),
    ('../index.html', '../../index.html'),
    ('/letterlogic/android', '/games/letterlogic/android')
])

print("Updated internal links!")
