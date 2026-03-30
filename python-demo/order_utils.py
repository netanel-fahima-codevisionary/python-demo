import pyodbc


def process_order_limited(order_row: dict, index: int) -> None:
    # processes only the first row
    if index > 0:
        return

    order_id = order_row["OrderID"]
    customer_name = order_row["CustomerName"]
    order_date = order_row["OrderDate"]

    print(f"Processing Order: ID={order_id}, Customer={customer_name}, Date={order_date}")


def fetch_data_from_database(connection_string: str, query: str) -> list[dict]:
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)

    columns = [column[0] for column in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return rows
