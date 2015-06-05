#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Airband
# Author: Adam Wespisers
# Description: Simple airband scanner
# Generated: Thu Jun  4 16:39:00 2015
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx

class airband(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Airband")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 500e-3
        self.samp_rate = samp_rate = 2.4e6
        self.offset_freq = offset_freq = 119e6
        self.freq_corr = freq_corr = 65
        self.freq = freq = 591.28e6
        self.base_freq = base_freq = 560e6

        ##################################################
        # Blocks
        ##################################################
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label="Volume",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_volume_sizer)
        self._offset_freq_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.offset_freq,
        	callback=self.set_offset_freq,
        	label="Frequency select",
        	choices=[119e6,120.5e6,123.85e6,126.55e6,128.65e6,132.225e6,560e6],
        	labels=["bradley 119M","worc tow 120.5M", "worc ground 123.85M","worc atais126.55M","worc clrnc 128.65M","logan twr 132.225M","560AM"],
        	style=wx.RA_VERTICAL,
        )
        self.Add(self._offset_freq_chooser)
        _freq_corr_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_corr_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_corr_sizer,
        	value=self.freq_corr,
        	callback=self.set_freq_corr,
        	label="Freq correction (ppm)",
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._freq_corr_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_corr_sizer,
        	value=self.freq_corr,
        	callback=self.set_freq_corr,
        	minimum=-127,
        	maximum=127,
        	num_steps=254,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_freq_corr_sizer)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(offset_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(freq_corr, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(49.6, 0)
        self.rtlsdr_source_0.set_if_gain(1, 0)
        self.rtlsdr_source_0.set_bb_gain(1, 0)
        self.rtlsdr_source_0.set_antenna("RX", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=48,
                decimation=48,
                taps=None,
                fractional_bw=None,
        )
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(50, (firdes.low_pass_2(1,samp_rate,25e3,10e3,40)), 0, samp_rate)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label="freq",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=500e6,
        	maximum=1200e6,
        	num_steps=700,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.audio_sink_0 = audio.sink(48000, "pulse", True)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=48e3,
        	audio_decim=1,
        	audio_pass=5000,
        	audio_stop=5500,
        )
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-5, 1, 0)
        self.analog_agc2_xx_0.set_max_gain(5)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_am_demod_cf_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_am_demod_cf_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    


    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass_2(1,self.samp_rate,25e3,10e3,40)))
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_offset_freq(self):
        return self.offset_freq

    def set_offset_freq(self, offset_freq):
        self.offset_freq = offset_freq
        self._offset_freq_chooser.set_value(self.offset_freq)
        self.rtlsdr_source_0.set_center_freq(self.offset_freq, 0)

    def get_freq_corr(self):
        return self.freq_corr

    def set_freq_corr(self, freq_corr):
        self.freq_corr = freq_corr
        self._freq_corr_slider.set_value(self.freq_corr)
        self._freq_corr_text_box.set_value(self.freq_corr)
        self.rtlsdr_source_0.set_freq_corr(self.freq_corr, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = airband()
    tb.Start(True)
    tb.Wait()
