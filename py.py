import pyautogui
import time

"""\
distance = 200
while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.5)   # move down
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up
"""

def click(imgUrl):
	coord = pyautogui.locateCenterOnScreen(imgUrl, confidence = 1)
	if coord != None:
		pyautogui.click(coord)
	time.sleep(1)
	
def rightClick(imgUrl):
	coord = pyautogui.locateCenterOnScreen(imgUrl, confidence = 1)
	if coord != None:
		pyautogui.click(coord, button='right')
	time.sleep(1)

click("iniciar.png")
click("calc.png")
click("num1.png")
click("x.png")
click("num2.png")
rightClick("result.png")
click("copy.png")
click("google.png")
click("pesquisa.png")



pyautogui.typewrite("leonardo2\n")



