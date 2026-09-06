from database.connection import get_connection

class ProductRepository:

    @staticmethod
    def get_all():
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT
                    item_id,
                    item_name,
                    selling_price,
                    quantity
                FROM products
                ORDER BY item_name ASC;
            """)

            return cursor.fetchall()

        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()

    @staticmethod
    def search(keyword):
        conn = None
        cursor = None

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            keyword = f"%{keyword}%"

            cursor.execute("""
                SELECT
                    item_id,
                    item_name,
                    selling_price,
                    quantity
                FROM products
                WHERE item_id LIKE %s
                OR item_name LIKE %s
                ORDER BY item_name ASC;
            """, (keyword, keyword))

            return cursor.fetchall()

        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()

    @staticmethod
    def get_product_by_id(product_id):
        conn = None
        cursor = None

        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT
                    item_id,
                    item_name,
                    selling_price,
                    quantity
                FROM products
                WHERE item_id = %s;
            """, (product_id,))

            return cursor.fetchone()

        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()
