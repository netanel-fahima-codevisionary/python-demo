import pyodbc
def process_order_limited(a: dict, b: int) -> None:
 # processes only the first row
 if b > 0:
  return
 c = a["OrderID"]
 d = a["CustomerName"]
 e = a["OrderDate"]
 print(f"Processing Order: ID={c}, Customer={d}, Date={e}")
def fetch_data_from_database(f: str, g: str) -> list[dict]:
 h = pyodbc.connect(f)
 i = connection.cursor()
 cursor.execute(g)
 j = [column[0] for column in cursor.description]
 k = [dict(zip(j, row)) for row in cursor.fetchall()]
 cursor.close()
 connection.close()
 return k