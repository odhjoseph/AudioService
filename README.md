# Audio Service that looks at the frequency of real time input

### TODO:

- [ ] Create our own spectograph
- [ ] Create analysis
- [ ] Send out a frequency to match that rate
- [X] Yoink someone else's matplotlib graph

# How to run the Repo
Bash wasn't working so just run these commands in your terminal 
- source recording/piAudio/bin/activate 
- pip3 install -r recording/newRequirements.txt 
- python3 recording/example.py

If one of these don't work it's probably because of installation problems.

#### Installation Troubleshoot

*Windows trouble shoot*

echo $PATH \
where python3 

*macOS*
which python3 

If that doesn't work might need to run it as sudo, but you should fix the --user issue

*Unix/Linux*
Run this if you get this error:
 **"ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied:"**

sudo - H pip3 install -r recording/newRequirements.txt 

*Windows*
Check if you're running you're terminal with administrative rights 

### Specs 
- Running on AV LINUX
- Raspberry Pi $
- Audio Input Blue Snowball

