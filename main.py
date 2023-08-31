from pynput import keyboard

def on_press(key):
    print(key)

if __name__ == "__main__":
    print("KeyAnalyser is running")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()