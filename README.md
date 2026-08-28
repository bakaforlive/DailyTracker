## About
DailyTracker is a Python CLI application for tracking daily routines.

It will ask a bunch of questions (e.g. "Did you do your chores?"). Answer them by typing "y" (yes) or "n" (no).
If you answered "n" to at least 1 daily routine, then AI will generate you a punishment. 

## Requirements
To use DailyTracker, you need to install Python Interpreter.
### Windows
You can install Python from Microsoft Store or from official [site](https://www.python.org/downloads/).
### Linux
You can install python with your package manager.

Arch Linux
```bash
$ sudo pacman -S python
```

Debian/Ubuntu
```bash
$ sudo apt install python
```

Fedora/RHEL
```
$ sudo dnf install python
```
## Installation

```bash
git clone https://github.com/bakaforlive/DailyTracker.git
cd DailyTracker

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage
To execute the program, run
```bash
$ python tracker.py
Did you brush your teeth? [y/n]

```
Answer these questions by typing "y" or "n".
