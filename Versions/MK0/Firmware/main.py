from gestures import *

def main():
    servos = setup()

    print("Enter a keybind: \n")
    print("Close Hand = a, Open Hand = b, Peace Sign = c")
    button = input()
    if button == 'a':
        close_hand(servos)
    elif button == 'b':
        open_hand(servos)
    elif button == 'c':
        peace_sign(servos)

# main_guard
if __name__ == "__main__":
    main() 