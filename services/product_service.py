from repositories.product_repository import ProductRepository

class ProductService:

    @staticmethod
    def get_new_products():
        products = ProductRepository.get_new_products()

        return products

    @staticmethod
    def search_new_products(keyword):
        keyword = keyword.strip()

        if not keyword:
            return ProductRepository.get_new_products()

        return ProductRepository.search(keyword)

    @staticmethod
    def get_new_product(product_id):
        if not product_id:
            return None

        return ProductRepository.get_new_product_by_id(product_id)

    @staticmethod
    def has_stock(product, quantity=1):
        if not product:
            return False

        if quantity <= 0:
            return False

        stock = product.get("stock", 0)

    @staticmethod
    def validate_sale(product, quantity):
        if not product:
            return False, "Produk tidak ditemukan."

        if quantity <= 0:
            return False, "Jumlah produk harus lebih dari 0."

        stock = product.get("stock", 0)

        if stock <= 0:
            return False, "Stok produk habis."

        if quantity > stock:
            return(
                False,
                f"Stok tidak cukup. Stok tersedia: {stock}"
            )

        return True, None

    @staticmethod
    def get_used_products():

        return ProductRepository.get_used_products()    
    