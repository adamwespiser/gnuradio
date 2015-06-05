#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: AM Receiver
# Author: OZ9AEC
# Description: Simple AM receiver prototype
# Generated: Wed Jun  3 18:13:07 2015
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

from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx

class am_rx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="AM Receiver")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.offset_fine = offset_fine = 0
        self.offset_coarse = offset_coarse = 0
        self.freq = freq = 7200000
        self.LO = LO = 0
        self.xlate_filter_taps = xlate_filter_taps = firdes.low_pass(1, samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.width = width = 10000
        self.trans = trans = 1500
        self.rx_freq = rx_freq = LO+freq+(offset_coarse+offset_fine)
        self.rf_gain = rf_gain = 20
        self.lo_freq = lo_freq = LO
        self.display_selector = display_selector = 0
        self.af_gain = af_gain = 1

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=50e3,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0_0.win)
        _width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._width_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	label="Filter",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._width_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	minimum=2000,
        	maximum=40000,
        	num_steps=760,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_width_sizer, 7, 0, 1, 1)
        _trans_sizer = wx.BoxSizer(wx.VERTICAL)
        self._trans_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_trans_sizer,
        	value=self.trans,
        	callback=self.set_trans,
        	label="Trans",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._trans_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_trans_sizer,
        	value=self.trans,
        	callback=self.set_trans,
        	minimum=500,
        	maximum=5000,
        	num_steps=900,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_trans_sizer, 8, 0, 1, 1)
        self._rx_freq_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	label="Receive",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._rx_freq_static_text, 5, 3, 1, 1)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(560e3, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label="RF",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=0,
        	maximum=50,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rf_gain_sizer, 7, 1, 1, 1)
        _offset_fine_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_fine_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_fine_sizer,
        	value=self.offset_fine,
        	callback=self.set_offset_fine,
        	label="Fine tune",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_fine_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_fine_sizer,
        	value=self.offset_fine,
        	callback=self.set_offset_fine,
        	minimum=-1000,
        	maximum=1000,
        	num_steps=400,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_offset_fine_sizer, 6, 0, 1, 2)
        _offset_coarse_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_coarse_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_coarse_sizer,
        	value=self.offset_coarse,
        	callback=self.set_offset_coarse,
        	label="Coarse tune",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_coarse_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_coarse_sizer,
        	value=self.offset_coarse,
        	callback=self.set_offset_coarse,
        	minimum=-120000,
        	maximum=120000,
        	num_steps=960,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_offset_coarse_sizer, 6, 2, 1, 2)
        self._lo_freq_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.lo_freq,
        	callback=self.set_lo_freq,
        	label="LO",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._lo_freq_static_text, 5, 2, 1, 1)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(2, (xlate_filter_taps), 100e3, samp_rate)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label="USRP",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._freq_text_box, 5, 1, 1, 1)
        self._display_selector_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.display_selector,
        	callback=self.set_display_selector,
        	label="Spectrum",
        	choices=[0, 1],
        	labels=['Baseband','USRP'],
        )
        self.GridAdd(self._display_selector_chooser, 5, 0, 1, 1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, 1e6, -5000, 5000, 700, firdes.WIN_HAMMING, 6.76))
        _af_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._af_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_af_gain_sizer,
        	value=self.af_gain,
        	callback=self.set_af_gain,
        	label="VOL",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._af_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_af_gain_sizer,
        	value=self.af_gain,
        	callback=self.set_af_gain,
        	minimum=0,
        	maximum=5,
        	num_steps=50,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_af_gain_sizer, 8, 1, 1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_xlate_filter_taps(firdes.low_pass(1, self.samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_offset_fine(self):
        return self.offset_fine

    def set_offset_fine(self, offset_fine):
        self.offset_fine = offset_fine
        self._offset_fine_slider.set_value(self.offset_fine)
        self._offset_fine_text_box.set_value(self.offset_fine)
        self.set_rx_freq(self.LO+self.freq+(self.offset_coarse+self.offset_fine))

    def get_offset_coarse(self):
        return self.offset_coarse

    def set_offset_coarse(self, offset_coarse):
        self.offset_coarse = offset_coarse
        self._offset_coarse_slider.set_value(self.offset_coarse)
        self._offset_coarse_text_box.set_value(self.offset_coarse)
        self.set_rx_freq(self.LO+self.freq+(self.offset_coarse+self.offset_fine))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_rx_freq(self.LO+self.freq+(self.offset_coarse+self.offset_fine))
        self._freq_text_box.set_value(self.freq)

    def get_LO(self):
        return self.LO

    def set_LO(self, LO):
        self.LO = LO
        self.set_lo_freq(self.LO)
        self.set_rx_freq(self.LO+self.freq+(self.offset_coarse+self.offset_fine))

    def get_xlate_filter_taps(self):
        return self.xlate_filter_taps

    def set_xlate_filter_taps(self, xlate_filter_taps):
        self.xlate_filter_taps = xlate_filter_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.xlate_filter_taps))

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self._width_slider.set_value(self.width)
        self._width_text_box.set_value(self.width)

    def get_trans(self):
        return self.trans

    def set_trans(self, trans):
        self.trans = trans
        self._trans_slider.set_value(self.trans)
        self._trans_text_box.set_value(self.trans)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self._rx_freq_static_text.set_value(self.rx_freq)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)

    def get_lo_freq(self):
        return self.lo_freq

    def set_lo_freq(self, lo_freq):
        self.lo_freq = lo_freq
        self._lo_freq_static_text.set_value(self.lo_freq)

    def get_display_selector(self):
        return self.display_selector

    def set_display_selector(self, display_selector):
        self.display_selector = display_selector
        self._display_selector_chooser.set_value(self.display_selector)

    def get_af_gain(self):
        return self.af_gain

    def set_af_gain(self, af_gain):
        self.af_gain = af_gain
        self._af_gain_slider.set_value(self.af_gain)
        self._af_gain_text_box.set_value(self.af_gain)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = am_rx()
    tb.Start(True)
    tb.Wait()
