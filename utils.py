import time,pymysql

def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")
# 封装两个方法
def get_conn():
    """
    return: 连接，游标
    """
    # 建立连接
    conn = pymysql.connect(host="127.0.0.1",
                          user="root",
                          password="kaer1943",
                          db="cov")
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor

def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
def query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结构，(().().)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_c1_data():
    """
    :return: 返回大屏div id=c1 的数据
    """
    sql = "select sum(confirm)," \
          "(select suspect from history order by ds desc limit 1)," \
          "sum(heal)," \
          "sum(dead)" \
          "from details" \
          "where update_time=(select update_time from details order by update_time desc limit 1)"
    res = query(sql)
    return res[0]

if __name__ == "__main__":
    print(get_c1_data())