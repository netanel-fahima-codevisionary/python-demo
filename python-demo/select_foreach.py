from fastapi import FastAPI
from order_utils import fetch_data_from_database

CONNECTION_STRING = "Your_Connection_String_Here"
QUERY = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS"

app = FastAPI()


def _format_order(order_row: dict) -> dict:
    return {
        "OrderID": order_row["OrderID"],
        "CustomerName": order_row["CustomerName"],
        "OrderDate": str(order_row["OrderDate"]),
    }


@app.get("/orders")
def get_all_orders() -> list[dict]:
    orders = fetch_data_from_database(CONNECTION_STRING, QUERY)

    return [_format_order(row) for row in orders]
