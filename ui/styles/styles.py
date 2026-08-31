DARK_THEME = """
QMainWindow { background:#0b1220; }
QWidget { font-family:"Segoe UI"; font-size:15px; color:#e5e7eb; }
QFrame#Sidebar { background:#111827; }
QLabel#Brand { color:#fff; font-size:32px; font-weight:700; }
QLabel#BrandSub { color:#94a3b8; font-size:16px; }
QLabel#Muted { color:#94a3b8; font-size:21px; }
QPushButton#Nav {
    background:transparent; color:#cbd5e1; border:0;
    border-radius:7px; text-align:left; padding:12px; font-size:21px;
}
QPushButton#Nav:hover { background:#1e293b; color:#fff; }
QPushButton#Nav[active="true"] { background:#2563eb; color:#fff; font-weight:700; }
QFrame#TopBar { background:#111827; border-bottom:1px solid #263244; }
QLabel#PageTitle { color:#f8fafc; font-size:24px; font-weight:700; }
QFrame#Card, QFrame#Panel {
    background:#172235; border:1px solid #29364a; border-radius:10px;
}
QLabel#CardTitle { color:#94a3b8; font-size:14px; }
QLabel#CardValue { color:#f8fafc; font-size:24px; font-weight:700; }
QLabel#PanelTitle { color:#f8fafc; font-size:17px; font-weight:700; }
QLineEdit, QComboBox {
    background:#111827; color:#e5e7eb; border:1px solid #334155;
    border-radius:7px; padding:9px 10px;
}
QLineEdit:focus, QComboBox:focus { border:1px solid #3b82f6; }
QPushButton#Primary, QPushButton#Secondary, QPushButton#Theme {
    min-height:24px; padding:9px 14px; border-radius:7px; font-weight:600;
}
QPushButton#Primary { background:#2563eb; color:#fff; border:0; }
QPushButton#Primary:hover { background:#1d4ed8; }
QPushButton#Secondary, QPushButton#Theme {
    background:#1e293b; color:#e5e7eb; border:1px solid #334155;
}
QPushButton#Secondary:hover, QPushButton#Theme:hover { background:#26354b; }
QTableWidget {
    background:#172235; alternate-background-color:#142033; color:#e5e7eb;
    border:0; gridline-color:#29364a; selection-background-color:#1d4ed8;
    selection-color:#fff;
}
QHeaderView::section {
    background:#111827; color:#94a3b8; border:0;
    border-bottom:1px solid #29364a; padding:10px 8px; font-weight:700;
}
QSplitter::handle { background:#29364a; }

SalesBarChart#painterBackgroundColor { background:#0b1220; }
"""

LIGHT_THEME = """
QMainWindow { background:#f4f6fa; }
QWidget { font-family:"Segoe UI"; font-size:15px; color:#172033; }
QFrame#Sidebar { background:#172033; }
QLabel#Brand { color:#fff; font-size:32px; font-weight:700; }
QLabel#BrandSub { color:#94a3b8; font-size:16px; }
QLabel#Muted { color:#94a3b8; font-size:21px; }
QPushButton#Nav {
    background:transparent; color:#cbd5e1; border:0;
    border-radius:7px; text-align:left; padding:12px; font-size:21px;
}
QPushButton#Nav:hover { background:#26334d; color:#fff; }
QPushButton#Nav[active="true"] { background:#2563eb; color:#fff; font-weight:700; }
QFrame#TopBar { background:#fff; border-bottom:1px solid #e5e7eb; }
QLabel#PageTitle { color:#111827; font-size:24px; font-weight:700; }
QFrame#Card, QFrame#Panel {
    background:#fff; border:1px solid #e2e8f0; border-radius:10px;
}
QLabel#CardTitle { color:#64748b; font-size:14px; }
QLabel#CardValue { color:#111827; font-size:24px; font-weight:700; }
QLabel#PanelTitle { color:#111827; font-size:17px; font-weight:700; }
QLineEdit, QComboBox {
    background:#fff; color:#111827; border:1px solid #cbd5e1;
    border-radius:7px; padding:9px 10px;
}
QLineEdit:focus, QComboBox:focus { border:1px solid #2563eb; }
QPushButton#Primary, QPushButton#Secondary, QPushButton#Theme {
    min-height:24px; padding:9px 14px; border-radius:7px; font-weight:600;
}
QPushButton#Primary { background:#2563eb; color:#fff; border:0; }
QPushButton#Primary:hover { background:#1d4ed8; }
QPushButton#Secondary, QPushButton#Theme {
    background:#fff; color:#374151; border:1px solid #cbd5e1;
}
QPushButton#Secondary:hover, QPushButton#Theme:hover { background:#f8fafc; }
QTableWidget {
    background:#fff; alternate-background-color:#f8fafc; color:#172033;
    border:0; gridline-color:#e5e7eb; selection-background-color:#dbeafe;
    selection-color:#111827;
}
QHeaderView::section {
    background:#f8fafc; color:#475569; border:0;
    border-bottom:1px solid #e5e7eb; padding:10px 8px; font-weight:700;
}
QSplitter::handle { background:#e5e7eb; }

SalesBarChart#painterBackgroundColor { background:#f4f6fa; }
"""