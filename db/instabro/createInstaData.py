#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE insta_data (
           user_id SERIAL PRIMARY KEY,
            insta_name VARCHAR(255) NOT NULL,
            insta_password VARCHAR(255) NOT NULL,
            insta_hashtag VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE bot_data (
                user_id INTEGER NOT NULL,
                follower_num INTEGER NOT NULL,
                log_date timestamp without time zone DEFAULT now(),
                PRIMARY KEY (user_id),
                FOREIGN KEY (user_id)
                    REFERENCES insta_data (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
