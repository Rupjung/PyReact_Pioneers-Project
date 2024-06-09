import psycopg2


def connect(database, user, password, host, port):
    conn = psycopg2.connect(database=database, 
                        user=user,
                        password=password,
                        host=host,
                        port=port)
    return conn


conn = connect('test', 'postgres', 'Sequel88@#', '127.0.0.1', '5432')


cur = conn.cursor()


def get_student_classroom_rollno(student_name):
    cur.execute(f"SELECT classroom_no, student_rollno FROM student WHERE student_name = '{student_name}'")
    student_rollno, classroom = cur.fetchone()
    print(student_rollno, classroom)
    return student_rollno, classroom

conn.commit()




