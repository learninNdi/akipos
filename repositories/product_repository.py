class ProductRepository:

    def get_all(self):
        query = """
            SELECT
                item_id,
                item_name,
                voltage,
                capacity,
                cca,
                weight,
                dimension,
                minimum_margin,
                selling_price,
                quantity,
                note
            FROM products
            ORDER BY item_name
        """

        # eksekusi query di sini