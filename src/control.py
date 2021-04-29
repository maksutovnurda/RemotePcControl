import platform
import subprocess
import webbrowser
import keyboard
import win32clipboard
import pyautogui
import psutil

def shutdown():
    if platform.system() == "Windows":
        subprocess.call('shutdown /s')
    else:
        subprocess.call('shutdown -h now')

def restart():
    if platform.system() == "Windows":
        subprocess.call('shutdown /r')
    else:
        subprocess.call('reboot')
def openSite(browser_name, browser_path, link):
	webbrowser.register(browser_name, None, webbrowser.BackgroundBrowser(browser_path))
	webbrowser.get(browser_name).open_new(link)
def close():
	keyboard.send('alt+f4')
def write(text):
	keyboard.write(text)
def getClipBoard():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data
def getPageLink():
	pyautogui.press(['f6'])
	pyautogui.keyDown('ctrl')
	pyautogui.press(['c'])
	pyautogui.keyUp('ctrl') 

	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data
def alert(text):
	pyautogui.alert(text)
def press(button, times):
	for i in range(times):
		pyautogui.press([button])
def status():
	status = ''
	if platform.system() == "Windows":
		status += "\n*OS:* _Windows "+platform.win32_ver()[0]+"_\n"
	status += "*CPU:* "+str(psutil.cpu_percent())+"% \n"
	status += "*RAM:* _"+str(int(psutil.virtual_memory().percent))+"%_\n"
	if psutil.sensors_battery():
		if psutil.sensors_battery().power_plugged is True:
			status += "*Charge:* _" + str(format(psutil.sensors_battery().percent, ".0f"))+ "% | Charging_"
		else:
			status += "*Battery:* _" + str(format(psutil.sensors_battery().percent, ".0f")) + "%_"
	return status