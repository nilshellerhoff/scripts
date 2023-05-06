# Scripts
Collection of various scripts, mainly linux

## newtab-terminal (Linux)
My workflow using terminals is to open one terminal window but with multiple tabs. These scripts enable this functionality in common linux terminal emulators

## yt-stream<span>.py
Play a Youtube-stream in vlc from commandline. Uses only 1080p60 h264 at the moment. This script is useful if you cant use hardware acceleration in the browser, but vlc works with it. On my pc CPU usage dropped from ~100% to 20-30%

Requirements:
- Python 3
- youtube-dl (`pip install youtube-dl`)

Usage:
`python yt-stream.py <youtube-url>`