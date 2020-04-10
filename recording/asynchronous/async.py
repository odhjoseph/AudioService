#Module file to call for wave analysis

import wave, struct

def readFrames(audioFile, frames: int):
    waveFile = wave.open(audioFile, 'r')
    audioData = waveFile.readframes(frames)
    return struct.unpack("<13h", audioData)