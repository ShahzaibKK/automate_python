import openpyxl, mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="PAKistan1122", database="tiles_bannu"
)

cursor = db.cursor()
sql = "SELECT * FROM tiles_bannu.inv_inventory_pro;"
cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)
cursor.close()
db.close()
