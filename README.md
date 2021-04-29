# RemotePcControl

**Python telegram** bot with **aiogram** to control with **Windows**

## Requirments

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
pip install aiogram
pip install configparser
pip install asyncio
pip install mss
pip install urllib
pip install platform
pip install subprocess
pip install webbrowser
pip install keyboard
pip install win32clipboard
pip install pyautogui
pip install psutil
pip install pywin32
```

## Usage
Enter your user name and bot_token into: **src/config.ini**
```ini
[bot_config]
owner_username = your_user_name
bot_token = XXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
browser_path = C://Program Files (x86)//Google//Chrome//Application//chrome.exe
browser_name = chrome
```
Then launch: **src/main.py**

## Contributor
@maksutovnurda