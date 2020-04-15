# Scuffed Versioning

- requirements.txt 0.0.1
- newRequirements.txt 0.0.2

Whatever is in recording is the main version

```
example.py:110: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
```

You're missing tk. Don't install it with pip. 

## ArchLinux 
```bash
sudo pacman -S tk
```

## Apt Gang 
```bash 
sudo apt-get install python3-tk
```
