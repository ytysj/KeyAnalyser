import sqlite3

conn = None
cursor = None

#初始化数据库
def init_db():
    global conn, cursor
    print("init_db")
    # 连接到数据库（如果数据库不存在，则会创建一个新的数据库文件）
    conn = sqlite3.connect('key_db.db')
    # 创建一个游标对象，用于执行SQL语句
    cursor = conn.cursor()

    # id INT类型，主键，数据序号
    # key_num INT类型，按键号码
    # character TEXT类型，按键文字
    # key_state INT类型，按键状态（0：点击，1：长按）
    # timestamp INT类型，时间戳
    # last_time INT类型，按下持续时间（单位：ms）

    cursor.execute('''CREATE TABLE IF NOT EXISTS key_analyser
                (id INT PRIMARY KEY NOT NULL,
                 key_num INT NOT NULL,
                 character TEXT NOT NULL,
                 key_state INT NOT NULL,
                 timestamp INT NOT NULL,
                 last_time INT NOT NULL)''')


# 添加数据
# id 主键，数据序号
# key_num 按键号码
# character 按键文字
# key_state 按键状态（0：点击，1：长按）
# timestamp 时间戳
# last_time 按下持续时间（单位：ms）
def add_item(id, key_num, character, key_state, timestamp, last_time):
    global conn, cursor
    try:
        str = "INSERT INTO key_analyser (id, key_num, character, key_state, timestamp, last_time)VALUES "\
            + f"({id}, {key_num}, '{character}', {key_state}, {timestamp}, {last_time})"
        #print("add_item:", str)
        cursor.execute(str)
        conn.commit()
    except Exception as e:
        print(f"add_item({id}) error!", e)

#查询单个数据
def query_item(id):
    global conn, cursor
    print(f"query_item({id})")
    # 查询"key_analyser"表格中id为"1"的数据。
    # SELECT *表示查询所有字段，FROM key_analyser表示从"key_analyser"表格中进行查询。
    # WHERE id="1"表示查询id为"1"的数据。
    cursor.execute("SELECT * FROM key_analyser WHERE id=?", (id))
    row = cursor.fetchone()
    print(row)

#查询所有数据
def query_all_item():
    global conn, cursor
    print("query_all_item")
    # 查询"key_analyser"表格中的所有数据。
    # SELECT *表示查询所有字段，FROM key_analyser表示从"key_analyser"表格中进行查询。
    cursor.execute("SELECT * FROM key_analyser")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    print("database module test start")
    init_db()
    
    query_all_item()

    add_item(1, 100, 'a', 0, 1000, 1)
    add_item(2, 101, 'b', 0, 1001, 1)
    add_item(3, 102, 'c', 0, 1002, 1)
    add_item(4, 103, 'd', 0, 1003, 1)
    
    query_all_item()