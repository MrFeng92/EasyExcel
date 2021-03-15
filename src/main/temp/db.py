import pymysql

"""
常用模块读写MySQL数据库
"""
import json

# dumps可以格式化所有的基本数据类型为字符串
data1 = json.dumps([])         # 列表
print(data1, type(data1))
data2 = json.dumps(2)          # 数字
print(data2, type(data2))
data3 = json.dumps('3')        # 字符串
print(data3, type(data3))
dict = {"name": "Tom", "age": 23}   # 字典
data4 = json.dumps(dict)
print(data4, type(data4))

with open("test.json", "w", encoding='utf-8') as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
    f.write(json.dumps(dict, indent=4))
    json.dump(dict, f, indent=4)  # 传入文件描述符，和dumps一样的结果


def get_conn():
    """
    获取MySQL链接
    :return:
    """
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='test',
        charset='utf8'
    )


def query_data(sql):
    """
    根据SQL查询数据并返回
    :param sql: SQL语句
    :return: list[dict] 字典集合
    """
    conn = get_conn()
    try:
        # DictCursor 每行数据以字典形式返回
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)

        # fetchall 返回整个列表数据
        return cursor.fetchall()
    finally:
        conn.close()


def insert_or_update_data(sql):
    """
    执行新增或更新的sql
    :param sql:
    :return: 不反回内容
    """
    conn = get_conn()
    try:
        cursor=conn.cursor()
        cursor.execute(sql)
#         主意这里，只有commit才可以生效
        conn.commit()
    finally:
        conn.close()
