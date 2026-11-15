"""Regression tests for the supplier order tracker."""

import unittest

import supplier_orders


class SupplierOrdersTests(unittest.TestCase):
    """Check normal workflow and important edge cases."""

    def setUp(self):
        self.connection = supplier_orders.create_connection()

    def tearDown(self):
        self.connection.close()

    def test_order_totals_and_pending_count(self):
        self.assertEqual(
            supplier_orders.place_order(self.connection, "Acme", "rods", 40),
            40,
        )
        self.assertEqual(
            supplier_orders.place_order(self.connection, "Bolt Co", "bolts", 500),
            540,
        )
        self.assertEqual(supplier_orders.pending_count(self.connection), 2)

    def test_received_order_saves_remarks_and_cleanup(self):
        supplier_orders.place_order(self.connection, "Acme", "rods", 40)
        supplier_orders.mark_received(self.connection, 1, "checked")
        row = self.connection.execute(
            "SELECT received, remarks FROM orders WHERE id = ?", (1,)
        ).fetchone()
        self.assertEqual(row, (1, "checked"))
        self.assertEqual(supplier_orders.cleanup(self.connection), 1)

    def test_sql_like_supplier_text_is_stored_as_data(self):
        value = "Acme'); DROP TABLE orders; --"
        supplier_orders.place_order(self.connection, value, "nuts", 2)
        row = self.connection.execute(
            "SELECT supplier FROM orders WHERE id = ?", (1,)
        ).fetchone()
        self.assertEqual(row[0], value)

    def test_non_positive_quantity_is_rejected(self):
        with self.assertRaises(ValueError):
            supplier_orders.place_order(self.connection, "Acme", "rods", 0)

    def test_unknown_order_is_rejected(self):
        with self.assertRaises(ValueError):
            supplier_orders.mark_received(self.connection, 999, "missing")


if __name__ == "__main__":
    unittest.main()
