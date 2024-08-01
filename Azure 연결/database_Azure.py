import pymysql

# 연결
hostname = 'taehwanfreeserver30.mysql.database.azure.com'
username = 'kimtaehwan'
password = 'wazikm427!@'
db_name = 'myData'

# # SSL
# ssl = {'ssl': {'ca': 'C:/Users/GJ/Desktop/certification'}}

# 데이터베이스에 연결
conn = pymysql.connect(host=hostname, user=username, password=password, database=db_name) # + ssl 필요하면 ssl = ssl
cur = conn.cursor()


def inputData(name ,id, pw, birth, email_f, email_b):
    
    # 테이블이 존재하는지 확인하고 생성
    cur.execute("SHOW TABLES LIKE 'userData'")
    result = cur.fetchall()
    
    if result:
        print('Table exist')
    else:
        cur.execute("CREATE TABLE userData(NAME char(15), ID char(15), PW char(15), BIRTH date, EMAIL char(30))")
    
    email = f'{email_f}@{email_b}'
    
    cur.execute("""
                INSERT INTO 
                userData (NAME, ID, PW, BIRTH, EMAIL) 
                VALUES(%s, %s, %s, %s, %s)
                """ , (name, id, pw, birth, email))
    
    conn.commit()
    
    print('Data Saved')
    conn.close()