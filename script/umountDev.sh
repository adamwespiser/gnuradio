#!/bin/bash

export mapped="rpi-encrypted"
export mounted="/data"

cd $HOME

sudo umount $mounted
sudo cryptsetup luksClose $mapped

