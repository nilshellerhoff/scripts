#! /usr/bin/env python3

#################################################################
# Stream Youtube to vlc
# 
# Author: Nils Hellerhoff <nils.hellerhoff@gmail.com>
# Date: 2020-12-04
# 
# This script uses youtube-dl to stream a Youtube-Video to vlc 
# It automatically picks 1080p60, this can be customized below
# Usage: stream.py <youtube-url>
# 
# Requirements:
# - youtube-dl (pip install youtube-dl)
################################################################

videoresolution = "1080p60"
videocodec = "avc1.64002a"

audiobitrate = 160
audiocodec = "opus"

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
video = [format["url"] for format in info["formats"] if format["format_note"] == videoresolution and format["vcodec"] == videocodec][0]
audio = [format["url"] for format in info["formats"] if format["acodec"] == audiocodec and format["abr"] == audiobitrate][0]

subprocess.Popen([
    vlcexec,
    video,
    "--input-slave={}".format(audio),
    "--no-video-title",
    "--meta-title={}: {}".format(uploader, title)],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)