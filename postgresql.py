'''from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *'''

import psycopg2

conn = psycopg2.connect(database='db395cakuikd2s',
                        user='yoxejfdazwyghe',
                        password='b35aaaceaf6c2c2bb47b3054e364fefec42fb8be687364e35e6b58a2260da715',
                        host='ec2-52-202-198-60.compute-1.amazonaws.com',
                        port='5432')
cur = conn.cursor()

cur.execute('SELECT VERSION()')
results=cur.fetchall()
print ("Database version : %s " % results)

class postgre:
    def __init__(self):
        """
        params:
            conn: Set credentials for manual connections to a specific database.
            cur: cursor
        description:
            connects to database
        """
        self.conn =  psycopg2.connect(database='db395cakuikd2s',
                                      user='yoxejfdazwyghe',
                                      password='b35aaaceaf6c2c2bb47b3054e364fefec42fb8be687364e35e6b58a2260da715',
                                      host='ec2-52-202-198-60.compute-1.amazonaws.com',
                                      port='5432')
        self.cur = self.conn.cursor()

        # Initialization completed-- print version
        self.cur.execute('SELECT VERSION()')
        results=self.cur.fetchall()
        print ("Database version : %s " % results)

    # Identify a new user
    def new_user(self, userid):
        self.cur.execute("SELECT userid FROM profile")
        rows = self.cur.fetchall()
        for row in rows:
            if userid==row[0]:
                return 0
        return 1
    
    # Fill in user information
    def user_registration(self, userid, status, university, department, studentid, year_of_enrollment, name, student_id_card, line_id):
        self.cur.execute("INSERT INTO profile(userid, status, university, department, studentid, year_of_enrollment, name, student_id_card, line_id) VALUES (%s, %s, %s, %s, %s, %d, %s, %s, %s)", 
                        (userid, status, university, department, studentid, year_of_enrollment, name, student_id_card, line_id))
        self.conn.commit()
    
    def setQuestions(self):
        pass

    def getQuestions(self):
        return 0