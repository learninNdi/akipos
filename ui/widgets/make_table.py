from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QTableWidget,
    QHeaderView,
    QSizePolicy,
    QTableWidgetItem
)

def make_table(headers, rows=()):
    t = QTableWidget(0, len(headers))
    t.setHorizontalHeaderLabels(headers)
    t.setSelectionBehavior(QTableWidget.SelectRows)
    t.setEditTriggers(QTableWidget.NoEditTriggers)
    t.verticalHeader().setVisible(False)
    t.verticalHeader().setDefaultSectionSize(40)
    t.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    t.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    for values in rows:
        r = t.rowCount()
        t.insertRow(r)
        for c, value in enumerate(values):
            item = QTableWidgetItem(str(value))
            item.setTextAlignment(
                Qt.AlignRight | Qt.AlignVCenter if c >= 2
                else Qt.AlignLeft | Qt.AlignVCenter
            )
            t.setItem(r, c, item)
    return t