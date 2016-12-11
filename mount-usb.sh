#!/bin/sh
sudo mount -t vfat /dev/sda1 /mnt/usb
rm -r ./sounds/*

ls /mnt/usb/ | cat -n | head -n 8 |  while read n f; do cp "/mnt/usb/$f" "./sounds/$n.wav"; done 

sudo chown -R pi:pi ./sounds