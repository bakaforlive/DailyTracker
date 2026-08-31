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
Clone the repo and install project dependencies:
```bash
git clone https://github.com/bakaforlive/DailyTracker.git
cd DailyTracker

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```
## Configuration
This app requires a Google Gemini API key to generate accountability punishments.
### 1. Get an API Key
* Visit [Google AI Studio](https://aistudio.google.com/apikey).
* Login into your Google account.
* Click "Create API key" and create your API key.
### 2. Create an environment variable
* In app's directory create .env file:
```bash
$ touch .env
```
* Then, open it with your text editor.

* Paste to this file:
```text
GEMINI_API_KEY=your_api_key_here
```

## Usage
To execute the program, run
```bash
$ python tracker.py
Did you brush your teeth? [y/n]

```
Answer these questions by typing "y" or "n".

### Flags
You can use flags to manipulate your routines:
* -a, --add - adds new routine to list.
* -d, --delete - deletes routine by name.
* -l, --list - prints all current routines.
* -v, --version - prints current app version.

Example:
```bash
$ python tracker.py -l
1: brush teeth
```
