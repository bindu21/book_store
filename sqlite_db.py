import sqlite3
def create_table():
	conn=sqlite3.connect("myfirstdb.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS mytable(item TEXT,quantity INTEGER,price REAL)")
	conn.commit()
	conn.close()

create_table()

def insert_item(item,quantity,price):
	conn=sqlite3.connect("myfirstdb.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO mytable VALUES(?,?,?)",(item,quantity,price))
	conn.commit()
	conn.close()

insert_item("Glass",6,15)
insert_item("Flower Pot",1,4)
insert_item("Mop",2,12)
insert_item("Jar",2,10)

def view_item():
	conn=sqlite3.connect("myfirstdb.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM mytable")
	rows=cur.fetchall()
	conn.close()
	return rows

print(view_item())

def delete_item(item):
	conn=sqlite3.connect("myfirstdb.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM mytable WHERE item=?",(item,))
	conn.commit()
	conn.close()
	
print("After deletion\n")
delete_item("Mop")
print(view_item())

def update_value(item,quan,price):
	conn=sqlite3.connect("myfirstdb.db")
	cur=conn.cursor()
	cur.execute("UPDATE mytable SET quantity=?,price=? where item=?",(quan,price,item))
	conn.commit()
	conn.close()

update_value("Glass",10,20)
print(view_item())