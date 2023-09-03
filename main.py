from pynput import keyboard
import time
import sqlite3
import database
import combined_key

pressed_keys = {}

def on_press(key):
    if key not in pressed_keys:
        # 记录按键的起始时间
        pressed_keys[key] = time.time()

def on_release(key):
    if key == keyboard.Key.esc:
        # 按下ESC键停止监听
        return False
    if key in pressed_keys:
        rls_time = time.time()
        if ('\\x' in str(key)):
            combined_key_list = combined_key.unpack_combined_key(key)
            if(combined_key_list!=None):
                new_key = '+'.join(combined_key_list)
                print("按下组合按键:", new_key, "持续时间:", rls_time - pressed_keys[key])
        else:
            print("按下:", key, "持续时间:", rls_time - pressed_keys[key])
        #if not isinstance(key, keyboard.KeyCode):   #判断是特殊按键
        #    print("特殊按键:", key, "持续时间:", time.time() - pressed_keys[key])
        del pressed_keys[key]


if __name__ == "__main__":
    print("KeyAnalyser is running")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()