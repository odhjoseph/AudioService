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

"""
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args(remaining)
"""

#https://github.com/spatialaudio/python-sounddevice/blob/master/examples/rec_unlimited.py
#Hardcode arguments passed above to raspberry pi