from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
     QFrame,
     QSplitter,
     QVBoxLayout,
     QLineEdit,
     QLabel,
     QPushButton
)

from ui.widgets.make_table import make_table
from ui.widgets.page_base import page_base
from ui.pages.products.product_list import ProductList

def sales_page():
    page,l=page_base("Penjualan","Kasir • Cash / Transfer / QRIS")
    split=QSplitter(Qt.Horizontal); split.setChildrenCollapsible(False)

    left = ProductList()
    split.addWidget(left)

    right=QFrame(); right.setObjectName("Panel"); rl=QVBoxLayout(right)
    rl.addWidget(QLabel("Keranjang",objectName="PanelTitle"))
    rl.addWidget(make_table(["Produk","Qty","Harga","Total"]),1)
    rl.addWidget(QLineEdit(placeholderText="Pelanggan (opsional)"))
    rl.addWidget(QLineEdit(placeholderText="No. polisi / kendaraan (opsional)"))
    rl.addWidget(QLabel("TOTAL",objectName="Muted"))
    total=QLabel("Rp 0"); total.setAlignment(Qt.AlignRight)
    total.setStyleSheet("font-size:25px;font-weight:700;")
    rl.addWidget(total)
    pay=QPushButton("BAYAR  F4"); pay.setObjectName("Primary"); pay.setMinimumHeight(44)
    rl.addWidget(pay)
    split.addWidget(right)
    split.setStretchFactor(0,3); split.setStretchFactor(1,2)
    l.addWidget(split,1)
    return page