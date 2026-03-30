from fastapi import FastAPI
from order_utils import fetch_data_from_database, process_order_limited

CONNECTION_STRING = "Your_Connection_String_Here"
QUERY = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS"

app = FastAPI()


@app.get("/orders/limited")
def get_limited_orders() -> dict:
    orders = fetch_data_from_database(CONNECTION_STRING, QUERY)

    for index, row in enumerate(orders):
        process_order_limited(row, index)

    return {"processed": len(orders), "note": "Only the first order was fully processed"}
