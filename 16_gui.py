import pyautogui

print(pyautogui.size())
width, height= pyautogui.size()

print(pyautogui.position())         # top left corner is 0,0

pyautogui.moveTo(10, 10)
pyautogui.moveTo(500, 500, duration=1.5)

pyautogui.moveRel(500, 0, duration=1)
pyautogui.moveRel(0, -500, duration=1)

pyautogui.click(476, 22)
# To activate failsafe, move cursor to top left corner

pyautogui.displayMousePosition()

######################################################################

pyautogui.typewrite('This was written by code not a human', interval=0.2)       # This was written by code not a human.!
pyautogui.typewrite(['!', 'left', '.'], interval=0.5)

print(pyautogui.KEYBOARD_KEYS)
pyautogui.hotkey('ctrl', 'o')

######################################################################

pyautogui.screenshot('screenshot.png')

pyautogui.locateOnScreen('calc7key.png', confidence=0.9)                # it has to match the image exactly, cannot be partially hidden
print(pyautogui.locateCenterOnScreen('calc7key.png', confidence=0.9))
pyautogui.moveTo((1349,572), duration=1)
pyautogui.click()