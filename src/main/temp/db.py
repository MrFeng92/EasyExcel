import pymysql

"""
常用模块读写MySQL数据库
"""


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
