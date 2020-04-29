# Audio Service that looks at the frequency of real time input

### TODO:

- [ ] Create our own spectograph
- [ ] Create analysis
- [ ] Integrate with rtmixer
- [ ] Send out a frequency to match that rate
- [X] Yoink someone else's matplotlib graph

# How to run the Repo
**If you follow the terminal version keep it open at all times, also command prompt is slightly different**

First clone the repo, with this command in your terminal.
```bash
pip3 install virtualenv 
git clone https://github.com/odhjoseph/AudioService.git
```
**Note:** If you're running windows and this doesn't work, that's because git doesn't come pre-installed. 
Instead just download the zip file and unzip it wherever you want. Then open a terminal in AudioService by left clicking the folder. Also works on folders on macs. Also typing cmd in the directory bar works.
- [Guide on opening Terminals in Windows](https://www.youtube.com/watch?v=bgSSJQolR0E)

Enter that directory in your terminal, or open a terminal from that folder.
Command to change directory

## How to setup a python virtual environment 
```bash
python3 -m venv piAudio
```

>**Note:** If you followed this guide, you probably don't have mutiple versions of python installed, you probably can just use ```python``` instead of ```python3```

On Windows
```bash
py -m venv piAudio
```

Run these commands in your terminal
```bash
source recording/piAudio/bin/activate 
pip3 install -r recording/requirements.txt 
python3 recording/example.py
```
>**Note:** I put my python virtual environment inside the recording folder

If one of these don't work it's probably because of installation problems.

#### Installation Troubleshoot
These should return a directory structure. If not they aren't installed, so download python3.

*Windows trouble shoot*
```bash
where python3 
```
*Unix/Linux* macOS = unix 
```bash
which python3 
```

## Can't install requirements.txt

#### Unix/Linux
Run this if you get this error:
 **"ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied:"**
```bash
sudo -H pip3 install -r recording/newRequirements.txt 
```
>**Note: My system setup is somewhat odd and I can just install with sudo, you'll probably just want to use the --user flag so you don't need sudo for pip. When in doubt --user before sudo.**

#### Windows
Check if you're running the terminal with administrative rights 

### Adding a new mic, requires sounddevice to be re-initialized 
```python
sd._terminate()
sd._initialize()
```
This stops any ongoing stream, might need to find a fork of portaudio that allows it. Most forks aren't updated, so good luck. Afer you can query agian.

This stops the listening, but when streaming is called it will continue to appear active to Windows until another audio based serviced is opened/restarted. So, if you're in a call you might need to open that call service again in order for the mic to work.


```python 
sd.query_devices()
```


### Specs 
- Running on AV LINUX
- Raspberry Pi $
- Audio Input Blue Snowball

### WIP: Dependencies

[rtmixer](https://github.com/spatialaudio/python-rtmixer)

