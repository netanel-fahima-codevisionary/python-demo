from order_utils import fetch_data_from_database, process_order_limited

CONNECTION_STRING = "Your_Connection_String_Here"
QUERY = "SELECT OrderID, CustomerName, OrderDate FROM ORDERS"


def main() -> None:
    orders = fetch_data_from_database(CONNECTION_STRING, QUERY)

    for index, row in enumerate(orders):
        process_order_limited(row, index)


if __name__ == "__main__":
    main()
