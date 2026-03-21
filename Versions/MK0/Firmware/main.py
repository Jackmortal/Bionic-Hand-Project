from gestures import *

def main():
    servos = setup()

    while True:
        print("Enter a keybind: \n")
        print("Close Hand = a, Open Hand = b, Peace Sign = c, Exit = x")
        button = input()
        if button == 'a':
            close_hand(servos)
        elif button == 'b':
            open_hand(servos)
        elif button == 'c':
            peace_sign(servos)
        elif button == 'd':
            thumbs_up(servos)
        elif button == 'x':
            break

# main_guard
if __name__ == "__main__":
    main() 