#!/bin/bash

killall -q antimicrox

if [ "$1" = "arrow" ]; then
    antimicrox  --tray --profile-controller 1 --profile ~/my-stuff/antimicrox/joystick-arrows.amgp
else
    antimicrox  --tray --profile-controller 1 --profile ~/my-stuff/antimicrox/joystick-mouse.amgp
fi