#!/bin/sh

#################################################################
# Add all subdirectories of a path to the path variable
# You can put this script into your .profile
#
# Author: Nils Hellerhoff <nils.hellerhoff@gmail.com>
# Date: 2023-05-06
#################################################################

scriptpath="$HOME/bin"

if [ -d "$scriptpath" ] ; then
    PATH=$(find "$scriptpath"/* -type d -not -path '*/.*'  -printf "%p:")$PATH
fi
