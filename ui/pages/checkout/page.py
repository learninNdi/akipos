from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
    QFrame,
)

from ui.widgets.rupiah import rupiah
from ui.styles.pages.checkout import get_checkout_style


class CheckoutDialog(QDialog):

    def __init__(self, cart_data, parent=None, theme="dark"):
        super().__init__(parent)

        self.cart_data = cart_data or {}
        self.current_theme = theme

        self.payment_method = None
        self.received_amount = 0
        self.change_amount = 0

        # =====================================================
        # DIALOG
        # =====================================================

        self.setObjectName("CheckoutDialog")
        self.setWindowTitle("Checkout")
        self.setModal(True)
        self.setFixedWidth(520)

        # Theme HARUS dipasang sebelum UI dibuat
        self.apply_theme()

        # =====================================================
        # UI
        # =====================================================

        self.setup_ui()
        self.setup_connections()
        self.update_payment_ui()

    # =========================================================
    # THEME
    # =========================================================

    def set_theme(self, theme):
        """
        Mengubah tema CheckoutDialog.
        theme: "dark" atau "light"
        """
        if theme not in ("dark", "light"):
            theme = "dark"

        self.current_theme = theme
        self.apply_theme()

    def apply_theme(self):
        """
        Apply stylesheet sesuai tema aktif.
        """
        self.setStyleSheet(
            get_checkout_style(self.current_theme)
        )

        # Refresh style object yang memakai dynamic objectName
        if hasattr(self, "change_label"):
            self.change_label.style().unpolish(
                self.change_label
            )
            self.change_label.style().polish(
                self.change_label
            )

    # =========================================================
    # UI
    # =========================================================

    def setup_ui(self):

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            25, 25, 25, 25
        )

        main_layout.setSpacing(18)

        # =====================================================
        # HEADER
        # =====================================================

        header_layout = QHBoxLayout()

        title_layout = QVBoxLayout()
        title_layout.setSpacing(2)

        title = QLabel("Checkout")
        title.setObjectName("CheckoutTitle")

        subtitle = QLabel(
            "Selesaikan pembayaran transaksi"
        )
        subtitle.setObjectName("CheckoutSubtitle")

        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)

        header_layout.addLayout(title_layout)
        header_layout.addStretch()

        main_layout.addLayout(header_layout)

        # =====================================================
        # TOTAL CARD
        # =====================================================

        total_card = QFrame()
        total_card.setObjectName("TotalCard")

        total_layout = QVBoxLayout(total_card)

        total_layout.setContentsMargins(
            20, 18, 20, 18
        )

        total_layout.setSpacing(5)

        total_caption = QLabel(
            "TOTAL PEMBAYARAN"
        )
        total_caption.setObjectName(
            "TotalCaption"
        )

        self.total_label = QLabel(
            rupiah(
                self.cart_data.get("total", 0)
            )
        )

        self.total_label.setObjectName(
            "TotalAmount"
        )

        self.total_label.setAlignment(
            Qt.AlignRight
        )

        total_layout.addWidget(
            total_caption
        )

        total_layout.addWidget(
            self.total_label
        )

        main_layout.addWidget(
            total_card
        )

        # =====================================================
        # PAYMENT METHOD
        # =====================================================

        payment_label = QLabel(
            "Metode Pembayaran"
        )

        payment_label.setObjectName(
            "SectionTitle"
        )

        main_layout.addWidget(
            payment_label
        )

        self.payment_combo = QComboBox()

        self.payment_combo.setObjectName(
            "PaymentCombo"
        )

        self.payment_combo.setFixedHeight(44)

        self.payment_combo.addItems([
            "Cash",
            "Transfer",
            "QRIS",
        ])

        main_layout.addWidget(
            self.payment_combo
        )

        # =====================================================
        # CASH SECTION
        # =====================================================

        self.cash_frame = QFrame()

        self.cash_frame.setObjectName(
            "CashFrame"
        )

        cash_layout = QVBoxLayout(
            self.cash_frame
        )

        cash_layout.setContentsMargins(
            16, 16, 16, 16
        )

        cash_layout.setSpacing(10)

        # -----------------------------------------------------
        # RECEIVED
        # -----------------------------------------------------

        received_title = QLabel(
            "Uang Diterima"
        )

        received_title.setObjectName(
            "FieldLabel"
        )

        self.received_input = QLineEdit()

        self.received_input.setObjectName(
            "ReceivedInput"
        )

        self.received_input.setPlaceholderText(
            "Masukkan jumlah uang"
        )

        self.received_input.setFixedHeight(
            44
        )

        cash_layout.addWidget(
            received_title
        )

        cash_layout.addWidget(
            self.received_input
        )

        # =====================================================
        # QUICK CASH
        # =====================================================

        quick_layout = QHBoxLayout()
        quick_layout.setSpacing(8)

        self.quick_buttons = []

        quick_values = [
            50000,
            100000,
            200000,
            500000,
        ]

        for value in quick_values:

            button = QPushButton(
                rupiah(value)
            )

            button.setObjectName(
                "QuickCash"
            )

            button.setCursor(
                Qt.PointingHandCursor
            )

            button.setFixedHeight(34)

            button.clicked.connect(
                lambda checked=False,
                amount=value:
                self.set_received_amount(
                    amount
                )
            )

            quick_layout.addWidget(
                button
            )

            self.quick_buttons.append(
                button
            )

        cash_layout.addLayout(
            quick_layout
        )

        # =====================================================
        # CHANGE
        # =====================================================

        change_layout = QHBoxLayout()

        change_title = QLabel(
            "Kembalian"
        )

        change_title.setObjectName(
            "FieldLabel"
        )

        self.change_label = QLabel(
            "Rp 0"
        )

        self.change_label.setObjectName(
            "ChangeAmount"
        )

        self.change_label.setAlignment(
            Qt.AlignRight
        )

        change_layout.addWidget(
            change_title
        )

        change_layout.addWidget(
            self.change_label
        )

        cash_layout.addLayout(
            change_layout
        )

        main_layout.addWidget(
            self.cash_frame
        )

        # =====================================================
        # BOTTOM BUTTON
        # =====================================================

        main_layout.addStretch()

        button_layout = QHBoxLayout()

        button_layout.setSpacing(10)

        # -----------------------------------------------------
        # CANCEL
        # -----------------------------------------------------

        self.cancel_button = QPushButton(
            "BATAL"
        )

        self.cancel_button.setObjectName(
            "Secondary"
        )

        self.cancel_button.setCursor(
            Qt.PointingHandCursor
        )

        self.cancel_button.setFixedHeight(
            46
        )

        # -----------------------------------------------------
        # CONFIRM
        # -----------------------------------------------------

        self.confirm_button = QPushButton(
            "KONFIRMASI"
        )

        self.confirm_button.setObjectName(
            "Primary"
        )

        self.confirm_button.setCursor(
            Qt.PointingHandCursor
        )

        self.confirm_button.setFixedHeight(
            46
        )

        self.confirm_button.setDefault(
            True
        )

        button_layout.addWidget(
            self.cancel_button,
            1
        )

        button_layout.addWidget(
            self.confirm_button,
            2
        )

        main_layout.addLayout(
            button_layout
        )

    # =========================================================
    # CONNECTION
    # =========================================================

    def setup_connections(self):

        self.payment_combo.currentIndexChanged.connect(
            self.update_payment_ui
        )

        self.received_input.textChanged.connect(
            self.calculate_change
        )

        self.cancel_button.clicked.connect(
            self.reject
        )

        self.confirm_button.clicked.connect(
            self.confirm_payment
        )

    # =========================================================
    # PAYMENT UI
    # =========================================================

    def update_payment_ui(self):

        method = self.payment_combo.currentText()

        if method == "Cash":

            self.cash_frame.show()

            self.received_input.setFocus()

        else:

            self.cash_frame.hide()

            self.change_label.setText(
                "Rp 0"
            )

    # =========================================================
    # QUICK CASH
    # =========================================================

    def set_received_amount(self, amount):

        self.received_input.setText(
            rupiah(amount)
        )

        self.received_input.setFocus()

        self.received_input.selectAll()

    # =========================================================
    # CHANGE
    # =========================================================

    def calculate_change(self):

        if self.payment_combo.currentText() != "Cash":
            return

        received = self.parse_currency(
            self.received_input.text()
        )

        total = float(
            self.cart_data.get(
                "total",
                0
            )
        )

        change = received - total

        if received <= 0:

            self.change_label.setText(
                "Rp 0"
            )

            self.change_label.setObjectName(
                "ChangeAmount"
            )

        elif change >= 0:

            self.change_label.setText(
                rupiah(change)
            )

            self.change_label.setObjectName(
                "ChangeAmount"
            )

        else:

            self.change_label.setText(
                "Kurang " +
                rupiah(abs(change))
            )

            self.change_label.setObjectName(
                "ChangeWarning"
            )

        self.change_label.style().unpolish(
            self.change_label
        )

        self.change_label.style().polish(
            self.change_label
        )

        self.change_label.update()

    # =========================================================
    # CONFIRM
    # =========================================================

    def confirm_payment(self):

        method = self.payment_combo.currentText()

        total = float(
            self.cart_data.get(
                "total",
                0
            )
        )

        # =====================================================
        # CASH
        # =====================================================

        if method == "Cash":

            received = self.parse_currency(
                self.received_input.text()
            )

            if received < total:

                self.received_input.setFocus()

                self.received_input.selectAll()

                return

            self.payment_method = "cash"

            self.received_amount = received

            self.change_amount = (
                received - total
            )

        # =====================================================
        # TRANSFER
        # =====================================================

        elif method == "Transfer":

            self.payment_method = "transfer"

            self.received_amount = total

            self.change_amount = 0

        # =====================================================
        # QRIS
        # =====================================================

        elif method == "QRIS":

            self.payment_method = "qris"

            self.received_amount = total

            self.change_amount = 0

        # =====================================================
        # ACCEPT
        # =====================================================

        self.accept()

    # =========================================================
    # RESULT
    # =========================================================

    def get_payment_data(self):

        return {
            "payment_method": self.payment_method,

            "total": float(
                self.cart_data.get(
                    "total",
                    0
                )
            ),

            "received_amount":
                self.received_amount,

            "change_amount":
                self.change_amount,
        }

    # =========================================================
    # FORMAT
    # =========================================================

    @staticmethod
    def parse_currency(value):

        if not value:
            return 0

        value = str(value)

        value = value.replace(
            "Rp", ""
        )

        value = value.replace(
            "rp", ""
        )

        value = value.replace(
            " ",
            ""
        )

        value = value.replace(
            ".",
            ""
        )

        value = value.replace(
            ",",
            "."
        )

        try:

            return float(value)

        except ValueError:

            return 0