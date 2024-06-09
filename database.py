import psycopg2
import creating_tables as c
import searching_details as s


def connect(database, user, password, host, port):
    conn = psycopg2.connect(database=database, 
                        user=user,
                        password=password,
                        host=host,
                        port=port)
    return conn


conn = connect('test', 'postgres', 'Sequel88@#', '127.0.0.1', '5432')

cur = conn.cursor()



c.creating_student_table(cur)
c.creating_attendance_table(cur)

def registering_attendance(student_rollno, classroom_no, date, time, status):
    cur.execute(f"INSERT INTO attendance(student_rollno, classroom_no, date, time, status) VALUES('{student_rollno}', '{classroom_no}', '{date}', '{time}', '{status}')")
    conn.commit()

