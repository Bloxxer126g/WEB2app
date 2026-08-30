# Install Python
```
# Windows
winget install python.python.3.14

# Debian
sudo apt update
sudo apt install python3 python3-pip

# Red hat (fedora)
sudo dnf check-update
sudo dnf install python3 python3-pip

# Arch linux
sudo pacman -Syu
sudo pacman -S python python-pip
```
# Download main.py
https://github.com/Bloxxer126g/WEB2app/blob/main/main.py

# CD into the same folder as main.py

# Package the app
```pyinstaller -F main.py --collect-all customtkinter```
