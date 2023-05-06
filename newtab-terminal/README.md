#### gnome-terminal
Gnome-Terminal does not have a new-tab option. Therefore this script will check whether gnome-terminal is running, focus the window and then execute Ctrl+Shift+t in the window, which will open a new tab

Requires `wmctrl` and `xdotool`.

#### konsole
Konsole has a `new-tab` option, which doesn't bring the window in focus though. Also in newer versions of Konsole, the option "Run all Konsole windows in a single process" under Settings -> Configure Konsole must be enabled for this to work.

Requires `wmctrl`.

#### xfce4-terminal
The XFCE Terminal does have an option `--tab` to open a new tab, but when no terminal is open, this causes a window with two tabs to be opened (see https://gitlab.xfce.org/apps/xfce4-terminal/-/issues/13)
