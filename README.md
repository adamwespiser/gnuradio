# gnuradio
gnu radio files


# HOWTWO
### use rtl-sdr
1)build gnuradio (build_gnuradio script)
2) update udev rules
3) plug in DVB-T device, run 
4) remove unused driver w/ `sudo rmmod dvb_usb_rtl28xxu rtl2832`

### scan for frequencies:
#### rtl_power
```rtl_power -f 88M:108M:125k fm_stations.csv```    
```python heatmap.py fm_stations.csv fm_stations.png```
#### RTLSDR-Scanner
```/home/adam/bin/RTLSDR-Scanner/src/rtlsdr_scan.py```
```getSigStations.R```

### GNURadio Companion
```gnuradio-companion```
0) visual a frequency -> waterfall.grc
1) Narrowband(police) -> narrow2.grc
2) FM                 -> fm_examples_works.grc
3) Airband            -> airband_and_am.grc



### listen to fm
`rtl_fm -f 104.5M -s 192000 -r 48000 - | aplay -r 48k -f S16_LE -t raw -c 1`

