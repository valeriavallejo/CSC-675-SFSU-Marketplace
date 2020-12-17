import mysql.connector
from mysql.connector import Error
from passlib.hash import sha256_crypt

def hash_password(user_id, password):
    hashed_password = sha256_crypt.hash(password)

    query = "UPDATE User " \
            "SET user_pass = %s " \
            "WHERE user_id  = %s"

    args = (hashed_password, user_id)

    try:
        conn =  mysql.connector.connect(host='trademart.c9x2rihy8ycd.us-west-1.rds.amazonaws.com',
                database='Trademart',
                user='root',
                password='trademartadmin')
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)


    return hashed_password

def verify_password(entered_password, hashed_password):
    return sha256_crypt.verify(entered_password, hashed_password)

def main():
    h = hash_password(224602238, "password")
    result = verify_password("password", h)
    print(result)

if __name__ == '__main__':
    main()
