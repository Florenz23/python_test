# from insertDataFunction import insert_vendor
# from insertDataFunction import insert_vendor_list
from config import config
import psycopg2



def insertData(amount):
    insert_vendor(amount)
    # insert multiple bot_data

def insert_vendor(user_id, follower_amount):
    """ insert a new vendor into the bot_data table """
    sql = """INSERT INTO bot_data(user_id, follower_num)
             VALUES(12,10) RETURNING user_id;"""
    conn = None
    user_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (user_id, follower_amount,))
        # get the generated id back
        user_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return user_id

insert_vendor(12,20)
insert_vendor(12,30)
insert_vendor(12,40)
