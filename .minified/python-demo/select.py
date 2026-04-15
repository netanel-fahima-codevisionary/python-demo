from fastapi import FastAPI
from order_utils import fetch_data_from_database
a = "Your_Connection_String_Here"
b = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS"
c = FastAPI()
def _process_order(d: dict) -> dict:
 return {
  "OrderID": d["OrderID"],
  "CustomerName": d["CustomerName"],
  "OrderDate": str(d["OrderDate"]),
 }
@app.get("/orders/first")
def get_first_order() -> dict:
 e = fetch_data_from_database(a, b)
 if not e:
  return {"message": "No orders found"}
 return _process_order(e[0])