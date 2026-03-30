from fastapi import FastAPI
from order_utils import fetch_data_from_database

CONNECTION_STRING = "Your_Connection_String_Here"
QUERY = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS LIMIT 1"

app = FastAPI()


def _format_order(order_row: dict) -> dict:
    return {
        "OrderID": order_row["OrderID"],
        "CustomerName": order_row["CustomerName"],
        "OrderDate": str(order_row["OrderDate"]),
    }


@app.get("/orders/top")
def get_top_order() -> dict:
    orders = fetch_data_from_database(CONNECTION_STRING, QUERY)

    if not orders:
        return {"message": "No orders found"}

    return _format_order(orders[0])
