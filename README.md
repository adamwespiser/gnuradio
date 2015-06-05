# gnuradio
gnu radio files


# HOWTO: Radio
###use rtl-sdr
1) build gnuradio (build_gnuradio script)    
2) update udev rules    
3) plug in DVB-T device, run    
4) remove unused driver w/ `sudo rmmod dvb_usb_rtl28xxu rtl2832`

###scan for frequencies:
#### rtl_power
`rtl_power -f 88M:108M:125k fm_stations.csv`    
`python heatmap.py fm_stations.csv fm_stations.png`    

#### RTLSDR-Scanner
`/home/adam/bin/RTLSDR-Scanner/src/rtlsdr_scan.py`    
`getSigStations.R`    

###listen to fm
`rtl_fm -f 104.5M -s 192000 -r 48000 - | aplay -r 48k -f S16_LE -t raw -c 1`    

###GNURadio Companion
run `gnuradio-companion`, then open:    
0) visual a frequency -> waterfall.grc    
1) Narrowband(police) -> narrow2.grc     
2) FM                 -> fm_examples_works.grc    
3) Airband            -> airband_and_am.grc    

###Moniter airtraffic with ADSB:
0) download dump1090 from github
2) `dump1090 --net --enable-agc`

# HOWTO:GPS
### Enable gps
`sudo gpsctl -n /dev/ttyUSB0`    
`sudo stty -F /dev/ttyUSB0 ispeed 4800`    
`sudo gpsd -D 5 -N -n /dev/ttyUSB0 > /dev/null`

### print out coords
`sudo awk -F"," '/GGA/ {print $3,$5}' /dev/ttyUSB0`    
`sudo cat /dev/ttyUSB0  > ./data/gps.track.file`    

### View position on map in realtime
`foxtrotgps`
`gpsdrive`

### log and view gpx (saved coord info)
`gpxlogger -f ./data/test.gpx`    
`gpxviewer ./data/test.gpx`    

### Use radio monitering w/ gps:
`/home/adam/bin/RTLSDR-Scanner/src/rtlsdr_scan.py`    



