# Frequency Guide

## Detecting Frequency

- [Discrete Fourier Transform](https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.fft.html)

- [Scipy FTT](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.fft.html)

Problem with FTT in order to get the live input to be .1 hertz of the one we're cancelling out, it needs to be in 10 second intervals.  
So the frequency sent out would be in 10 second delays

A better/easier idea would be using filters, which cutt off frequencies at that range

## Finding peaks

- [Scipy Peaks](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html)
    - [example](https://dsp.stackexchange.com/questions/36236/estimate-the-wavelength-of-an-oscillatory-signal)

    
### Last session research
https://github.com/spatialaudio/python-sounddevice/tree/master/examples
https://github.com/spatialaudio/python-sounddevice/blob/master/sounddevice.py
https://github.com/spatialaudio/python-sounddevice/issues
    - Recreate raw input stream, forgot what issue it was