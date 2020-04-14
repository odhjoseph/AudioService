from scipy.io.wavfile import read
import sounddevice as sd 
import scipy.signal as signal
from scipy.io.wavfile import read

class audioBuffer():

    def __init__(self, audioFile, audioStreamType: str, twoStreamInput: bool, stream = None):
        self.audioFile = audioFile
        self.audioStreamType = audioStreamType
        self.twoStreamInput = twoStreamInput
        self.stream = stream

    def findPeaks(self):
        return signal.find_peaks(self.audioFile)  

    @property
    def audioStreamType(self):
        return self.audioStreamType

    @audioStreamType.setter
    def audioStreamType(self, streamType):
        streamTypes = {"Stream", "InputStream", "OutputStream, RawInputStream, RawStream, OutputStream, RawOutputStream"}

        if self.audioStreamType not in streamTypes:
            raise AttributeError
        
        self.audioStreamType = streamType

    @property
    def stream(self):
        return self.stream

    @stream.setter
    def stream(self, stream):
        #Overcomplicated way to do it
        #TODO: Create dict, check if dict is in there, call it from the dict fucntion key
        module = __import__('sounddevice')
        streamType = getattr(module, self.audioStreamType)
        return streamType()        

    



