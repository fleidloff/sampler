#!/bin/sh
sudo mount -t vfat /dev/sda1 /mnt/usb
rm -r ./sounds/*
#find /mnt/usb/ -maxdepth 1 -type f |head -1000|xargs cp -t ./sounds/

ls ./tsounds/ | cat -n | head -n 8 |  while read n f; do cp "./tsounds/$f" "./sounds/$n.wav"; done 

sudo chown -R pi:pi ./sounds