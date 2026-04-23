from gestures import *
from recognition import recognize_frame, settings, current_state
import threading

def main():
    servos = setup()

    # Creates a thread for recognize_frame so that new states are captured
    # from its loop, while also looping the gesture control in main.
    threading.Thread(target = recognize_frame, args=(settings,)).start()

    while True:
        if current_state == 'None':
            break
        elif current_state == 'Closed_Fist':
            close_hand(servos)
        elif current_state == 'Open_palm':
            open_hand(servos)
        elif current_state == 'Victory':
            peace_sign(servos)
        elif current_state == 'Thumb_Up':
            thumbs_up(servos)
        elif current_state == 'Pointing_Up':
            pointing(servos)
        elif current_state == 'ILoveYou':
            rock_on(servos)

# main_guard
if __name__ == "__main__":
    main() 