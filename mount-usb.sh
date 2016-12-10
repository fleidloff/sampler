#!/bin/sh
sudo mount -t vfat /dev/sda1 /mnt/usb
rm -r ./sounds/*
cp -r /mnt/usb/* ./sounds/
sudo chown -R pi:pi ./sounds