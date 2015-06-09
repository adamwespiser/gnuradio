#!/bin/bash


while true; do


	#get temp information
	cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
	cpuTemp1=$(($cpuTemp0/1000))
	cpuTemp2=$(($cpuTemp0/100))
	cpuTempM=$(($cpuTemp2 % $cpuTemp1))
	fmtTmp=$cpuTemp1"."$cpuTempM

	# get time information
	stamp=$(date)
	unixEpoch=$(date +%s)

	# format and print the output
	output=$fmtTmp",C,"$stamp","$unixEpoch
	echo $output

	# sleep
	sleep 10
done
