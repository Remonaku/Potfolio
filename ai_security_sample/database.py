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

##########################################################################################################################

def createTable():
    
    # 테이블이 존재하는지 확인하고 생성
    cur.execute("SHOW TABLES LIKE 'userData'")
    result = cur.fetchall()
    
    if result:
        print('Table exist')
    else:
        cur.execute("""
                    CREATE TABLE userData(
                        NAME char(15), 
                        ID char(15) PRIMARY KEY, 
                        PW char(15),
                        EMAIL char(30)
                    )
                    """)
    conn.commit()
    print('Table created')
    
##########################################################################################################################

##########################################################################################################################

def createData(name ,id, pw, email):
    
    # ID가 존재하는지 확인하고 생성
    cur.execute("SELECT ID FROM userData WHERE ID = %s", (id))
    result = cur.fetchone()
    
    if result:
        print('ID already exist')
        
    else:
        cur.execute("""
                    INSERT INTO userData (NAME, ID, PW, EMAIL) 
                    VALUES(%s, %s, %s, %s)
                    """ , (name, id, pw, email))

        conn.commit() 
        print('Data created')

##########################################################################################################################

##########################################################################################################################

def selectId(id):
    cur.execute("SELECT ID FROM userData WHERE ID = %s", (id))
    result = cur.fetchone()
    print('Found ID')
    return result[0]
        
##########################################################################################################################

##########################################################################################################################

def selectPw(id, pw):
    cur.execute("SELECT PW FROM userData WHERE ID = %s AND PW = %s", (id, pw))
    result = cur.fetchone()
    print('Found Password')
    return result[0]
        
##########################################################################################################################