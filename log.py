import logging

def log_init():
    logging.basicConfig(filename='debug.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def is_log_inited():
    return len(logging.root.handlers) > 0

def debug(*args, **kwargs):
    message = ' '.join(map(str, args))
    if(is_log_inited()):
        logging.info(message)  # 记录日志信息
    print(message, **kwargs)  # 打印到终端

def error(*args, **kwargs):
    message = ' '.join(map(str, args))
    if(is_log_inited()):
        logging.error(message)  # 记录日志信息
    print(message, **kwargs)  # 打印到终端