# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:50:05 2020

@author: hong joo LEE
"""
from scipy.signal import butter, lfilter, filtfilt

def butter_bandpass(lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    #y = filtfilt(b, a, data)
    return y