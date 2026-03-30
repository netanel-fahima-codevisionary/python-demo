from order_utils import fetch_data_from_database

CONNECTION_STRING = "Your_Connection_String_Here"
QUERY = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS"


def process_order(order_row: dict) -> None:
    order_id = order_row["OrderID"]
    customer_name = order_row["CustomerName"]
    order_date = order_row["OrderDate"]

    print(f"Processing Order: ID={order_id}, Customer={customer_name}, Date={order_date}")


def main() -> None:
    orders = fetch_data_from_database(CONNECTION_STRING, QUERY)

    for row in orders:
        process_order(row)


if __name__ == "__main__":
    main()
