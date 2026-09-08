DARK_CHECKOUT_STYLE = """
QDialog#CheckoutDialog {
    background-color: #0b1220;
}

/* ==============================
   HEADER
   ============================== */

QLabel#CheckoutTitle {
    color: #f5f5f5;
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
    color: #f0f0f0;
    font-size: 14px;
    font-weight: 600;
}

QLabel#FieldLabel {
    color: #aaaaaa;
    font-size: 13px;
    font-weight: 600;
}

/* ==============================
   TOTAL CARD
   ============================== */

QFrame#TotalCard {
    background-color: #222222;
    border: 1px solid #333333;
    border-radius: 10px;
}

QLabel#TotalCaption {
    color: #999999;
    font-size: 11px;
    font-weight: 600;
}

QLabel#TotalAmount {
    color: #ffffff;
    font-size: 30px;
    font-weight: 700;
}

/* ==============================
   CASH FRAME
   ============================== */

QFrame#CashFrame {
    background-color: #202020;
    border: 1px solid #333333;
    border-radius: 8px;
}

/* ==============================
   QUICK CASH
   ============================== */

QPushButton#QuickCash {
    background-color: #292929;
    color: #dddddd;
    border: 1px solid #444444;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 11px;
}

QPushButton#QuickCash:hover {
    background-color: #353535;
}

QPushButton#QuickCash:pressed {
    background-color: #222222;
}

/* ==============================
   CHANGE
   ============================== */

QLabel#ChangeAmount {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
}

QLabel#ChangeWarning {
    color: #ff7777;
    font-size: 20px;
    font-weight: 700;
}

"""


LIGHT_CHECKOUT_STYLE = """
QDialog#CheckoutDialog {
    background-color: #f5f6f8;
}

/* ==============================
   HEADER
   ============================== */

QLabel#CheckoutTitle {
    color: #202124;
    font-size: 24px;
    font-weight: 700;
}

QLabel#CheckoutSubtitle {
    color: #777777;
    font-size: 13px;
}

/* ==============================
   SECTION
   ============================== */

QLabel#SectionTitle {
    color: #202124;
    font-size: 14px;
    font-weight: 600;
}

QLabel#FieldLabel {
    color: #666666;
    font-size: 13px;
    font-weight: 600;
}

/* ==============================
   TOTAL CARD
   ============================== */

QFrame#TotalCard {
    background-color: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 10px;
}

QLabel#TotalCaption {
    color: #777777;
    font-size: 11px;
    font-weight: 600;
}

QLabel#TotalAmount {
    color: #202124;
    font-size: 30px;
    font-weight: 700;
}

/* ==============================
   CASH FRAME
   ============================== */

QFrame#CashFrame {
    background-color: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 8px;
}

/* ==============================
   QUICK CASH
   ============================== */

QPushButton#QuickCash {
    background-color: #ffffff;
    color: #333333;
    border: 1px solid #cccccc;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 11px;
}

QPushButton#QuickCash:hover {
    background-color: #eeeeee;
}

QPushButton#QuickCash:pressed {
    background-color: #e5e5e5;
}

/* ==============================
   CHANGE
   ============================== */

QLabel#ChangeAmount {
    color: #202124;
    font-size: 20px;
    font-weight: 700;
}

QLabel#ChangeWarning {
    color: #d93025;
    font-size: 20px;
    font-weight: 700;
}
"""


def get_checkout_style(theme):
    if theme == "light":
        return LIGHT_CHECKOUT_STYLE

    return DARK_CHECKOUT_STYLE