import pymysql

def getData():
    conn = pymysql.connect(host='localhost', user='root', password='1234', db="practice", charset="utf8")
    cur = conn.cursor()

    # 예외사항이 생겨서 에러가 생길 경우도 있기 때문에, 그것도 고려해야한다.
    try:
        cur.execute("SELECT * FROM userTable WHERE NAME='홍지윤'")
        result = cur.fetchone()

        if result:
            user_id = result[0]
            user_name = result[1]
            user_email = result[2]
            user_birth = result[3]
            return user_id, user_name, user_email, user_birth
        
        else:
            return None, None, None, None
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        conn.close()

