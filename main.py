import mysql.connector as connector

class DBhelper:
    def __init__(self):
        self.con=connector.connect(host = 'localhost', port = '3306', user = 'root', password = 'Enter Your Password', database= 'test_mysql', auth_plugin='mysql_native_password',consume_results=True)

        query = 'select * from crud'
        cur = self.con.cursor()
        cur.execute(query)
        print("Connected..!!")

# Insert data

    def insert_user(self,name,phone,password):
        query = "insert into crud (name,phone,password) Values('{}','{}','{}')".format(name,phone,password)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data Inserted..")

    def fetch_all(self):
        query = "select * from crud"
        cur= self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("id: ",row[0])
            print("Name: ",row[1])
            print("Phone: ",row[2])
            print("Password: ",row[3])

    def fetch_one(self,id):
        query = "select * from crud where id={}".format(id)
        cur= self.con.cursor()
        cur.execute(query)
        id = id
        for id in cur:
            print("id: ",id[0])
            print("Name: ",id[1])
            print("Phone: ",id [2])
            print("Password: ",id[3])

    def delete_user(self, id):
        query = "delete from crud where id={}".format(id)
        print(query)
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data Deleted...")

    def update_user(self, id, newname, newphone, newpassword):
        query = "update crud set name='{}', phone='{}', password='{}' where id={}".format(newname,newphone,newpassword,id)
        print(query)
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data Updated...")

# main code
helper = DBhelper()
# helper.insert_user("pm","147852","123456")
# helper.fetch_all()
helper.fetch_one(2)
# helper.delete_user(3)
# helper.update_user(2,"pm","98989898","123456")

