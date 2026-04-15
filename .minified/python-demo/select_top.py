from fastapi import FastAPI
from order_utils import fetch_data_from_database
a = "Your_Connection_String_Here"
b = FastAPI()
def _format_order(c: dict) -> dict:
 return {
  "OrderID": c["OrderID"],
  "CustomerName": c["CustomerName"],
  "OrderDate": str(c["OrderDate"]),
 }
@app.get("/orders/top")
def get_top_order() -> dict:
 d = fetch_data_from_database(a, "SELECT OrderID, CustomerName, OrderDate FROM ORDERS")
 if not d:
  return {"message": "No orders found"}
 return _format_order(d[0])