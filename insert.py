

# DB 연결 가져오기
if __name__ == '__main__':
    db_manager = db.DatabaseManager()
    conn = db_manager.get_conn()
    conn.set_client_encoding('UTF8')
    cur = conn.cursor()
    cur.execute('SELECT * FROM maltipoo.request_info;')
    result = cur.fetchall()
    print(result)
    cur.close()
    # 연결 반환
    db_manager.put_conn(conn)
