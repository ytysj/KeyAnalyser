from pynput import keyboard
import time
import threading
import database
import combined_key
import log

lock = threading.Lock()     # 创建线程锁

pressed_keys = {}
cur_id = 0

def on_press(key):
    if key not in pressed_keys:
        pressed_keys[key] = time.time()   # 记录按键的起始时间

def on_release(key):
    global cur_id
    if key == keyboard.Key.esc:        # 按下ESC键停止监听
        return False
    if key in pressed_keys:
        last_time = int(1000 * (time.time() - pressed_keys[key]))
        key_str = str(key).replace("'", "")
        if ('\\x' in key_str):
            combined_key_list = combined_key.unpack_combined_key(key)
            if(combined_key_list!=None):
                new_key = '+'.join(combined_key_list)
                key_str = new_key
                log.debug("按下组合按键:", new_key)
        else:
            log.debug("按下:", key)
        
        key_num = 0
        if not isinstance(key, keyboard.KeyCode):   #判断是特殊按键
            key_num = key.value.vk
        else:
            key_num = key.vk

        if(last_time>1000): #根据按下时间判断按键类型
            key_type = 0
        else:
            key_type = 1

        lock.acquire()      # 获取线程锁
        try:
            time_stamp = int(1000 * pressed_keys[key])
            database.add_item(cur_id, key_num, key_str, key_type, time_stamp, last_time)
            cur_id += 1
            del pressed_keys[key]
        except Exception as e:
            log.error("数据库操作出错:", e)
        finally:
            lock.release()  # 释放线程锁

if __name__ == "__main__":
    log.log_init()
    log.debug("KeyAnalyser start up")

    database.init_db()
    cur_id = database.query_max_id()    #获取最大键值
    if(cur_id!=0):
        cur_id += 1

    log.debug("KeyAnalyser is listenning")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    log.debug("KeyAnalyser quit")