mao = 0

def on_gesture_shake():
    global mao
    mao = randint(1, 3)
    if mao == 1:
        basic.show_icon(IconNames.SQUARE)
    elif mao == 2:
        basic.show_icon(IconNames.SMALL_SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
