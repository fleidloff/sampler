#!/bin/sh
sudo mount -t vfat /dev/sda1 /mnt/usb
cp -r /mnt/usb/* ./sounds/