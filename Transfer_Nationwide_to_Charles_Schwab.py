import time, datetime
from datetime import timedelta
from datetime import date
from time import sleep
import webbrowser

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
    pass 
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
def OpenMicrosoftEdge():
    # browser = RoboBrowser(history=True)
    # browser.open('https://www.nrsflorida.com/iApp/rsc/login.x')
    webbrowser.open_new('https://www.nrsflorida.com/iApp/rsc/login.x')
    pass
def NavigateNRS_Florida():
    duration = 3
    # Click "Log in"
    pyautogui.moveTo(1137, 526, duration)
    pyautogui.click()
    # Click "Manage account"
    pyautogui.moveTo(889, 207, 3*duration)
    pyautogui.click()
    # Click "Change investments"
    pyautogui.moveTo(485, 326, duration)
    pyautogui.click()
    # Click "Manage Your Self-directed Option (SDO)"
    time.sleep(duration)
    pyautogui.hotkey('pagedown')
    time.sleep(duration)
    pyautogui.moveTo(535, 975, duration)
    pyautogui.click()
    # Click "One time transfer from your core account to Schwab PCRA"
    pyautogui.moveTo(383, 822, duration)
    pyautogui.click()
    # Click "Percent"
    pyautogui.moveTo(383, 991, duration)
    pyautogui.click()
    # Click "Next"
    pyautogui.hotkey('pagedown')
    pyautogui.moveTo(1489, 358, duration)
    pyautogui.click()
    # Click "Next"
    pyautogui.moveTo(1492, 819, duration)
    pyautogui.click()
    # Type "100"
    pyautogui.moveTo(1475, 744, duration)
    pyautogui.click()
    pyautogui.hotkey('1','0','0', interval=duration)
    # Click "Next"
    pyautogui.moveTo(1492, 897, duration)
    pyautogui.click()
    # Click "Submit"
    pyautogui.moveTo(1492, 897, duration)
    pyautogui.click()
    pass
if __name__ == "__main__":
    # pyautogui1()
    OpenMicrosoftEdge()
    NavigateNRS_Florida()
    pass