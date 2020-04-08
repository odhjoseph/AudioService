import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np 

duration = 10
#Personal microphone to listen on    
#9 Blue Snowball: USB Audio (hw:2,0), ALSA (2 in, 0 out)


#Callback stream to handle current real data 
def callback(indata, outdata, frames, times, status):
    if status:
        print(status)
    outdata[:] = indata #copies the entire array
    print(outdata)
    with sd.RawInputStream(channels=2, dtype = 'int64', callback=callback): #not read in as a numpy array
        sd.sleep(int(duration * 1000))


#https://github.com/spatialaudio/python-sounddevice/blob/master/examples/rec_unlimited.py
#Hardcode arguments passed above to raspberry pi