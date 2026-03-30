from fastapi import FastAPI
from order_utils import fetch_data_from_database

CONNECTION_STRING = "Your_Connection_String_Here"
QUERY = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS"

app = FastAPI()


def _process_order(order_row: dict) -> dict:
    return {
        "OrderID": order_row["OrderID"],
        "CustomerName": order_row["CustomerName"],
        "OrderDate": str(order_row["OrderDate"]),
    }


@app.get("/orders/first")
def get_first_order() -> dict:
    orders = fetch_data_from_database(CONNECTION_STRING, QUERY)

    if not orders:
        return {"message": "No orders found"}

    return _process_order(orders[0])
