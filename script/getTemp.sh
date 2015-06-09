#!/bin/bash
cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
cpuTemp1=$(($cpuTemp0/1000))
cpuTemp2=$(($cpuTemp0/100))
cpuTempM=$(($cpuTemp2 % $cpuTemp1))
stamp=$(date)
unixEpoch=$(date +%s)


#echo CPU temp"="$cpuTemp1"."$cpuTempM"'C"

fmtTmp=$cpuTemp1"."$cpuTempM
output=$fmtTmp",C,"$stamp","$unixEpoch
echo $output
