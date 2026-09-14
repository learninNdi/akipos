from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QComboBox,
    QHeaderView,
    QWidget,
)

from ui.widgets.rupiah import rupiah
from services.product_service import ProductService

class Cart(QFrame):

    total_changed = pyqtSignal(float)
    checkout_requested = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.setObjectName("Panel")

        self.items = []
        self.used_products = []

        self.setup_ui()
        self.setup_connections()

        self.load_used_batteries()

        self.create_used_battery_row()

        # Default
        self.on_transaction_type_changed(0)

    # ==========================================================
    # UI
    # ==========================================================

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            15, 15, 15, 15
        )

        layout.setSpacing(10)

        # ======================================================
        # TITLE
        # ======================================================

        layout.addWidget(
            QLabel(
                "Keranjang",
                objectName="PanelTitle"
            )
        )

        # ======================================================
        # TRANSACTION TYPE
        # ======================================================

        transaction_layout = QHBoxLayout()

        transaction_layout.addWidget(
            QLabel(
                "Jenis Transaksi"
            )
        )

        self.transaction_type = QComboBox()
        self.transaction_type.setObjectName("ComboBoxFilter")

        self.transaction_type.addItems([
            "Penjualan Biasa",
            "Tukar Tambah Aki",
            "Beli Aki Bekas",
        ])

        transaction_layout.addWidget(
            self.transaction_type,
            1
        )

        layout.addLayout(
            transaction_layout
        )

        # ======================================================
        # CART TABLE
        # ======================================================

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Produk",
            "Qty",
            "Harga",
            "Total",
            ""
        ])

        self.table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        self.table.setSelectionMode(
            QTableWidget.SingleSelection
        )

        self.table.verticalHeader().setVisible(
            False
        )

        header = self.table.horizontalHeader()

        # Produk
        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )

        # Qty
        header.setSectionResizeMode(
            1,
            QHeaderView.Fixed
        )
        header.resizeSection(
            1,
            55
        )

        # Harga
        header.setSectionResizeMode(
            2,
            QHeaderView.Fixed
        )
        header.resizeSection(
            2,
            110
        )

        # Total
        header.setSectionResizeMode(
            3,
            QHeaderView.Fixed
        )
        header.resizeSection(
            3,
            120
        )

        # Hapus
        header.setSectionResizeMode(
            4,
            QHeaderView.Fixed
        )
        header.resizeSection(
            4,
            40
        )

        layout.addWidget(
            self.table,
            1
        )

        # ======================================================
        # TRADE IN / BUY USED
        # ======================================================

        self.used_battery_frame = QFrame()

        self.used_battery_frame.setObjectName(
            "TradeInPanel"
        )

        used_layout = QVBoxLayout(
            self.used_battery_frame
        )

        used_layout.setContentsMargins(
            0, 0, 0, 0
        )

        used_layout.setSpacing(7)

        # Label
        self.used_battery_title = QLabel(
            "Aki Bekas"
        )

        self.used_battery_title.setObjectName(
            "PanelTitle"
        )

        used_layout.addWidget(
            self.used_battery_title
        )

        # ======================================================
        # USED BATTERY
        # ======================================================

        self.used_battery_rows = []

        self.used_battery_container = QWidget()

        self.used_battery_layout = QVBoxLayout(
            self.used_battery_container
        )

        self.used_battery_layout.setContentsMargins(
            0,0,0,0
        )

        self.used_battery_layout.setSpacing(7)

        # ------------------------------------------------------
        # ADD BUTTON
        # ------------------------------------------------------

        self.add_used_battery_button = QPushButton(
            "+ Tambah Aki Bekas"
        )

        self.add_used_battery_button.setObjectName(
            "Secondary"
        )

        self.used_battery_layout.addWidget(
            self.add_used_battery_button
        )

        used_layout.addWidget(
            self.used_battery_container
        )

        layout.addWidget(
            self.used_battery_frame
        )

        # ======================================================
        # PURCHASE / TRADE-IN PRICE
        # ======================================================

        self.used_battery_price = QLineEdit()

        self.used_battery_price.setPlaceholderText(
            "Harga beli / nilai tukar"
        )

        used_layout.addWidget(
            self.used_battery_price
        )

        layout.addWidget(
            self.used_battery_frame
        )

        # ======================================================
        # CUSTOMER
        # ======================================================

        self.customer_input = QLineEdit()

        self.customer_input.setPlaceholderText(
            "Pelanggan (opsional)"
        )

        layout.addWidget(
            self.customer_input
        )

        # ======================================================
        # VEHICLE
        # ======================================================

        self.vehicle_input = QLineEdit()

        self.vehicle_input.setPlaceholderText(
            "No. polisi / kendaraan (opsional)"
        )

        layout.addWidget(
            self.vehicle_input
        )

        # ======================================================
        # TOTAL
        # ======================================================

        total_layout = QHBoxLayout()

        total_layout.addWidget(
            QLabel(
                "TOTAL",
                objectName="Muted"
            )
        )

        total_layout.addStretch()

        self.total_label = QLabel(
            "Rp 0"
        )

        self.total_label.setAlignment(
            Qt.AlignRight
        )

        self.total_label.setStyleSheet(
            "font-size:25px;font-weight:700;"
        )

        total_layout.addWidget(
            self.total_label
        )

        layout.addLayout(
            total_layout
        )

        # ======================================================
        # PAYMENT BUTTON
        # ======================================================

        self.pay_button = QPushButton(
            "BAYAR"
        )

        self.pay_button.setObjectName(
            "Primary"
        )

        self.pay_button.clicked.connect(
            self.checkout
        )

        self.pay_button.setMinimumHeight(
            44
        )

        layout.addWidget(
            self.pay_button
        )

    def load_used_batteries(self):
        try:
            self.used_products = (ProductService.get_used_products())

        except Exception as e:
            print("ERROR LOAD USED BATTERIES:", e)

            self.used_products = []

    # ==========================================================
    # CONNECTIONS
    # ==========================================================

    def setup_connections(self):

        self.transaction_type.currentIndexChanged.connect(
            self.on_transaction_type_changed
        )

        self.used_battery_price.textChanged.connect(
            self.update_total
        )

        self.add_used_battery_button.clicked.connect(
            self.add_used_battery_row
        )

    # ==========================================================
    # TRANSACTION TYPE
    # ==========================================================

    def on_transaction_type_changed(self, index):

        # ------------------------------------------------------
        # 0 = PENJUALAN BIASA
        # ------------------------------------------------------

        if index == 0:

            self.used_battery_frame.hide()

            self.pay_button.setText(
                "BAYAR"
            )

        # ------------------------------------------------------
        # 1 = TUKAR TAMBAH
        # ------------------------------------------------------

        elif index == 1:

            self.used_battery_frame.show()

            self.used_battery_title.setText(
                "Aki Lama"
            )

            self.used_battery_price.setPlaceholderText(
                "Nilai tukar tambah"
            )

            self.pay_button.setText(
                "BAYAR SELISIH"
            )

        # ------------------------------------------------------
        # 2 = BELI AKI BEKAS
        # ------------------------------------------------------

        elif index == 2:

            self.used_battery_frame.show()

            self.used_battery_title.setText(
                "Aki Bekas"
            )

            self.used_battery_price.setPlaceholderText(
                "Harga beli aki bekas"
            )

            self.pay_button.setText(
                "BAYAR KE PELANGGAN"
            )

        self.update_total()

    # ==========================================================
    # ADD PRODUCT
    # ==========================================================

    def add_product(
        self,
        product,
        quantity=1
    ):

        # Beli aki bekas tidak menggunakan
        # product dari ProductList sebagai barang baru.
        if self.transaction_type.currentIndex() == 2:
            return
        
        # Beli aki baru saja dari ProductList sebagai barang baru.
        if self.transaction_type.currentIndex() == 0:
            item_id = product["item_id"]

            # ------------------------------------------------------
            # SUDAH ADA
            # ------------------------------------------------------

            for item in self.items:

                if item["item_id"] == item_id:

                    new_quantity = item["quantity"]+1

                    if new_quantity > product["quantity"]:

                        QMessageBox.warning(
                            self,
                            "Stok Tidak Cukup",
                            f'Stok {product["item_name"]} '
                            f'hanya {product["quantity"]}.'
                        )

                        return False

                    item["quantity"] = new_quantity

                    self.refresh()

                    return True

            # ------------------------------------------------------
            # STOK
            # ------------------------------------------------------

            if product["quantity"] <= 0:

                QMessageBox.warning(
                    self,
                    "Stok Habis",
                    f'Produk "{product["item_name"]}" '
                    "tidak memiliki stok."
                )

                return False

            if quantity > product["quantity"]:

                QMessageBox.warning(
                    self,
                    "Stok Tidak Cukup",
                    f'Stok {product["item_name"]} '
                    f'hanya {product["quantity"]}.'
                )

                return False

            # ------------------------------------------------------
            # ADD
            # ------------------------------------------------------

            self.items.append({
                "item_id": product["item_id"],
                "item_name": product["item_name"],
                "price": float(
                    product["selling_price"]
                ),
                "quantity": quantity,
                "quantity": 1,
            })

            self.refresh()

        # return True

    # ==========================================================
    # REFRESH
    # ==========================================================

    def refresh(self):

        self.table.setRowCount(
            len(self.items)
        )

        for row, item in enumerate(
            self.items
        ):

            total = (
                item["price"]
                * item["quantity"]
            )

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    item["item_name"]
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(item["quantity"])
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    rupiah(
                        item["price"]
                    )
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    rupiah(
                        total
                    )
                )
            )

            # --------------------------------------------------
            # DELETE BUTTON
            # --------------------------------------------------

            button = QPushButton("×")

            button.setObjectName(
                "Danger"
            )

            button.setCursor(
                Qt.PointingHandCursor
            )

            button.setFixedSize(
                28,
                28
            )

            button.setToolTip(
                "Hapus produk"
            )

            button.clicked.connect(
                lambda checked=False, r=row:
                self.remove_item(r)
            )

            self.table.setCellWidget(
                row,
                4,
                button
            )

        self.update_total()

    # ==========================================================
    # REMOVE
    # ==========================================================

    def remove_item(self, row):

        if 0 <= row < len(self.items):

            self.items.pop(row)

            self.refresh()

    # ==========================================================
    # TOTAL
    # ==========================================================

    def get_cart_total(self):

        return sum(
            item["price"]
            * item["quantity"]
            for item in self.items
        )

    def get_used_battery_value(self):

        total = 0

        for row in self.used_battery_rows:

            text = (
                row["price"]
                .text()
                .strip()
            )

            if not text:
                continue

            try:

                price = float(
                    text
                    .replace("Rp", "")
                    .replace(".", "")
                    .replace(",", "")
                    .strip()
                )

                total += price

            except ValueError:

                continue

        return total

    def get_total(self):

        transaction_type = (
            self.transaction_type.currentIndex()
        )

        cart_total = self.get_cart_total()

        used_value = (
            self.get_used_battery_value()
        )

        # ------------------------------------------------------
        # PENJUALAN BIASA
        # ------------------------------------------------------

        if transaction_type == 0:

            return cart_total

        # ------------------------------------------------------
        # TUKAR TAMBAH
        # ------------------------------------------------------

        if transaction_type == 1:

            return max(
                cart_total - used_value,
                0
            )

        # ------------------------------------------------------
        # BELI AKI BEKAS
        # ------------------------------------------------------

        if transaction_type == 2:

            return used_value

        return 0

    def update_total(self):

        total = self.get_total()

        self.total_label.setText(
            rupiah(total)
        )

        self.total_changed.emit(
            total
        )

    # ==========================================================
    # CLEAR
    # ==========================================================

    def clear(self):

        self.items.clear()

        self.customer_input.clear()

        self.vehicle_input.clear()

        self.used_battery_combo.setCurrentIndex(
            0
        )

        self.used_battery_price.clear()

        self.transaction_type.setCurrentIndex(
            0
        )

        self.refresh()

    def checkout(self):
        if self.table.rowCount() == 0:
            QMessageBox.warning(
                self,
                "Checkout",
                "Keranjang masih kosong."
            )

            return

        self.checkout_requested.emit(self.get_cart_data())

    def get_cart_data(self):
        items = []

        for item in self.items:
            product_id = item["item_id"]
            product_name = item["item_name"]
            quantity = item["quantity"]
            price = item["price"]

            total = price * quantity

            items.append({
                "product_id": product_id,
                "product_name": product_name,
                "quantity": quantity,
                "price": price,
                "total": total
            })

        transaction_type = (
            self.transaction_type.currentIndex()
        )

        return {
            "items": items,
            "transaction_type": transaction_type,
            "customer_name": self.customer_input.text().strip(),
            "vehicle_number": self.vehicle_input.text().strip(),
            "used_batteries": self.get_used_batteries(),
            "used_battery_total": self.get_used_battery_value(),
            "total": self.get_total()
        }

    def create_used_battery_row(self):

        row_widget = QWidget()

        row_layout = QHBoxLayout(
            row_widget
        )

        row_layout.setContentsMargins(
            0,0,0,0
        )

        row_layout.setSpacing(7)

        # ==================================================
        # COMBOBOX
        # ==================================================

        combo = QComboBox()

        combo.setObjectName(
            "ComboBoxFilter"
        )

        combo.addItem(
            "Pilih aki bekas...",
            None
        )

        for product in self.used_products:
            combo.addItem(
                product["item_name"],
                product["item_id"]
            )

        # ==================================================
        # PRICE
        # ==================================================

        price_input = QLineEdit()

        price_input.setPlaceholderText(
            "Harga beli"
        )

        # ==================================================
        # REMOVE BUTTON
        # ==================================================

        remove_button = QPushButton(
            "×"
        )

        remove_button.setObjectName(
            "Danger"
        )

        remove_button.setFixedWidth(
            32
        )

        # ==================================================
        # LAYOUT
        # ==================================================

        row_layout.addWidget(
            combo,
            2
        )

        row_layout.addWidget(
            price_input,
            1
        )

        row_layout.addWidget(
            remove_button
        )

        # ==================================================
        # INSERT BEFORE ADD BUTTON
        # ==================================================

        index = (
            self.used_battery_layout.count() - 1
        )

        self.used_battery_layout.insertWidget(
            index,
            row_widget
        )

        # ==================================================
        # SAVE ROW
        # ==================================================

        row_data = {
            "widget": row_widget,
            "combo": combo,
            "price": price_input
        }

        self.used_battery_rows.append(
            row_data
        )

        # ==================================================
        # CONNECTION
        # ==================================================

        price_input.textChanged.connect(
            self.update_total
        )

        remove_button.clicked.connect(
            lambda: self.remove_used_battery_row(
                row_data
            )
        )

        return row_data

    def remove_used_battery_row(
            self,
            row_data
    ):

        if row_data in self.used_battery_rows:
            self.used_battery_rows.remove(
                row_data
            )

        row_data["widget"].deleteLater()

        self.update_total()

    def add_used_battery_row(self):

        self.create_used_battery_row()

        self.update_total()

    def get_used_batteries(self):

        batteries = []

        for row in self.used_battery_rows:
            product_id = (
                row["combo"].currentData()
            )

            if not product_id:
                continue

            product_name = (
                row["combo"].currentText()
            )

            price = (
                self.get_price_from_input(
                    row["price"]
                )
            )

            batteries.append({
                "product_id": product_id,
                "product_name": product_name,
                "purchase_price": price
            })

        return batteries

    def get_price_from_input(
        self,
        input_widget
    ):

        text = (
            input_widget
            .text()
            .strip()
        )

        if not text:
            return 0

        try:

            return float(
                text
                .replace("Rp", "")
                .replace(".", "")
                .replace(",", "")
                .strip()
            )

        except ValueError:

            return 0
