#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: OSMOSDR NFM RX
# Description: https://apollo.open-resource.org/mission:log:2012:05:06:rtlsdr-osmosdr-gnuradio-fm-receiver
# Generated: Fri Jun  5 09:35:53 2015
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

class osmo_nfm_rx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="OSMOSDR NFM RX")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2400000
        self.rx_freq = rx_freq = 854.388e6
        self.rx_fine = rx_fine = 0
        self.rx_coarse = rx_coarse = 0
        self.xlate_filter_taps = xlate_filter_taps = firdes.low_pass(1, samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.width = width = 12500
        self.variable_chooser_1 = variable_chooser_1 = 1
        self.tv_freq = tv_freq = 500.25e6
        self.trans = trans = 25000
        self.squelch = squelch = -55
        self.sql_lev = sql_lev = -20
        self.rx_freq_val = rx_freq_val = rx_freq+(rx_coarse+rx_fine)
        self.freq = freq = 155e6
        self.dev = dev = 7500
        self.decimation = decimation = 50
        self.af_gain = af_gain = 1

        ##################################################
        # Blocks
        ##################################################
        _width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._width_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_width_sizer,
        	value=self.width,
        	callback=self.set_width,
        	label="LP Filter",
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
        self.GridAdd(_width_sizer, 2, 4, 1, 4)
        _trans_sizer = wx.BoxSizer(wx.VERTICAL)
        self._trans_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_trans_sizer,
        	value=self.trans,
        	callback=self.set_trans,
        	label="LP Trans",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._trans_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_trans_sizer,
        	value=self.trans,
        	callback=self.set_trans,
        	minimum=500,
        	maximum=50000,
        	num_steps=900,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_trans_sizer, 2, 8, 1, 4)
        _squelch_sizer = wx.BoxSizer(wx.VERTICAL)
        self._squelch_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_squelch_sizer,
        	value=self.squelch,
        	callback=self.set_squelch,
        	label="squelch level",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._squelch_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_squelch_sizer,
        	value=self.squelch,
        	callback=self.set_squelch,
        	minimum=-100,
        	maximum=0,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_squelch_sizer)
        _rx_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_freq_sizer,
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	label="RX Center ",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_freq_sizer,
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	minimum=840000000,
        	maximum=860000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rx_freq_sizer, 0, 0, 1, 16)
        _dev_sizer = wx.BoxSizer(wx.VERTICAL)
        self._dev_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_dev_sizer,
        	value=self.dev,
        	callback=self.set_dev,
        	label="NBFM deviation",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._dev_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_dev_sizer,
        	value=self.dev,
        	callback=self.set_dev,
        	minimum=4000,
        	maximum=16000,
        	num_steps=24,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_dev_sizer)
        self._variable_chooser_1_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.variable_chooser_1,
        	callback=self.set_variable_chooser_1,
        	label='variable_chooser_1',
        	choices=[1, 2, 3],
        	labels=[],
        )
        self.Add(self._variable_chooser_1_chooser)
        _sql_lev_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sql_lev_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sql_lev_sizer,
        	value=self.sql_lev,
        	callback=self.set_sql_lev,
        	label="SQL",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sql_lev_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sql_lev_sizer,
        	value=self.sql_lev,
        	callback=self.set_sql_lev,
        	minimum=-100,
        	maximum=100,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_sql_lev_sizer, 1, 12, 1, 4)
        self._rx_freq_val_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.rx_freq_val,
        	callback=self.set_rx_freq_val,
        	label="Receive",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._rx_freq_val_static_text, 0, 16, 1, 1)
        _rx_fine_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_fine_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_fine_sizer,
        	value=self.rx_fine,
        	callback=self.set_rx_fine,
        	label="RX Fine",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_fine_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_fine_sizer,
        	value=self.rx_fine,
        	callback=self.set_rx_fine,
        	minimum=0,
        	maximum=10000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rx_fine_sizer, 1, 4, 1, 4)
        _rx_coarse_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_coarse_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_coarse_sizer,
        	value=self.rx_coarse,
        	callback=self.set_rx_coarse,
        	label="RX Offset",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_coarse_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_coarse_sizer,
        	value=self.rx_coarse,
        	callback=self.set_rx_coarse,
        	minimum=0,
        	maximum=1e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rx_coarse_sizer, 1, 0, 1, 4)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(rx_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(decimation, firdes.low_pass(
        	1, samp_rate, width, trans, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(48000, "", True)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(squelch, 1)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=48000,
        	tau=50e-6,
        	max_dev=dev,
        )
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
        self.GridAdd(_af_gain_sizer, 2, 12, 1, 4)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_simple_squelch_cc_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_xlate_filter_taps(firdes.low_pass(1, self.samp_rate, 125000, 25000, firdes.WIN_HAMMING, 6.76))
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, self.trans, firdes.WIN_HAMMING, 6.76))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.set_rx_freq_val(self.rx_freq+(self.rx_coarse+self.rx_fine))
        self.rtlsdr_source_0.set_center_freq(self.rx_freq, 0)
        self._rx_freq_slider.set_value(self.rx_freq)
        self._rx_freq_text_box.set_value(self.rx_freq)

    def get_rx_fine(self):
        return self.rx_fine

    def set_rx_fine(self, rx_fine):
        self.rx_fine = rx_fine
        self.set_rx_freq_val(self.rx_freq+(self.rx_coarse+self.rx_fine))
        self._rx_fine_slider.set_value(self.rx_fine)
        self._rx_fine_text_box.set_value(self.rx_fine)

    def get_rx_coarse(self):
        return self.rx_coarse

    def set_rx_coarse(self, rx_coarse):
        self.rx_coarse = rx_coarse
        self.set_rx_freq_val(self.rx_freq+(self.rx_coarse+self.rx_fine))
        self._rx_coarse_slider.set_value(self.rx_coarse)
        self._rx_coarse_text_box.set_value(self.rx_coarse)

    def get_xlate_filter_taps(self):
        return self.xlate_filter_taps

    def set_xlate_filter_taps(self, xlate_filter_taps):
        self.xlate_filter_taps = xlate_filter_taps

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self._width_slider.set_value(self.width)
        self._width_text_box.set_value(self.width)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, self.trans, firdes.WIN_HAMMING, 6.76))

    def get_variable_chooser_1(self):
        return self.variable_chooser_1

    def set_variable_chooser_1(self, variable_chooser_1):
        self.variable_chooser_1 = variable_chooser_1
        self._variable_chooser_1_chooser.set_value(self.variable_chooser_1)

    def get_tv_freq(self):
        return self.tv_freq

    def set_tv_freq(self, tv_freq):
        self.tv_freq = tv_freq

    def get_trans(self):
        return self.trans

    def set_trans(self, trans):
        self.trans = trans
        self._trans_slider.set_value(self.trans)
        self._trans_text_box.set_value(self.trans)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.width, self.trans, firdes.WIN_HAMMING, 6.76))

    def get_squelch(self):
        return self.squelch

    def set_squelch(self, squelch):
        self.squelch = squelch
        self.analog_simple_squelch_cc_0.set_threshold(self.squelch)
        self._squelch_slider.set_value(self.squelch)
        self._squelch_text_box.set_value(self.squelch)

    def get_sql_lev(self):
        return self.sql_lev

    def set_sql_lev(self, sql_lev):
        self.sql_lev = sql_lev
        self._sql_lev_slider.set_value(self.sql_lev)
        self._sql_lev_text_box.set_value(self.sql_lev)

    def get_rx_freq_val(self):
        return self.rx_freq_val

    def set_rx_freq_val(self, rx_freq_val):
        self.rx_freq_val = rx_freq_val
        self._rx_freq_val_static_text.set_value(self.rx_freq_val)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_dev(self):
        return self.dev

    def set_dev(self, dev):
        self.dev = dev
        self._dev_slider.set_value(self.dev)
        self._dev_text_box.set_value(self.dev)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation

    def get_af_gain(self):
        return self.af_gain

    def set_af_gain(self, af_gain):
        self.af_gain = af_gain
        self._af_gain_slider.set_value(self.af_gain)
        self._af_gain_text_box.set_value(self.af_gain)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = osmo_nfm_rx()
    tb.Start(True)
    tb.Wait()
