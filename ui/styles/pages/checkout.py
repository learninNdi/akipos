DARK_CHECKOUT_STYLE = """
/* =========================================================
   DIALOG
   ========================================================= */

QDialog#CheckoutDialog {
    background-color: #0b1220;
}


/* =========================================================
   HEADER
   ========================================================= */

QLabel#CheckoutTitle {
    color: #f8fafc;
    font-size: 24px;
    font-weight: 700;
}

QLabel#CheckoutSubtitle {
    color: #94a3b8;
    font-size: 13px;
}


/* =========================================================
   SECTION
   ========================================================= */

QLabel#SectionTitle {
    color: #f1f5f9;
    font-size: 14px;
    font-weight: 600;
}

QLabel#FieldLabel {
    color: #a8b3c2;
    font-size: 13px;
    font-weight: 600;
}


/* =========================================================
   TOTAL CARD
   ========================================================= */

QFrame#TotalCard {
    background-color: #151e2d;
    border: 1px solid #263449;
    border-radius: 10px;
}

QLabel#TotalCaption {
    color: #8d9aab;
    font-size: 11px;
    font-weight: 600;
}

QLabel#TotalAmount {
    color: #ffffff;
    font-size: 30px;
    font-weight: 700;
}


/* =========================================================
   PAYMENT COMBO
   ========================================================= */

QComboBox#PaymentCombo {
    background-color: #151e2d;
    color: #f8fafc;
    border: 1px solid #34445c;
    border-radius: 7px;
    padding-left: 12px;
    padding-right: 12px;
    font-size: 13px;
}

QComboBox#PaymentCombo:hover {
    border: 1px solid #4b5f7d;
}

QComboBox#PaymentCombo:focus {
    border: 1px solid #4f8df7;
}

QComboBox#PaymentCombo::drop-down {
    width: 30px;
    border: none;
}

QComboBox#PaymentCombo QAbstractItemView {
    background-color: #151e2d;
    color: #f8fafc;
    border: 1px solid #34445c;
    selection-background-color: #29405f;
    selection-color: #ffffff;
}


/* =========================================================
   CASH FRAME
   ========================================================= */

QFrame#CashFrame {
    background-color: #151e2d;
    border: 1px solid #263449;
    border-radius: 8px;
}


/* =========================================================
   RECEIVED INPUT
   ========================================================= */

QLineEdit#ReceivedInput {
    background-color: #0f1724;
    color: #ffffff;
    border: 1px solid #34445c;
    border-radius: 7px;
    padding-left: 12px;
    padding-right: 12px;
    font-size: 15px;
}

QLineEdit#ReceivedInput:hover {
    border: 1px solid #4b5f7d;
}

QLineEdit#ReceivedInput:focus {
    border: 1px solid #4f8df7;
}

QLineEdit#ReceivedInput::placeholder {
    color: #66758a;
}


/* =========================================================
   QUICK CASH
   ========================================================= */

QPushButton#QuickCash {
    background-color: #202c3e;
    color: #dbe4ef;
    border: 1px solid #35465e;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 11px;
}

QPushButton#QuickCash:hover {
    background-color: #2a394e;
    border: 1px solid #4a5d79;
}

QPushButton#QuickCash:pressed {
    background-color: #182333;
}


/* =========================================================
   CHANGE
   ========================================================= */

QLabel#ChangeAmount {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
}

QLabel#ChangeWarning {
    color: #ef4444;
    font-size: 20px;
    font-weight: 700;
}


/* =========================================================
   SECONDARY BUTTON
   ========================================================= */

QPushButton#Secondary {
    background-color: #202c3e;
    color: #dbe4ef;
    border: 1px solid #35465e;
    border-radius: 7px;
    font-size: 13px;
    font-weight: 600;
}

QPushButton#Secondary:hover {
    background-color: #2a394e;
}

QPushButton#Secondary:pressed {
    background-color: #182333;
}


/* =========================================================
   PRIMARY BUTTON
   ========================================================= */

QPushButton#Primary {
    background-color: #2563eb;
    color: #ffffff;
    border: none;
    border-radius: 7px;
    font-size: 13px;
    font-weight: 600;
}

QPushButton#Primary:hover {
    background-color: #3474f0;
}

QPushButton#Primary:pressed {
    background-color: #1d4ed8;
}

QPushButton#Primary:disabled {
    background-color: #334155;
    color: #7c8797;
}
"""


