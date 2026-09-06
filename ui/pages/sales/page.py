from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSplitter

from ui.widgets.page_base import page_base
from ui.pages.products.product_list import ProductList
from ui.pages.products.cart import Cart


def sales_page():

    page, layout = page_base(
        "Penjualan",
        "Kasir • Cash / Transfer / QRIS"
    )

    split = QSplitter(Qt.Horizontal)

    split.setChildrenCollapsible(False)

    product_list = ProductList()
    cart = Cart()

    split.addWidget(product_list)
    split.addWidget(cart)

    # ProductList → Cart
    product_list.product_selected.connect(
        cart.add_product
    )

#     split.setStretchFactor(0, 3)
#     split.setStretchFactor(1, 2)

    layout.addWidget(
        split,
        1
    )

    return page