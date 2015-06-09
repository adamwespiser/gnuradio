#!/bin/bash

export mapped="rpi-encrypted"
export mounted="/data"

sudo umount $mounted
sudo cryptsetup luksClose $mapped

