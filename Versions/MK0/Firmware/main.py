from gestures import *
from recognition import recognize_frame, settings
import recognition
import threading

def main():
    servos = setup()
    state = recognition.current_state

    # Creates a thread for recognize_frame so that new states are captured
    # from its loop, while also looping the gesture control in main.
    threading.Thread(target = recognize_frame, args=(settings,)).start()

    while True:
        if state == 'None':
            break
        elif state == 'Closed_Fist':
            close_hand(servos)
        elif state == 'Open_palm':
            open_hand(servos)
        elif state == 'Victory':
            peace_sign(servos)
        elif state == 'Thumb_Up':
            thumbs_up(servos)
        elif state == 'Pointing_Up':
            pointing(servos)
        elif state == 'ILoveYou':
            rock_on(servos)

# main_guard
if __name__ == "__main__":
    main() 