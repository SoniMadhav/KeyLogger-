#Controllin your mouse
#listing your mouse
#Controllin your keyboard
#listening to your keyboard -will be finally used in our keylogger

from pynput.mouse import Controller
# from pynput.keyboard import Controller

#move the mouse to the position (left to right(x) 100, top to bottom(y)  100)
def controlMouse():  # Fix the typo in the function name
    mouse = Controller()
    mouse.move(-200, 20)


controlMouse()  # Call the function


def controlKeyboard():
    keyword=Controller()
    keyword.type("soni Madhav")

# controlKeyboard()
