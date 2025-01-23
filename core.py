import vgamepad as vg
import time

#Left stick
RELEASE = [128, 128] #0
FORWARD = [128, 255] #1
RIGHT = [255, 128] #2
LEFT = [0, 128] #3
BACK = [128, 0] #4
#Right stick
#Right stickは同期処理が難しいため今後処理系統が変更になる可能性がある
URIGHT = [255, 255] #5
ULEFT = [0, 255] #6
LRIGHT = [255, 0] #7
LBLEFT = [0,0] #8

gamepad = vg.VDS4Gamepad()

#Left stick input
def lstick_input(dir):
    if dir == 0: gamepad.left_joystick(x_value=RELEASE[0], y_value=RELEASE[1])
    elif dir == 1: gamepad.left_joystick(x_value=FORWARD[0], y_value=FORWARD[1])
    elif dir == 2: gamepad.left_joystick(x_value=RIGHT[0], y_value=RIGHT[1])
    elif dir == 3: gamepad.left_joystick(x_value=LEFT[0], y_value=LEFT[1])
    elif dir == 4: gamepad.left_joystick(x_value=BACK[0], y_value=BACK[1])
    gamepad.update()
    time.sleep(0.05)
    return

#Right stick input
def rstick_input(dir):
    if dir == 0: gamepad.right_joystick(x_value=RELEASE[0], y_value=RELEASE[1])
    elif dir == 1: gamepad.right_joystick(x_value=FORWARD[0], y_value=FORWARD[1])
    elif dir == 2: gamepad.right_joystick(x_value=RIGHT[0], y_value=RIGHT[1])
    elif dir == 3: gamepad.right_joystick(x_value=LEFT[0], y_value=LEFT[1])
    elif dir == 4: gamepad.right_joystick(x_value=BACK[0], y_value=BACK[1])
    elif dir == 5: gamepad.right_joystick(x_value=URIGHT[0], y_value=URIGHT[1])
    elif dir == 6: gamepad.right_joystick(x_value=ULEFT[0], y_value=ULEFT[1])
    elif dir == 7: gamepad.right_joystick(x_value=URIGHT[0], y_value=URIGHT[1])
    elif dir == 8: gamepad.right_joystick(x_value=ULEFT[0], y_value=ULEFT[1])
    gamepad.update()
    time.sleep(0.05)
    return

#QB input
#ssflag 1:SS 0:NornalQB
def qb_input(dir, ssflag):
    lstick_input(dir)
    if ssflag == 1:
        gamepad.right_trigger(value=141)
        gamepad.update()
        time.sleep(0.366)
    gamepad.right_trigger(value=220)
    gamepad.update()
    time.sleep(0.05)
    gamepad.right_trigger(value=0)
    gamepad.update()
    lstick_input(0)
    time.sleep(0.05)
    return

#QT input
#ssflag 1:SS 0:NornalQB
def qt_input(dir, ssflag):
    lstick_input(0)
    rstick_input(dir)
    if ssflag == 1:
        gamepad.right_trigger(value=141)
        gamepad.update()
        time.sleep(0.366)
    gamepad.right_trigger(value=220)
    gamepad.update()
    time.sleep(0.05)
    gamepad.right_trigger(value=0)
    gamepad.update()
    rstick_input(0)
    time.sleep(0.05)
    return

#Attack input
#pos 1:right 2:left 3:shoulder
def attack_input(pos):
    if pos == 1: gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
    elif pos == 2: gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
    elif pos == 3: gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    gamepad.update()
    time.sleep(0.05)

#Attack off input
#pos 1:right 2:left 3:shoulder
def attack_input(pos):
    if pos == 1: gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
    elif pos == 2: gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
    elif pos == 3: gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    gamepad.update()
    time.sleep(0.05)

#Purge input
#pos 1:right 2:left 3:shoulder
def purge_input(pos):
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    gamepad.update()
    time.sleep(0.05)
    if pos == 1: gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
    elif pos == 2: gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
    elif pos == 3: gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    gamepad.update()
    time.sleep(0.05)
    gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
    gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
    if pos == 1: gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
    elif pos == 2: gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
    elif pos == 3: gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
    gamepad.update()
    time.sleep(0.05)
    return

#Boost input
#sens: 0~255
def boost_input(sens):
    gamepad.left_trigger(value=sens)
    gamepad.update()
    time.sleep(0.05)
    return

#Boostoff input
def boostoff_input():
    gamepad.left_trigger(value=0)
    gamepad.update()
    time.sleep(0.05)
    return