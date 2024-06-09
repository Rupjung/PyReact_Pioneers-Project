import psycopg2


def creating_student_table(cur):
    cur.execute('''
    CREATE TABLE  IF NOT EXISTS student(
                student_rollno INT PRIMARY KEY,
                classroom_no INT NOT NULL,
                student_name VARCHAR(50) NOT NULL
    );
    ''')

def creating_attendance_table(cur):
    cur.execute('''
    CREATE TABLE  IF NOT EXISTS attendance(
                student_rollno INT NOT NULL,
                classroom_no INT NOT NULL,
                date DATE NOT NULL,
                time TIME,
                status VARCHAR(10) DEFAULT 'Absent' NOT NULL,
                CHECK (status IN ('Present','Absent')),
                FOREIGN KEY(student_rollno) REFERENCES student(student_rollno)
    );
    ''')



print('Tables are created successfully....')


