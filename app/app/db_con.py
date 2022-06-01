"""
    db_con.py - dbConnection class:
    connection params from database.ini file
"""

import psycopg2
from psycopg2 import connect
from psycopg2.extras import DictConnection
from configparser import ConfigParser

class dbConnection:
    
    # reading connection params
    def __init__(self, filename='app/database.ini', section='postgresql'):
        self.parser = ConfigParser() 
        self.parser.read(filename)   
        self.db = {}   
    
        if self.parser.has_section(section):
            self.params = self.parser.items(section)
            for param in self.params:
                self.db[param[0]] = param[1]
        else:
            raise Exception(f"Section {section} can\'t be found in {filename} file.")
    
    # connection to my database
    def connect(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(host = self.db['host'], 
                                        database = self.db['database'], 
                                        user = self.db['user'], 
                                        password = self.db['password'],
                                        port = self.db['port']
                                        )
        except (Exception, psycopg2.DatabaseError) as err: 
            print(f"Database connection error:  {err}")
    
    # version of database
    def db_version(self):
        try:
            self.connect()
            self.cur = self.conn.cursor()                    
            self.cur.execute('SELECT version()')    
            self.db_v = self.cur.fetchone()         
            print(f"Database version: \n \t {self.db_v}")
            self.close()
        except (Exception, psycopg2.DatabaseError) as err: 
            print(f"Database connection error: {err}")
        finally:
            self.close()
    
    # closing the connection
    def close(self):
        if self.conn and not self.conn.closed:
            self.conn.close()
        self.conn = None

    # commiting query
    def commit(self):
        self.conn.commit()

    # rollbacking query
    def rollback(self):
        self.conn.rollback()

    # executing queries drop, create, insert,...
    def execute(self, query, args=None):
        if self.conn is None or self.conn.closed:
            self.connect()
        curs = self.conn.cursor()
        try:
            curs.execute(query, args)
        except Exception as ex:
            self.conn.rollback()
            curs.close()
            raise ex
        return curs   

    # executing query COUNT, SUM, MIN, ...
    def fetchone(self, query, args=None):
        curs = self.execute(query, args)
        row = curs.fetchone()
        curs.close()
        return row

    # executing query returning more rows than one
    def fetchall(self, query, args=None):
        curs = self.execute(query, args)
        rows = curs.fetchall()
        curs.close()
        return rows

    # copying records of the table to the file 
    def copy_to(self, path_file, table_name, sep=','):
        if self.conn is None or self.conn.closed:
            self.connect()
        with open(path_file, 'w+') as f:
            curs = self.conn.cursor()
            try:
                curs.copy_to(f, table_name, sep)
            except:
                curs.close()
                raise Exception(f"Problem with writing to the file {path_file}")
            
    # copying records from the file to the table
    def copy_from(self, path_file, table_name, sep=','):
        if self.conn is None or self.conn.closed:
            self.connect()
        with open(path_file, 'r') as f:
            curs = self.conn.cursor()
            try:
                curs.copy_from(f, table_name, sep)
            except:
                curs.close()
                raise Exception(f"Problem copying from {path_file} to {table_name}")

# m = dbConnection()
# print(m.db_version())
# #m.execute("INSERT INTO users (user_id, name) VALUES (105,'fux')")
# #m.execute("INSERT INTO users (user_id, name) VALUES (106,'fux')")
# print(m.fetchall("SELECT user_id, name FROM users where name='fux'"))
