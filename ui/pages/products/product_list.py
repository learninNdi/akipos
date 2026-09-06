from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( 
    QWidget, QVBoxLayout,
    QLineEdit, QLabel,
    QComboBox, QHBoxLayout,
    QHeaderView
)

from PyQt5.QtGui import QBrush

from ui.widgets.make_table import make_table
from ui.widgets.rupiah import rupiah

from services.product_service import ProductService

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
        self.table = None
        self.search_input = None

        self.setup_ui()
        self.setup_connections()

    # ========================================================== 
    # UI 
    # ==========================================================

    def setup_ui(self):
        layout = QVBoxLayout(self)

        search_layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Cari produk atau scan barcode..."
        )

        self.stock_filter = QComboBox()
        self.stock_filter.setObjectName("StockFilter")
        self.stock_filter.addItems([
            "Semua",
            "Tersedia",
            "Tidak Tersedia"
        ])
        self.stock_filter.setCurrentIndex(1)
        self.stock_filter.setFixedWidth(130)

        search_layout.addWidget(
            self.search_input,
            1
        )

        search_layout.addWidget(
            self.stock_filter
        )

        layout.addLayout(search_layout)

        self.table = make_table(
            ["Kode", "Produk", "Harga", "Stok"]
        )

        header = self.table.horizontalHeader()

        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.resizeSection(0, 120)

        header.setSectionResizeMode(2, QHeaderView.Fixed)
        header.resizeSection(2, 100)

        header.setSectionResizeMode(3, QHeaderView.Fixed)
        header.resizeSection(3, 10)

        layout.addWidget(self.table, 1)

        layout.addWidget(
            QLabel(
                "Double-click produk untuk menambahkan.",
                objectName="Muted"
            )
        )

    def setup_connections(self):
        # self.load_products()

        self.search_input.textChanged.connect(
            self.apply_filter
        )

        self.stock_filter.currentIndexChanged.connect(
            self.apply_filter
        )

        self.table.cellDoubleClicked.connect(
            self.on_product_double_clicked
        )

        self.load_products()

    def load_products(self):
        try:
            self.products = ProductService.get_products()
            self.apply_filter()

        except Exception as e:
            print("ERROR LOAD PRODUCTS:", e)

    def display_products(self, products):
        self.table.setRowCount(0)

        for product in products:
            row = self.table.rowCount()
            self.table.insertRow(row)

            self.table.setItem(
                row, 0,
                self.make_item(product["item_id"])
            )

            self.table.setItem(
                row, 1,
                self.make_item(product["item_name"])
            )

            self.table.setItem(
                row, 2,
                self.make_item(
                    f"{rupiah(product['selling_price'])}"
                )
            )

            self.table.setItem(
                row, 3,
                self.make_item(
                    str(product["quantity"])
                )
            )

            if product["quantity"] == 0:
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)

                    if item:
                        item.setBackground(
                            QBrush(Qt.darkGray)
                        )

                        item.setForeground(
                            QBrush(Qt.gray)
                        )

    def make_item(self, value):
        from PyQt5.QtWidgets import QTableWidgetItem

        return QTableWidgetItem(str(value))

    def apply_filter(self):

        search_text = self.search_input.text().strip().lower()

        stock_filter = self.stock_filter.currentIndex()

        filtered_products = []

        for product in self.products:
            item_id = str(product["item_id"]).lower()
            name = str(product["item_name"]).lower()

            if search_text:
                if(
                    search_text not in item_id
                    and
                    search_text not in name
                ):
                    continue

            stock = product["quantity"]

            if stock_filter == 1:
                if stock <= 0:
                    continue
            elif stock_filter == 2:
                if stock != 0:
                    continue

            filtered_products.append(product)

        self.display_products(filtered_products)

    def on_product_double_clicked(self, row, column):

        if row < 0 or row >= self.table.rowCount():
            return

        code = self.table.item(row, 0).text()

        for product in self.products:
            if str(product["item_id"]) == code:
                self.product_selected.emit(product)

                break
    