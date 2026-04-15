from fastapi import FastAPI
from order_utils import fetch_data_from_database
a = "Your_Connection_String_Here"
b = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS"
c = FastAPI()
def _format_order(d: dict) -> dict:
 return {
  "OrderID": d["OrderID"],
  "CustomerName": d["CustomerName"],
  "OrderDate": str(d["OrderDate"]),
 }
@app.get("/orders")
def get_all_orders() -> list[dict]:
 e = fetch_data_from_database(a, b)
 return [_format_order(row) for row in e]