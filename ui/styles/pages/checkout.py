CHECKOUT_STYLE = """
QDialog {
    background-color: #0b1220;
}

/* ==============================
   HEADER
   ============================== */

QLabel#CheckoutTitle {
    font-size: 24px;
    font-weight: 700;
}

QLabel#CheckoutSubtitle {
    color: #888888;
    font-size: 13px;
}

/* ==============================
   SECTION
   ============================== */

QLabel#SectionTitle {
    font-size: 14px;
    font-weight: 600;
}

QLabel#FieldLabel {
    font-size: 13px;
    font-weight: 600;
    color: #aaaaaa;
}

/* ==============================
   TOTAL
   ============================== */

QFrame#TotalCard {
    background-color: #111827;
    border: 1px solid #333333;
    border-radius: 10px;
}

QLabel#TotalCaption {
    color: #999999;
    font-size: 12px;
    font-weight: 600;
}

QLabel#TotalAmount {
    font-size: 32px;
    font-weight: 700;
}

/* ==============================
   CASH
   ============================== */

QFrame#CashFrame {
    background-color: #202020;
    border: 1px solid #333333;
    border-radius: 8px;
}

/* ==============================
   INPUT
   ============================== */

QLineEdit {
    background-color: #292929;
    border: 1px solid #444444;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 15px;
}

QLineEdit:focus {
    border: 1px solid #777777;
}

/* ==============================
   COMBOBOX
   ============================== */

QComboBox {
    background-color: #292929;
    border: 1px solid #444444;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 15px;
}

QComboBox:hover {
    border: 1px solid #666666;
}

/* ==============================
   QUICK CASH
   ============================== */

QPushButton#QuickCash {
    background-color: #292929;
    border: 1px solid #444444;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 11px;
}

QPushButton#QuickCash:hover {
    background-color: #353535;
}

/* ==============================
   CHANGE
   ============================== */

QLabel#ChangeAmount {
    font-size: 20px;
    font-weight: 700;
}

QLabel#ChangeWarning {
    color: #ff8585;
    font-size: 20px;
    font-weight: 700;
}

/* ==============================
   BUTTON
   ============================== */

QPushButton#Primary {
    background-color: #3b82f6;
    color: white;
    border: none;
    border-radius: 6px;
    font-weight: 700;
    font-size: 14px;
}

QPushButton#Primary:hover {
    background-color: #4b8df8;
}

QPushButton#Primary:pressed {
    background-color: #2869cc;
}

QPushButton#Secondary {
    background-color: #292929;
    color: #dddddd;
    border: 1px solid #444444;
    border-radius: 6px;
    font-weight: 600;
    font-size: 14px;
}

QPushButton#Secondary:hover {
    background-color: #353535;
}
"""