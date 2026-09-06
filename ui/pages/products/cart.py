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
    QHeaderView
)

from ui.widgets.rupiah import rupiah

class Cart(QFrame):

    total_changed = pyqtSignal(float)

    def __init__(self):
        super().__init__()

        self.setObjectName("Panel")

        self.items = []

        self.setup_ui()
        self.setup_connections()

    # ==========================================================
    # UI
    # ==========================================================

    def setup_ui(self):

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel(
                "Keranjang",
                objectName="PanelTitle"
            )
        )

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

        self.table.verticalHeader().setVisible(False)

        header = self.table.horizontalHeader()

        # Produk → mengambil sisa ruang
        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )

        # Qty
        header.setSectionResizeMode(
            1,
            QHeaderView.Fixed
        )
        header.resizeSection(1, 60)

        # Harga
        header.setSectionResizeMode(
            2,
            QHeaderView.Fixed
        )
        header.resizeSection(2, 110)

        # Total
        header.setSectionResizeMode(
            3,
            QHeaderView.Fixed
        )
        header.resizeSection(3, 120)

        # Tombol hapus
        header.setSectionResizeMode(
            4,
            QHeaderView.Fixed
        )
        header.resizeSection(4, 40)

        layout.addWidget(
            self.table,
            1
        )

        self.customer_input = QLineEdit()
        self.customer_input.setPlaceholderText(
            "Pelanggan (opsional)"
        )

        layout.addWidget(
            self.customer_input
        )

        self.vehicle_input = QLineEdit()
        self.vehicle_input.setPlaceholderText(
            "No. polisi / kendaraan (opsional)"
        )

        layout.addWidget(
            self.vehicle_input
        )

        total_layout = QHBoxLayout()

        total_layout.addWidget(
            QLabel(
                "TOTAL",
                objectName="Muted"
            )
        )

        total_layout.addStretch()

        self.total_label = QLabel("Rp 0")

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

        self.pay_button = QPushButton(
            # "BAYAR  F4"
            "BAYAR"
        )

        self.pay_button.setObjectName(
            "Primary"
        )

        self.pay_button.setMinimumHeight(44)

        layout.addWidget(
            self.pay_button
        )

    # ==========================================================
    # CONNECTION
    # ==========================================================

    def setup_connections(self):

        pass

    # ==========================================================
    # ADD PRODUCT
    # ==========================================================

    def add_product(self, product):

        for item in self.items:

            if item["product_id"] == product["item_id"]:

                new_qty = item["quantity"] + 1

                if new_qty > product["quantity"]:

                    QMessageBox.warning(
                        self,
                        "Stok Tidak Cukup",
                        f'Stok {product["name"]} '
                        f'hanya {product["stock"]}.'
                    )

                    return

                item["quantity"] = new_qty

                self.refresh()

                return

        if product["quantity"] <= 0:

            QMessageBox.warning(
                self,
                "Stok Habis",
                f'Produk "{product["name"]}" '
                "tidak memiliki stok."
            )

            return

        self.items.append({
            "product_id": product["item_id"],
            "name": product["item_name"],
            "price": float(product["selling_price"]),
            "quantity": 1,
        })

        self.refresh()

    # ==========================================================
    # REFRESH
    # ==========================================================

    def refresh(self):

        self.table.setRowCount(
            len(self.items)
        )

        for row, item in enumerate(self.items):

            total = (
                item["price"]
                * item["quantity"]
            )

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    item["name"]
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

            button = QPushButton("x")
            button.setObjectName("Danger")
            button.setCursor(Qt.PointingHandCursor)
            button.setFixedSize(28, 28)
            button.setToolTip("Hapus Produk")

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

    def get_total(self):

        return sum(
            item["price"] * item["quantity"]
            for item in self.items
        )

    def update_total(self):

        total = self.get_total()

        self.total_label.setText(
            rupiah(total)
        )

        self.total_changed.emit(total)

    # ==========================================================
    # CLEAR
    # ==========================================================

    def clear(self):

        self.items.clear()

        self.customer_input.clear()
        self.vehicle_input.clear()

        self.refresh()

    # ==========================================================
    # FORMAT
    # ==========================================================
