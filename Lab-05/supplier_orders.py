"""Track supplier purchase orders and warehouse receipt status."""

import logging
import sqlite3

LOGGER = logging.getLogger(__name__)


def create_connection() -> sqlite3.Connection:
    """Create and initialize the in-memory supplier orders database."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            supplier TEXT NOT NULL,
            item TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            received INTEGER NOT NULL DEFAULT 0,
            remarks TEXT
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE order_summary (
            total_quantity INTEGER NOT NULL
        )
        """
    )
    connection.execute(
        "INSERT INTO order_summary (total_quantity) VALUES (?)",
        (0,),
    )
    return connection


def place_order(
    connection: sqlite3.Connection,
    supplier: str,
    item: str,
    quantity: int,
) -> int:
    """Create an order and return the cumulative quantity ordered."""
    if quantity <= 0:
        raise ValueError("Order quantity must be greater than zero.")

    with connection:
        connection.execute(
            """
            INSERT INTO orders (supplier, item, quantity, received)
            VALUES (?, ?, ?, 0)
            """,
            (supplier, item, quantity),
        )
        connection.execute(
            "UPDATE order_summary SET total_quantity = total_quantity + ?",
            (quantity,),
        )
        total_row = connection.execute(
            "SELECT total_quantity FROM order_summary"
        ).fetchone()

    return int(total_row[0])


def mark_received(
    connection: sqlite3.Connection,
    order_id: int,
    remarks: str,
) -> None:
    """Mark an order as received and store the supplied remarks."""
    with connection:
        cursor = connection.execute(
            """
            UPDATE orders
            SET received = 1, remarks = ?
            WHERE id = ?
            """,
            (remarks, order_id),
        )

    if cursor.rowcount == 0:
        raise ValueError(f"No order exists with ID {order_id}.")


def notify_warehouse(supplier: str) -> None:
    """Log a warehouse notification without invoking a shell command."""
    LOGGER.info("Notifying warehouse about supplier: %s", supplier)


def cleanup(connection: sqlite3.Connection) -> int:
    """Delete received orders and return the number of rows removed."""
    with connection:
        cursor = connection.execute(
            "DELETE FROM orders WHERE received = 1"
        )
    return cursor.rowcount


def pending_count(connection: sqlite3.Connection) -> int:
    """Return the number of orders that have not yet been received."""
    result = connection.execute(
        "SELECT COUNT(*) FROM orders WHERE received = 0"
    ).fetchone()
    return int(result[0])


def main() -> None:
    """Run a small demonstration of the supplier order workflow."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    connection = create_connection()
    try:
        place_order(connection, "Acme Steel", "rods", 40)
        total_quantity = place_order(connection, "Bolt Co", "bolts", 500)
        mark_received(connection, 1, "ok")
        notify_warehouse("Acme")
        print(pending_count(connection), total_quantity)
        cleanup(connection)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
