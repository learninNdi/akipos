from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QSizePolicy,
)


class DashboardPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("dashboardPage")

        self.setup_ui()

    # ========================================================
    # SETUP UI
    # ========================================================

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            24,
            24,
            24,
            24
        )

        main_layout.setSpacing(20)

        # ====================================================
        # PAGE HEADER
        # ====================================================

        title = QLabel("Dashboard")
        title.setObjectName("pageTitle")

        subtitle = QLabel(
            "Ringkasan aktivitas toko aki"
        )
        subtitle.setObjectName("pageSubtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # ====================================================
        # SUMMARY CARDS
        # ====================================================

        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(16)

        self.sales_card = self.create_summary_card(
            title="Penjualan Hari Ini",
            value="Rp0",
            object_name="salesCard"
        )

        self.transaction_card = self.create_summary_card(
            title="Transaksi Hari Ini",
            value="0",
            object_name="transactionCard"
        )

        self.profit_card = self.create_summary_card(
            title="Laba Hari Ini",
            value="Rp0",
            object_name="profitCard"
        )

        self.stock_card = self.create_summary_card(
            title="Produk Stok Menipis",
            value="0",
            object_name="stockCard"
        )

        cards_layout.addWidget(
            self.sales_card,
            1
        )

        cards_layout.addWidget(
            self.transaction_card,
            1
        )

        cards_layout.addWidget(
            self.profit_card,
            1
        )

        cards_layout.addWidget(
            self.stock_card,
            1
        )

        main_layout.addLayout(
            cards_layout
        )

        # ====================================================
        # BOTTOM CONTENT
        # ====================================================

        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(16)

        # ----------------------------------------------------
        # RECENT SALES
        # ----------------------------------------------------

        recent_sales_frame = QFrame()
        recent_sales_frame.setObjectName(
            "dashboardPanel"
        )

        recent_sales_layout = QVBoxLayout(
            recent_sales_frame
        )

        recent_sales_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        recent_sales_layout.setSpacing(12)

        recent_sales_title = QLabel(
            "Penjualan Terbaru"
        )

        recent_sales_title.setObjectName(
            "panelTitle"
        )

        recent_sales_layout.addWidget(
            recent_sales_title
        )

        recent_sales_info = QLabel(
            "Belum ada data penjualan."
        )

        recent_sales_info.setObjectName(
            "emptyLabel"
        )

        recent_sales_info.setAlignment(
            Qt.AlignCenter
        )

        recent_sales_layout.addWidget(
            recent_sales_info,
            1
        )

        # ----------------------------------------------------
        # LOW STOCK
        # ----------------------------------------------------

        low_stock_frame = QFrame()
        low_stock_frame.setObjectName(
            "dashboardPanel"
        )

        low_stock_layout = QVBoxLayout(
            low_stock_frame
        )

        low_stock_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )

        low_stock_layout.setSpacing(12)

        low_stock_title = QLabel(
            "Stok Menipis"
        )

        low_stock_title.setObjectName(
            "panelTitle"
        )

        low_stock_layout.addWidget(
            low_stock_title
        )

        low_stock_info = QLabel(
            "Tidak ada produk stok menipis."
        )

        low_stock_info.setObjectName(
            "emptyLabel"
        )

        low_stock_info.setAlignment(
            Qt.AlignCenter
        )

        low_stock_layout.addWidget(
            low_stock_info,
            1
        )

        # ====================================================
        # ADD BOTTOM PANELS
        # ====================================================

        bottom_layout.addWidget(
            recent_sales_frame,
            2
        )

        bottom_layout.addWidget(
            low_stock_frame,
            1
        )

        main_layout.addLayout(
            bottom_layout,
            1
        )

    # ========================================================
    # CREATE SUMMARY CARD
    # ========================================================

    def create_summary_card(
        self,
        title,
        value,
        object_name
    ):
        card = QFrame()

        card.setObjectName(
            object_name
        )

        card.setMinimumHeight(
            120
        )

        card.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )

        layout = QVBoxLayout(card)

        layout.setContentsMargins(
            20,
            16,
            20,
            16
        )

        layout.setSpacing(8)

        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "cardTitle"
        )

        value_label = QLabel(
            value
        )

        value_label.setObjectName(
            "cardValue"
        )

        layout.addWidget(
            title_label
        )

        layout.addWidget(
            value_label
        )

        card.value_label = value_label

        return card