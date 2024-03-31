import mysql.connector as m

con=m.connect(host="localhost",user="root",password="",database="student")

cur=con.cursor()
'''
#cur.execute("create table info (rollno int, stud_name varchar(40), marks int )")

#cur.execute("show tables")

for db in cur:
    print(db)


sql="insert into info (rollno, stud_name,marks)values (%s,%s,%s)"
val=[("17","sdgfdg","89"),
     ("19","ghh","56"),
     ("1","fghjyt","98"),
     ("6","fghjhjuk","59")
     ]
cur.executemany(sql,val)
con.commit()

cur.execute("select rollno, stud_name from info where marks > 60 order by rollno")
rows=cur.fetchall()
print(rows)

for row in rows:
    print()
    for val in row:
        print(val,end=" ")



cur.execute("update info set stud_name=(%s) where rollno=%s",("xys",1))
con.commit()

'''
cur.execute("delete from info where rollno=17")
con.commit()

