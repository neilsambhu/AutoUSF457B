import time, datetime
from datetime import timedelta
from datetime import date
from time import sleep
from tqdm import tqdm

import pyautogui
def pyautogui1():    
    "click Microsoft Edge on taskbar"
    time.sleep(5)
    print(pyautogui.position())

    # duration = 10
    # # login button
    # pyautogui.moveTo(780,587,duration)
    # pyautogui.click()

    # time.sleep(duration)   
def pyautogui2():
    duration = 3
    # login button
    pyautogui.moveTo(780,587,duration)
    pyautogui.click()

    # accept button
    pyautogui.moveTo(353,391,duration)
    pyautogui.click()

    # copy authorization code
    pyautogui.moveTo(310,266,duration)
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'c')
    
    # time.sleep(duration)
    import win32clipboard
    win32clipboard.OpenClipboard()
    authorizationCode = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return authorizationCode
def pyautogui2_1():
    "get 5-digit auth code from URL"
    duration = 2
    # login button
    pyautogui.moveTo(780,587,4)
    # pyautogui.moveTo(780,587,10)
    pyautogui.click()

    # accept button
    pyautogui.moveTo(353,391,5)
    pyautogui.click()

    # copy URL with authorization code
    pyautogui.moveTo(206,51,duration)
    pyautogui.tripleClick()
    pyautogui.hotkey('ctrl', 'c')
    
    # time.sleep(duration)
    import win32clipboard
    win32clipboard.OpenClipboard()
    url_etrade = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    
    import urllib.parse as urlparse
    from urllib.parse import parse_qs
    parsed = urlparse.urlparse(url_etrade)
    authorizationCode = parse_qs(parsed.query)['oauth_verifier']
    # print(authorizationCode)
    return authorizationCode

if __name__ == "__main__":
    pyautogui()