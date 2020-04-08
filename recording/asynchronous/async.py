#Module file to call for wave analysis
#Currently not realtime

import scipy.signal as signal
import scipy.fftpack as ftt, ifft

#takes in numpy array
def peak(wave):
    #local check .find_peaks_cwt for vector analysis
    peaks = signal.find_peaks(wave)
    return peaks

# Domain - A mask array with the same number of dimensions as a. Each dimension should have an odd number of elements.
def filter(filterPass, soundArray, domain, rank):
    if filterPass(filterPass) == "Invalid Filter":
        raise InputError

    if filterPass(filterPass) == "high":
        high()

    elif filterPass(filterPass) == "low":
        low()
    else:
        specificFilter()

    return

# discrete Fourier transform
def fftTransform():
    return

# Filter Switch

def high():
    return 
    
def low():
    return

def specificFilter(): 
    return 

def filterPass(filter):
    filter = filter.lower()

    switcher = {
        0: high,
        1: low,
        2: specificFilter
    }

    return switcher.get(filter, "Invalid Filter")


#Move to error handling file eventually
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message