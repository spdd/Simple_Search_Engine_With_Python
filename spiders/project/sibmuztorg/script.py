import MySQLdb
mydb = MySQLdb.connect(host = 'localhost',
		    user = 'root',
		    passwd = 'mysql',
		    db = 'irkdb')
cur = mydb.cursor()
delete1 = "DELETE FROM search_goods WHERE id BETWEEN 830001 AND 840000"
cur.execute(delete1)