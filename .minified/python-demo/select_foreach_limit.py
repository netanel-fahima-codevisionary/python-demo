from fastapi import FastAPI
from order_utils import fetch_data_from_database, process_order_limited
a = "Your_Connection_String_Here"
b = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS"
c = FastAPI()
@app.get("/orders/limited")
def get_limited_orders() -> dict:
 d = fetch_data_from_database(a, b)
 for e, f in enumerate(d):
  process_order_limited(f, e)
 return {"processed": len(d), "note": "Only the first order was fully processed"}