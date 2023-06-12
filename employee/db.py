import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employee(
           id Integer Primary Key,
           name text,
           age text,
           dob text,
           email text,
           gender text,
           contact text,
           address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()
    # Insert Function
    def insert(self,name,age,dob,email,gender,contact,address):

        self.cur.execute("insert into employee values(NULL,?,?,?,?,?,?,?)",
                         (name,age,dob,email,gender,contact,address))
        self.con.commit()
    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("select * from employee")
        rows=self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a record in db
    def remove(self,id):
        self.cur.execute("delete from employee where id=?",(id,))
        self.con.commit()

    #update a record in db
    def update(self,id,name,age,dob,email,gender,contact,address):
        self.cur.execute("update  employee set name=?,age=?,dob=?,email=?,gender=?,contact=?,address=? where id=?",
                         (name, age, dob, email, gender, contact, address,id))
        self.con.commit()

