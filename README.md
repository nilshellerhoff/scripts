# Scripts
Collection of various scripts, mainly linux

## newtab-&lt;terminal-app&gt; (Linux)
My workflow using terminals is to open one terminal window but with multiple tabs. These scripts enable this functionality in common linux terminal emulators

#### gnome-terminal
Gnome-Terminal does not have a new-tab option. Therefore this script will check whether gnome-terminal is running, focus the window and then execute Ctrl+Shift+t in the window, which will open a new tab

Requires `wmctrl` and `xdotool`.

#### konsole
Konsole has a `new-tab` option, which doesn't bring the window in focus though.

Requires `xdotool`.

#### xfce4-terminal
The XFCE Terminal does have an option `--tab` to open a new tab, but when no terminal is open, this causes a window with two tabs to be opened (see https://gitlab.xfce.org/apps/xfce4-terminal/-/issues/13)

## yt-stream<span>.py
Play a Youtube-stream in vlc from commandline. Uses only 1080p60 h264 at the moment. This script is useful if you cant use hardware acceleration in the browser, but vlc works with it. On my pc CPU usage dropped from ~100% to 20-30%

Requirements:
- Python 3
- youtube-dl (`pip install youtube-dl`)

Usage:
`python yt-stream.py <youtube-url>`