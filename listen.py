from pynput.mouse import Listener


# Function to handle mouse movement
def on_move(x, y):
    print('Position of current mouse: {0}'.format((x, y)))


# Creating the listener
with Listener(on_move=on_move) as l:
    l.join()
