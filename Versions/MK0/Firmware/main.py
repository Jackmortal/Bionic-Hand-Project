from gestures import *
import recognition

def main():
    servos = setup()

    while True:
        state = recognition.current_state
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