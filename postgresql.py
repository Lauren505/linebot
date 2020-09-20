import psycopg2

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
    def new_user(self, lineid):
        self.cur.execute("SELECT line_id FROM profile")
        rows = self.cur.fetchall()
        for row in rows:
            if lineid==row[0]:
                return 0
        return 1
    
    # Fill in user information(undone)
    def user_registration(self, userid, status, university, department, studentid, year_of_enrollment, name, student_id_card, lineid):
        self.cur.execute("INSERT INTO profile(userid, status, university, department, studentid, year_of_enrollment, name, student_id_card, line_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                        (userid, status, university, department, studentid, year_of_enrollment, name, student_id_card, lineid))
        self.conn.commit()
    
    # Set user status
    def setUserStatus(self, userid, status):
        status = str(status)
        self.cur.execute("""
                        UPDATE profile 
                        SET status = %s
                        WHERE userid = %s
                        """, (status, userid))
        self.conn.commit()

    '''
    question_list = [
            # |題號|            header                |           圖片url                 |                  body中的文字
            [1005, ['交換電路與邏輯設計', '課本', '7.1'], 'https://i.imgur.com/8Mjhu0Y.png',
                ['第一段我有點不懂', '第二段我也不太懂', '第三段我也不會，我是不是太笨了QQ？']],
            [1006, ['計算機概論', '作業',  '1'],
                'https://i.imgur.com/FwVstGx.png', ['這次作業好難喔', '我都不會寫']],
            [1007, ['微積分 ', '考古題', '108.1'],
                'https://i.imgur.com/x3Sftiv.png', ['吉鈞救救我']]
    ]
    '''

    # Set questions(undone)
    def setQuestion(self, question_id, asker_id, question_image, question_text, status, subject, source, number):
        self.cur.execute("INSERT INTO questions(question_id, asker_id, question_image, question_text, status, subject, source, number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (question_id, asker_id, question_image, question_text, status, subject, source, number))
        self.conn.commit()

    # Functions for data retrieval...
    def getQuestionList(self):
        question_list = []
        self.cur.execute("SELECT * FROM questions")
        rows = self.cur.fetchall()
        for row in rows:
            header = [row[5], row[6], row[7]]
            body = [row[3]]
            question_list.append([row[0], header, row[2], body])
        print(question_list)
        return question_list

    def getQuestionListBySubject(self, subject):
        question_list = []
        self.cur.execute("SELECT * FROM questions WHERE subject=%s", (subject, ))
        rows = self.cur.fetchall()
        for row in rows:
            header = [row[5], row[6], row[7]]
            body = [row[3]]
            question_list.append([row[0], header, row[2], body])
        print(question_list)
        return question_list

    def getQuestionListByAsker(self, askerid):
        question_list = []
        self.cur.execute("SELECT * FROM questions WHERE asker_id=%s", (askerid, ))
        rows = self.cur.fetchall()
        for row in rows:
            header = [row[5], row[6], row[7]]
            body = [row[3]]
            question_list.append([row[0], header, row[2], body])
        print(question_list)
        return question_list
 
    '''
    answer_id, solver_id, question_id, answer, ratings
    '''

    # Set answers(undone: id)
    def setAnswer(self, answer_id, solver_id, question_id, answer):
        self.cur.execute("INSERT INTO answers(answer_id, solver_id, question_id, answer) VALUES (%s, %s, %s, %s)",
                        (answer_id, solver_id, question_id, answer))
        self.conn.commit()

    # Set ratings
    def setRatings(self, answer_id, ratings):
        self.cur.execute("""
                         UPDATE answers
                         SET ratings = %s
                         WHERE answer_id = %s
                         """, (ratings, answer_id))
        self.conn.commit()

    # Functions for data retrieval...
    def getAnswerList(self):
        answer_list = []
        self.cur.execute("SELECT * FROM answers")
        rows = self.cur.fetchall()
        for row in rows:
            answer_list.append([row])
        print(answer_list)
        return answer_list

    def getAnswerListByQuestion(self, question_id):
        answer_list = []
        self.cur.execute("SELECT answer FROM answers WHERE question_id=%s", (question_id, ))
        rows = self.cur.fetchall()
        for row in rows:
            answer_list.append([row])
        print(answer_list)
        return answer_list

    def getAnswerListBySolver(self, solver_id):
        answer_list = []
        self.cur.execute("SELECT answer FROM answers WHERE solver_id=%s", (solver_id, ))
        rows = self.cur.fetchall()
        for row in rows:
            answer_list.append([row])
        print(answer_list)
        return answer_list