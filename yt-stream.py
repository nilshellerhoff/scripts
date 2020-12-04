#! /usr/bin/env python3
# Stream to vlc
# 
# Date: 4.12.2020
# Author: Nils Hellerhoff
#
# This script uses youtube-dl to stream a Youtube-Video to vlc 
# It automatically picks 1080p60 h264 codec
# Usage: stream.py <youtube-url>

audioformat = "251"
videoformat = "299"

vlcexec = "vlc"

import subprocess
import sys
import json 
from youtube_dl import YoutubeDL

if len(sys.argv) != 2:
    print("Usage: stream.py <youtube-url>")
    sys.exit()
else:
    url = sys.argv[1]

ydl = YoutubeDL()
info = ydl.extract_info(url, download=False)

uploader = info["uploader"]
title = info["title"]
video = [format["url"] for format in info["formats"] if format["format_id"] == videoformat][0]
audio = [format["url"] for format in info["formats"] if format["format_id"] == audioformat][0]

subprocess.Popen([
    vlcexec,
    video,
    "--input-slave={}".format(audio),
    "--no-video-title",
    "--meta-title={}: {}".format(uploader, title)],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)