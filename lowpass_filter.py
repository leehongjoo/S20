# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:33:56 2020

@author: hong joo LEE
"""

from scipy.signal import butter, lfilter, lfilter_zi
from scipy import signal


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    #y = signal.filtfilt(b, a, data)
    #zi = lfilter_zi(b, a)
    y = lfilter(b, a, data)#, zi=zi * data[0])
    return y
