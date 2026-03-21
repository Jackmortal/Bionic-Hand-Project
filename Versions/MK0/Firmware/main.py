from gestures import setup, close_hand, open_hand

def main():
    servos = setup()

    print("Enter a keybind (a or b): ")
    button = input()
    if button == 'a':
        close_hand(servos)
    elif button == 'b':
        open_hand(servos)

# main_guard
if __name__ == "__main__":
    main() 