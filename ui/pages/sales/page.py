from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QSplitter, QVBoxLayout, QWidget

from ui.pages.products.product_list import ProductList
from ui.pages.products.cart import Cart
from ui.pages.checkout.page import CheckoutDialog

class SalesPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent_window = parent
        self.current_theme = getattr(
            parent,
            "current_theme",
            "dark"
        )

        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            20, 20, 20, 20
        )

        layout.setSpacing(15)

        self.splitter = QSplitter(
            Qt.Horizontal
        )

        self.splitter.setChildrenCollapsible(
            False
        )

        self.product_list = ProductList()
        self.cart = Cart()

        self.splitter.addWidget(
            self.product_list
        )

        self.splitter.addWidget(
            self.cart
        )

        self.splitter.setStretchFactor(0, 3)
        self.splitter.setStretchFactor(1, 2)

        layout.addWidget(
            self.splitter,
            1
        )

    def setup_connections(self):

        self.product_list.product_selected.connect(
            self.cart.add_product
        )

        self.cart.checkout_requested.connect(
            self.handle_checkout
        )

    def handle_checkout(self, data):

        dialog = CheckoutDialog(
            data,
            parent=self,
            theme=self.current_theme
        )

        if dialog.exec_() != QDialog.Accepted:
            return

        payment_data = (
            dialog.get_payment_data()
        )

        try:
            print(payment_data)

            self.cart.clear()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Checkout Gagal",
                f"Transaksi gagal diproses:\n{e}"
            )

    def set_theme(self, theme):

        self.current_theme = theme