import matplotlib.pyplot as plt
import sounddevice as sd

#sd._initialize()

fs = 44100  # Sample rates

#Selecting device is needed on windows????
sd.query_devices()

seconds = 5  
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait() 
sd._terminate() 

#Prints left and right input
print(myrecording)

plt.ion()
plt.figure()
plt.plot(myrecording)
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.title("Waveform")
plt.show()


