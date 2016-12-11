#!/bin/sh
sudo mount -t vfat /dev/sda1 /mnt/usb

ls /mnt/usb/ | cat -n | head -n 1 | while read n f; do cp "/mnt/usb/$f" "./sounds/$1.wav"; done 

sudo chown -R pi:pi ./sounds