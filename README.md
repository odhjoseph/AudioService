# Audio Service that looks at the frequency of real time input

### TODO:

- [ ] Create our own spectograph
- [ ] Create analysis
- [ ] Send out a frequency to match that rate
- [X] Yoink someone else's matplotlib graph

# How to run the Repo
**If you follow the terminal version keep it open at all times, also command prompt is slightly different**

First clone the repo, with this command in your terminal.
```bash
git clone https://github.com/odhjoseph/AudioService.git
```
**Note:** If you're running windows and this doesn't work, that's because git doesn't come pre-installed. 
Instead just download the zip file and unzip it wherever you want. Then open a terminal in AudioService by left clicking the folder. Also works on folders on macs. Also typing cmd in the directory bar works.
- [Guide on opening Terminals in Windows](https://www.youtube.com/watch?v=bgSSJQolR0E)

Enter that directory in your terminal, or open a terminal from that folder.
Command to change directory

Run these commands in your terminal
```bash
source recording/piAudio/bin/activate 
pip3 install -r recording/newRequirements.txt 
python3 recording/example.py
```

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

#### Can't install requirements.txt

##### Unix/Linux
Run this if you get this error:
 **"ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied:"**
```bash
sudo -H pip3 install -r recording/newRequirements.txt 
```

##### Windows
Check if you're running the terminal with administrative rights 

### Specs 
- Running on AV LINUX
- Raspberry Pi $
- Audio Input Blue Snowball

