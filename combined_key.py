from pynput import keyboard

#list all combined key
dict_combined_key = {
    "\x1a":["ctrl", 'z'], "\x18":["ctrl", 'x'], "\x03":["ctrl", 'c'], "\x16":["ctrl", 'v'], \
    "\x02":["ctrl", 'b'], "\x0e":["ctrl", 'n'], "\x1b":["ctrl", '['], "\x1d":["ctrl", ']'], \
}

def unpack_combined_key(key):
    if key in dict_combined_key:
        return dict_combined_key[key]
    else:
        return None

if __name__ == "__main__":
    print("combined key module test start")
    rst = unpack_combined_key("\x1a")
    print(rst)
    rst = unpack_combined_key("\x18")
    print(rst)
    rst = unpack_combined_key("\x1b")
    print(rst)
    rst = unpack_combined_key("\x99")
    print(rst)