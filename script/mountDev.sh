#!/bin/bash

#export dev=$(blkid| grep 80d38717-1cf2-4c0d-aa17-5b12478319e1| cut -f 1 -d ':')
export dev="/dev/disk/by-uuid/a632064c-c4ed-4302-b542-0389a1ba5c54"
export mapped="rpi-encrypted"
export mounted="/data"

sudo cryptsetup luksOpen $dev $mapped

if [ ! -e $mounted ];then
		sudo mkdir $mounted
fi

sudo mount /dev/mapper/$mapped $mounted




