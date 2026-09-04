from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import ( 
    QWidget, QVBoxLayout, QFrame, 
    QLineEdit, QLabel
)

from ui.widgets.make_table import make_table

class ProductList(QWidget):
    """ Widget untuk menampilkan daftar produk 
    pada halaman Sales. 
    Tanggung jawab: 
    - Menampilkan daftar produk 
    - Search produk - Memilih produk 
    - Mengirim produk yang dipilih ke SalesPage 
    Tidak melakukan query database secara langsung. 
    """
    product_selected = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.products = []

        self.setup_ui()
        # self.setup_connections()

    # ========================================================== 
    # UI 
    # ==========================================================

    def setup_ui(self):
        left=QFrame(); left.setObjectName("Panel"); ll=QVBoxLayout(left)
        ll.addWidget(QLineEdit(placeholderText="Cari produk atau scan barcode..."))
        ll.addWidget(make_table(["Kode","Produk","Harga","Stok"],[
            ("A001","GS Astra NS40","850.000","8"),
            ("A002","GS Astra N50","1.050.000","3"),
            ("Y001","Yuasa N70","1.250.000","7"),
            ("I001","Incoe NS60","950.000","4"),
            ("B001","Bosch N50","1.100.000","6"),
        ]),1)
        ll.addWidget(QLabel("Double-click produk untuk menambahkan.",objectName="Muted"))