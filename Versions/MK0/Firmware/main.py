from gestures import *
from recognition import current_state

def main():
    servos = setup()

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

# main_guard
if __name__ == "__main__":
    main() 