LIGHT_CHECKOUT_STYLE = """
/* =========================================================
   DIALOG
   ========================================================= */

QDialog#CheckoutDialog {
    background-color: #f4f6f8;
}


/* =========================================================
   HEADER
   ========================================================= */

QLabel#CheckoutTitle {
    color: #202124;
    font-size: 24px;
    font-weight: 700;
}

QLabel#CheckoutSubtitle {
    color: #6b7280;
    font-size: 13px;
}


/* =========================================================
   SECTION
   ========================================================= */

QLabel#SectionTitle {
    color: #202124;
    font-size: 14px;
    font-weight: 600;
}

QLabel#FieldLabel {
    color: #4b5563;
    font-size: 13px;
    font-weight: 600;
}


/* =========================================================
   TOTAL CARD
   ========================================================= */

QFrame#TotalCard {
    background-color: #ffffff;
    border: 1px solid #e1e5ea;
    border-radius: 10px;
}

QLabel#TotalCaption {
    color: #6b7280;
    font-size: 11px;
    font-weight: 600;
}

QLabel#TotalAmount {
    color: #202124;
    font-size: 30px;
    font-weight: 700;
}


/* =========================================================
   PAYMENT COMBO
   ========================================================= */

QComboBox#PaymentCombo {
    background-color: #ffffff;
    color: #202124;
    border: 1px solid #cfd4da;
    border-radius: 7px;
    padding-left: 12px;
    padding-right: 12px;
    font-size: 13px;
}

QComboBox#PaymentCombo:hover {
    border: 1px solid #aeb4bb;
}

QComboBox#PaymentCombo:focus {
    border: 1px solid #4285f4;
}

QComboBox#PaymentCombo::drop-down {
    width: 30px;
    border: none;
}

QComboBox#PaymentCombo QAbstractItemView {
    background-color: #ffffff;
    color: #202124;
    border: 1px solid #cfd4da;
    selection-background-color: #e8f0fe;
    selection-color: #202124;
}


/* =========================================================
   CASH FRAME
   ========================================================= */

QFrame#CashFrame {
    background-color: #ffffff;
    border: 1px solid #e1e5ea;
    border-radius: 8px;
}


/* =========================================================
   RECEIVED INPUT
   ========================================================= */

QLineEdit#ReceivedInput {
    background-color: #ffffff;
    color: #202124;
    border: 1px solid #cfd4da;
    border-radius: 7px;
    padding-left: 12px;
    padding-right: 12px;
    font-size: 15px;
}

QLineEdit#ReceivedInput:hover {
    border: 1px solid #aeb4bb;
}

QLineEdit#ReceivedInput:focus {
    border: 1px solid #4285f4;
}

QLineEdit#ReceivedInput::placeholder {
    color: #9aa0a6;
}


/* =========================================================
   QUICK CASH
   ========================================================= */

QPushButton#QuickCash {
    background-color: #ffffff;
    color: #374151;
    border: 1px solid #d1d5db;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 11px;
}

QPushButton#QuickCash:hover {
    background-color: #f3f4f6;
    border: 1px solid #aeb4bb;
}

QPushButton#QuickCash:pressed {
    background-color: #e5e7eb;
}


/* =========================================================
   CHANGE
   ========================================================= */

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


/* =========================================================
   SECONDARY BUTTON
   ========================================================= */

QPushButton#Secondary {
    background-color: #ffffff;
    color: #374151;
    border: 1px solid #d1d5db;
    border-radius: 7px;
    font-size: 13px;
    font-weight: 600;
}

QPushButton#Secondary:hover {
    background-color: #f3f4f6;
}

QPushButton#Secondary:pressed {
    background-color: #e5e7eb;
}


/* =========================================================
   PRIMARY BUTTON
   ========================================================= */

QPushButton#Primary {
    background-color: #2563eb;
    color: #ffffff;
    border: none;
    border-radius: 7px;
    font-size: 13px;
    font-weight: 600;
}

QPushButton#Primary:hover {
    background-color: #1d4ed8;
}

QPushButton#Primary:pressed {
    background-color: #1e40af;
}

QPushButton#Primary:disabled {
    background-color: #d1d5db;
    color: #9ca3af;
}
"""


def get_checkout_style(theme):
    if theme == "light":
        return LIGHT_CHECKOUT_STYLE

    return DARK_CHECKOUT_STYLE