## Python installation (mac)

First, you'll need to install Homebrew if it's not already installed. Homebrew is a package manager for macOS that simplifies the installation of software.
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Once Homebrew is installed, use it to install Python:
```
brew install python
```

To ensure that Python 3 was installed successfully, open a terminal and run the following command:
```
python3 --version
```

It's a good practice to ensure that pip (Python's package installer) is up-to-date. You can upgrade pip using the following command:
```
pip3 install --upgrade pip
```

Install the requirements included in the current folder
```
pip3 install -r requirements.txt
```

## Assignment instructions
Navigate to the `assets` folder and use the `asset_creator.py` script to generate 6 screenshots of the 3D views of the map that will be used as a background for the game. You should progressively cover all the Tiber river.

After generating the screenshots, copy them to the `challenge` folder and open the `game.py` script. You should modify it in such a way that a character (pygame circle) can move on top of each screenshot. When the character passes through one horizontal border of the screen, it will appear on the opposite border and continue the exploration of the next screenshot tile, so that it can visit the whole Tiber river.

## Program instructions
### instructions for asset_creator script

WASD = Camera translations

Arrows = Camera rotations

Z = Zoom out

X = Zoom in

Enter = Save screenshot
